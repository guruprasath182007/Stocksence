# STOCKSENSE — AI-Powered Inventory Intelligence & Demand Forecasting Platform

<p align="center">
  <img src="frontend/public/logo.png" alt="STOCKSENSE Logo" width="130" style="border-radius: 50%; border: 3px solid rgba(59, 130, 246, 0.4); box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.4);" />
</p>

<p align="center">
  <strong>Predict Demand. Prevent Stockouts. Make Smarter Inventory Decisions.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue.svg" alt="Version" />
  <img src="https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-brightgreen.svg" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688.svg" alt="FastAPI" />
  <img src="https://img.shields.io/badge/React-19.0-61DAFB.svg" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-5.7-3178C6.svg" alt="TypeScript" />
  <img src="https://img.shields.io/badge/TailwindCSS-v4.0-38B2AC.svg" alt="TailwindCSS" />
  <img src="https://img.shields.io/badge/Tests-29%2F29%20Passing-success.svg" alt="Tests" />
  <img src="https://img.shields.io/badge/License-Proprietary-orange.svg" alt="License" />
</p>

---

## 📋 Table of Contents
1. [STOCKSENSE Overview](#-stocksense-overview)
2. [Features](#-features)
3. [Technology Stack](#-technology-stack)
4. [Project Architecture](#-project-architecture)
5. [Frontend Setup](#-frontend-setup)
6. [Backend Setup](#-backend-setup)
7. [Database Setup](#-database-setup)
8. [Machine Learning (ML) Setup](#-machine-learning-ml-setup)
9. [Environment Variables](#-environment-variables)
10. [How to Run Locally](#-how-to-run-locally)
11. [How to Test](#-how-to-test)
12. [Deployment Instructions](#-deployment-instructions)
13. [Demo Credentials](#-demo-credentials)

---

## 🎯 STOCKSENSE Overview

**STOCKSENSE** is a commercial-grade, multi-store inventory intelligence and demand forecasting SaaS platform designed for retailers, supermarket chains, wholesalers, and multi-location enterprises.

Traditional inventory management systems are static and reactive—alerting managers only after an item has already run out of stock or capital has been tied up in unsellable dead inventory. STOCKSENSE bridges the gap between enterprise transactional integrity and predictive machine learning to answer critical operational questions:
- *What stock will I need over the next 7, 14, and 30 days?*
- *When should I reorder, and in what exact quantity (EOQ)?*
- *Which store locations require immediate stock redistribution?*
- *What happens to my margins and safety buffers if demand surges or supplier lead times increase?*

---

## ✨ Features

- **Executive Intelligence Dashboard**: Real-time KPI summary (Inventory Valuation, Daily Revenue, Estimated Profits, Low Stock Alerts, Stockout Risks, Dead Stock), interactive Recharts revenue/profit analytics, and actionable algorithmic insights.
- **Multi-Store Inventory Management**: Location-filtered stock tracking with health indicators (*Healthy*, *Low Stock*, *Critical*, *Overstock*, *Dead Stock*), inter-store transfers with automatic double-entry auditing, and cycle-count stock adjustments.
- **Products Catalog & Gross Margin Analysis**: SKU catalog management, categories, units of measure, wholesale costs, retail pricing, and automated gross profit margin calculations.
- **Point of Sale (POS) & Checkout**: Instant counter sales, multi-channel checkout (*In-Store*, *Online*, *Wholesale*), and real-time inventory validation that strictly prevents negative stock.
- **Purchase Orders & Automated Replenishment**: Vendor lead-time tracking, purchase order creation, and one-click stock receiving that atomically updates store-level inventory.
- **AI Demand Forecasting Studio**: Time-series demand forecasting with walk-forward validation (zero forward data leakage), configurable 7/14/30-day horizons, and 95% empirical confidence intervals.
- **Smart Decisions Engine**:
  - *Automated Reorder Recommendations*: Calculates Economic Order Quantity (EOQ), Minimum Order Quantity (MOQ), and dynamic safety stock.
  - *Stockout Radar*: Proactively flags SKUs whose days of coverage fall below vendor lead time.
  - *Constrained Multi-Store Allocation*: Fair-share proportional inventory distribution when central supply is constrained.
  - *What-If Scenario Simulator*: Risk-free sandbox to simulate demand spikes (+/-100%), delivery delays, and price sensitivity with zero database mutations.
- **Enterprise CSV Reports Center**: Instant export of Valuation Reports, Sales Ledgers, Purchase Orders, Dead Stock Analysis, and Audit Trail history.
- **Role-Based Access Control (RBAC)**: Secure separation between `admin` (full configuration, model retraining, system health) and `staff` (day-to-day POS and inventory operations).

---

## 🛠 Technology Stack

### Backend & API
- **Language**: Python 3.11+
- **Web Framework**: FastAPI (Asynchronous REST API)
- **ASGI Server**: Uvicorn
- **Data Validation & Settings**: Pydantic v2
- **Authentication & Security**: PyJWT (HMAC-SHA256), bcrypt (password hashing)
- **Data Processing**: Pandas, NumPy

### Machine Learning
- **Libraries**: Scikit-Learn, XGBoost, Joblib
- **Models**: Random Forest Regressor, Gradient Boosting Regressor, XGBoost Regressor
- **Validation**: Chronological time-series walk-forward split (train/validation)
- **Metrics**: RMSE, MAE, R², MAPE, Empirical Prediction Intervals

### Frontend
- **Framework**: React 19 + TypeScript 5.7
- **Build Tool**: Vite
- **Styling**: Tailwind CSS (v4)
- **Icons**: Lucide React
- **Data Visualization**: Recharts
- **HTTP Client**: Axios with automatic JWT bearer interceptors

### Database
- **Primary / Default**: SQLite 3 with Write-Ahead Logging (WAL) and enforced foreign keys
- **Migrations**: Versioned raw SQL migration runner (`0001` through `0019`)
- **Compatibility**: SQLAlchemy/PostgreSQL ready architecture

---

## 🏛 Project Architecture

```
STOCKSENSE
│
├── frontend/                     # React + TypeScript + Vite + Tailwind CSS
│   ├── src/
│   │   ├── components/           # UI components (Sidebar, Navbar, StatCard, Badge, Modal)
│   │   ├── context/              # AuthContext (JWT session management, RBAC)
│   │   ├── pages/                # Application views (Dashboard, Inventory, POS Sales,
│   │   │                         # Purchases, Forecasting, Smart Decisions, Reports, Admin)
│   │   ├── services/             # Axios API client with token interceptor
│   │   └── types/                # Domain TypeScript interfaces
│   ├── public/                   # Static assets & official STOCKSENSE circular logo
│   └── package.json
│
├── backend/                      # FastAPI REST Backend
│   ├── api/                      # Route controllers (auth, dashboard, inventory, products,
│   │                             # sales, purchases, forecast, smart_decisions, reports, admin)
│   ├── auth/                     # Bcrypt hashing & PyJWT token management
│   ├── database.py               # Database connection lifecycle & pooling
│   ├── schemas/                  # Pydantic request/response schemas
│   ├── services/                 # Business logic engines (forecasting, EOQ, inventory, sales)
│   ├── seed_data.py              # 24-month multi-store historical sales generator
│   ├── config.py                 # Application settings from environment variables
│   └── main.py                   # FastAPI application entrypoint
│
├── smartstock/db/                # Database Foundation
│   ├── migrations/               # 19 incremental SQL migration files (0001 to 0019)
│   ├── connection.py             # WAL mode, foreign key enforcement, thread-safe access
│   ├── operations.py             # CRUD helper functions with parameter binding
│   └── schema.py                 # Migration runner and version registry
│
├── models/                       # ML Model Storage (tracked via .gitkeep)
├── data/                         # SQLite database storage directory (smartstock.db)
├── tests/                        # Automated Test Suite (29 tests)
│   ├── db/                       # Database schema, foreign key & constraint tests (19 tests)
│   └── test_backend_services.py  # Full-stack service verification tests (10 tests)
│
├── run.py                        # Cross-platform unified launcher (starts backend + frontend)
├── start.bat                     # Windows one-click double-click launcher
├── requirements.txt              # Python production dependencies
├── .env.example                  # Environment configuration template
└── .gitignore                    # Git exclusion rules
```

---

## 🎨 Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment (optional)**:
   By default, the Vite dev server proxies requests to `http://localhost:8000/api`. If you need to customize the backend URL, create a `.env` file in the `frontend` folder:
   ```env
   VITE_API_BASE_URL=http://localhost:8000/api
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```
   The frontend will be available at: **http://localhost:5173**

5. **Build for production**:
   ```bash
   npm run build
   ```

---

## ⚙️ Backend Setup

1. **Ensure Python 3.11+ is installed**:
   ```bash
   python --version
   ```

2. **Create and activate a virtual environment**:
   - **Windows (Command Prompt / PowerShell)**:
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment file**:
   ```bash
   # Copy template
   cp .env.example .env
   ```

5. **Start the FastAPI server**:
   ```bash
   python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```
   Interactive Swagger API Documentation will be available at: **http://127.0.0.1:8000/docs**

---

## 🗄 Database Setup

STOCKSENSE uses an enterprise SQLite architecture out of the box with zero external database configuration required.

### 1. Automatic Schema Migration & Seeding
When the backend starts, it automatically:
- Executes all 19 versioned SQL migrations in `smartstock/db/migrations/` sequentially.
- Enables SQLite Write-Ahead Logging (`PRAGMA journal_mode = WAL;`) for concurrent read/write throughput.
- Enforces strict foreign key integrity (`PRAGMA foreign_keys = ON;`).
- Runs `backend/seed_data.py` to populate 105 commercial products, 4 store locations, suppliers, initial inventory, and 24 months of realistic sales transactions if empty.

### 2. Manual Migration Validation
To inspect database integrity manually:
```bash
python validate_db.py
```

### 3. Production PostgreSQL Setup (Optional)
To switch to PostgreSQL in cloud deployments, configure the `DATABASE_URL` environment variable:
```env
DATABASE_URL=postgresql://stocksense_user:your_password@localhost:5432/stocksense_db
```

---

## 🤖 Machine Learning (ML) Setup

STOCKSENSE features an integrated demand forecasting pipeline that operates on chronological sales data:

### Feature Engineering Pipeline
The time-series engine automatically extracts:
- **Calendar Signals**: Day of week, month, weekend indicators, day of year.
- **Lag Features**: Demand at $t-1$, $t-7$, $t-14$, and $t-28$ days.
- **Rolling Statistics**: 7-day and 28-day rolling moving averages and standard deviations.

### Model Candidates & Walk-Forward Validation
1. **Random Forest Regressor** (ensemble averaging)
2. **Gradient Boosting Regressor** (gradient descent on residuals)
3. **XGBoost Regressor** (extreme gradient boosting)

Evaluation uses a strictly chronological 80/20 train-test split (preventing lookahead bias). The model with the lowest Root Mean Squared Error (RMSE) is automatically selected, registered in the `ml_model_registry` table, and serialized to `models/`.

### Retraining via Admin Dashboard or API
- **Web UI**: Navigate to **Admin** -> **Model Center** and click **Retrain Production Model**.
- **REST API**:
  ```bash
  POST /api/forecast/retrain
  Authorization: Bearer <ADMIN_JWT_TOKEN>
  ```

---

## 🔐 Environment Variables

Copy `.env.example` to `.env` to customize settings:

| Variable | Description | Default | Required for Production |
| :--- | :--- | :--- | :--- |
| `ENVIRONMENT` | Runtime environment (`development`, `staging`, `production`) | `development` | Yes |
| `SECRET_KEY` / `STOCKSENSE_SECRET_KEY` | Secret key used to sign JWT authentication tokens | *Auto-fallback* | **Yes (Generate 32+ char key)** |
| `ALGORITHM` | JWT signing algorithm | `HS256` | No |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Session validity duration in minutes | `1440` (24h) | No |
| `DATABASE_PATH` / `SMARTSTOCK_DB_PATH` | Path to local SQLite database file | `data/smartstock.db` | No |
| `DATABASE_URL` | Optional PostgreSQL connection string | *None* | For Cloud/PostgreSQL |
| `CORS_ORIGINS` | Comma-separated list of allowed frontend origins | `http://localhost:5173,...` | **Yes (Match frontend domain)** |
| `HOST` | Backend server host address | `127.0.0.1` | No |
| `PORT` | Backend server port | `8000` | No |

---

## 🚀 How to Run Locally

### Option A: Unified Launcher (Recommended)
STOCKSENSE provides cross-platform launchers that boot both backend and frontend simultaneously:

- **Python Launcher (Windows, macOS, Linux)**:
  ```bash
  python run.py
  ```
- **Windows Double-Click Launcher**:
  Double-click `start.bat` in the project root.

The launcher runs the FastAPI server at `http://localhost:8000` and the React frontend at `http://localhost:5173`.

### Option B: Separate Terminals

**Terminal 1 — Backend**:
```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

**Terminal 2 — Frontend**:
```bash
cd frontend
npm run dev
```

Open your browser at: **http://localhost:5173**

---

## 🧪 How to Test

STOCKSENSE contains a 29-test automated test suite covering database constraints, foreign keys, schema migrations, and full-stack business logic.

### 1. Run Database Unit Tests (19 tests)
```bash
pytest tests/db/
```
Validates:
- SQLite connection pooling, WAL mode, and PRAGMA settings.
- NOT NULL, CHECK, UNIQUE, and FOREIGN KEY constraints across all 19 migration tables.
- Transaction rollback safety.

### 2. Run Full-Stack Backend Service Tests (10 tests)
```bash
python -m unittest tests.test_backend_services
```
Validates:
- JWT authentication and bcrypt password verification.
- Product catalog and margin calculations.
- Multi-store inventory transfers with ledger balancing.
- POS sale processing with negative stock prevention.
- Purchase order creation and atomic stock replenishment.
- ML time-series feature engineering and walk-forward prediction.
- Smart reorder calculation (EOQ/MOQ) and store allocation.
- What-If simulator zero database mutation guarantee.
- System health diagnostics and audit trail completeness.

### 3. Run Frontend Type Checking & Production Build
```bash
cd frontend
npm run build
```

---

## 🚢 Deployment Instructions

### 1. Docker / Container Deployment
Create a `Dockerfile` for the backend:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY smartstock/ ./smartstock/
COPY data/ ./data/
COPY models/ ./models/

EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. Frontend Production Deployment
Build the static bundle:
```bash
cd frontend
npm run build
```
Deploy the generated `frontend/dist/` directory to static hosting services such as:
- **Vercel** / **Netlify** / **Cloudflare Pages**
- **AWS S3 + CloudFront**
- **Nginx Web Server**

### 3. Nginx Reverse Proxy Example Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Frontend static files
    location / {
        root /var/www/stocksense/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # Backend API proxy
    location /api/ {
        proxy_pass http://127.0.0.1:8000/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 4. Production Security Checklist
- Set a strong, random `SECRET_KEY` in environment variables (`openssl rand -hex 32`).
- Update `CORS_ORIGINS` to only permit your production domain.
- Enforce HTTPS across all endpoints.
- Change default admin credentials upon first login.

---

## 🔑 Demo Credentials

STOCKSENSE comes pre-seeded with ready-to-test demo accounts:

| Role | Username | Password | Permitted Actions |
| :--- | :--- | :--- | :--- |
| **Administrator** | `admin` | `Admin@123` | Full access: All modules, ML model retraining, system health diagnostics, audit logs |
| **Staff Member** | `staff` | `Staff@123` | Operational access: POS checkout, inventory adjustments, purchase orders, forecast viewing |

---

## 📄 License

Proprietary enterprise SaaS codebase developed for commercial inventory intelligence. All rights reserved.
