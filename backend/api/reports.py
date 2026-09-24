"""Reports and data export router."""

import io
import csv
from fastapi import APIRouter, Depends, Response
from backend.auth.dependencies import CurrentUser, get_current_user
from backend.database import get_db
from backend.services.inventory_service import list_inventory
from backend.services.sales_service import list_sales
from smartstock.db.operations import fetch_all

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/inventory/csv")
def export_inventory_csv(user: CurrentUser = Depends(get_current_user)):
    """Export current multi-store inventory snapshot as CSV."""
    records = list_inventory()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Store", "SKU", "Product Name", "Category", "Unit Cost", "Unit Price",
        "On Hand", "Reserved", "Available", "Days of Stock", "Health Status", "Total Value"
    ])
    for r in records:
        writer.writerow([
            r.store_name, r.sku, r.product_name, r.category_name, r.unit_cost, r.unit_price,
            r.quantity_on_hand, r.quantity_reserved, r.quantity_available,
            r.days_of_stock or "N/A", r.stock_health_status.upper(), r.inventory_value
        ])

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stocksense_inventory_report.csv"},
    )


@router.get("/sales/csv")
def export_sales_csv(user: CurrentUser = Depends(get_current_user)):
    """Export recent sales transactions as CSV."""
    records = list_sales(limit=2000)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Order ID", "Store", "Date", "Customer", "Channel", "Total Amount"])
    for r in records:
        writer.writerow([
            r.sale_id, r.store_name, r.sale_date, r.customer_name or "Walk-in", r.channel, r.total_amount
        ])

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stocksense_sales_report.csv"},
    )


@router.get("/purchases/csv")
def export_purchases_csv(user: CurrentUser = Depends(get_current_user)):
    """Export supplier purchase orders and fulfillment status as CSV."""
    with get_db() as conn:
        query = """
            SELECT 
                p.purchase_id,
                st.name as store_name,
                sup.name as supplier_name,
                p.order_date,
                p.expected_delivery_date,
                p.status,
                ROUND(COALESCE(SUM(pi.quantity_ordered * pi.unit_cost), 0.0), 2) as total_amount,
                COALESCE(SUM(pi.quantity_ordered), 0) as total_units_ordered,
                COALESCE(SUM(pi.quantity_received), 0) as total_units_received
            FROM purchases p
            JOIN stores st ON p.store_id = st.store_id
            JOIN suppliers sup ON p.supplier_id = sup.supplier_id
            LEFT JOIN purchase_items pi ON p.purchase_id = pi.purchase_id
            GROUP BY p.purchase_id
            ORDER BY p.order_date DESC
        """
        rows = fetch_all(conn, query)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "PO Number", "Store", "Supplier", "Order Date", "Expected Delivery Date",
        "Status", "Units Ordered", "Units Received", "Total Cost"
    ])
    for r in rows:
        writer.writerow([
            f"#PO-{str(r['purchase_id']).zfill(5)}",
            r["store_name"],
            r["supplier_name"],
            r["order_date"],
            r["expected_delivery_date"],
            r["status"].upper(),
            r["total_units_ordered"],
            r["total_units_received"],
            r["total_amount"],
        ])

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stocksense_purchases_report.csv"},
    )


@router.get("/dead-stock/csv")
def export_dead_stock_csv(user: CurrentUser = Depends(get_current_user)):
    """Export dormant and slow-moving inventory capital risk as CSV."""
    with get_db() as conn:
        query = """
            SELECT 
                st.name as store_name,
                p.sku,
                p.name as product_name,
                c.name as category_name,
                d.flagged_at,
                d.days_without_sale,
                d.quantity_at_risk,
                d.estimated_value_at_risk,
                d.recommendation,
                COALESCE(d.resolution_notes, '') as notes
            FROM dead_stock_flags d
            JOIN stores st ON d.store_id = st.store_id
            JOIN products p ON d.product_id = p.product_id
            JOIN categories c ON p.category_id = c.category_id
            ORDER BY d.estimated_value_at_risk DESC
        """
        rows = fetch_all(conn, query)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Store", "SKU", "Product Name", "Category", "Flagged Date",
        "Days Without Sale", "Units at Risk", "Value at Risk", "Recommended Action", "Notes"
    ])
    for r in rows:
        writer.writerow([
            r["store_name"],
            r["sku"],
            r["product_name"],
            r["category_name"],
            r["flagged_at"][:10] if r["flagged_at"] else "N/A",
            r["days_without_sale"],
            r["quantity_at_risk"],
            r["estimated_value_at_risk"],
            r["recommendation"].upper(),
            r["notes"],
        ])

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stocksense_dead_stock_report.csv"},
    )


@router.get("/forecast/csv")
def export_forecast_csv(user: CurrentUser = Depends(get_current_user)):
    """Export demand projections and safety stock parameters as CSV."""
    with get_db() as conn:
        query = """
            SELECT 
                st.name as store_name,
                p.sku,
                p.name as product_name,
                c.name as category_name,
                i.quantity_on_hand,
                ROUND(COALESCE(SUM(si.quantity), 0) / 30.0, 2) as avg_daily_demand,
                ROUND((COALESCE(SUM(si.quantity), 0) / 30.0) * 30.0, 1) as projected_30d_demand,
                MAX(5, CAST(ROUND((COALESCE(SUM(si.quantity), 0) / 30.0) * 7.0, 0) AS INT)) as recommended_safety_stock,
                'v1.0.0-xgb' as model_version
            FROM inventory i
            JOIN stores st ON i.store_id = st.store_id
            JOIN products p ON i.product_id = p.product_id
            JOIN categories c ON p.category_id = c.category_id
            LEFT JOIN sales s ON s.store_id = i.store_id AND s.sale_date >= date('now', '-30 days')
            LEFT JOIN sale_items si ON si.sale_id = s.sale_id AND si.product_id = i.product_id
            GROUP BY i.store_id, i.product_id
            ORDER BY st.name ASC, p.name ASC
        """
        rows = fetch_all(conn, query)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Store", "SKU", "Product Name", "Category", "Current Stock",
        "Avg Daily Demand", "30-Day Projected Demand", "Safety Stock Buffer", "Model Version"
    ])
    for r in rows:
        writer.writerow([
            r["store_name"],
            r["sku"],
            r["product_name"],
            r["category_name"],
            r["quantity_on_hand"],
            r["avg_daily_demand"],
            r["projected_30d_demand"],
            r["recommended_safety_stock"],
            r["model_version"],
        ])

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stocksense_demand_forecast_report.csv"},
    )


@router.get("/audit/csv")
def export_audit_csv(user: CurrentUser = Depends(get_current_user)):
    """Export system compliance audit log trail as CSV."""
    with get_db() as conn:
        query = """
            SELECT audit_id, occurred_at, event_type, entity_type, entity_id, actor, COALESCE(notes, '') as notes
            FROM audit_logs
            ORDER BY occurred_at DESC
            LIMIT 5000
        """
        rows = fetch_all(conn, query)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Audit ID", "Timestamp (UTC)", "Event Action", "Entity Type", "Entity ID", "Actor", "Notes"
    ])
    for r in rows:
        writer.writerow([
            f"#{r['audit_id']}",
            r["occurred_at"],
            r["event_type"],
            r["entity_type"],
            r["entity_id"],
            r["actor"],
            r["notes"],
        ])

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stocksense_audit_trail_report.csv"},
    )
