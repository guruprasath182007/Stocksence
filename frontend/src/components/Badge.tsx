import React from 'react';

interface BadgeProps {
  status: string;
  size?: 'sm' | 'md';
}

export const Badge: React.FC<BadgeProps> = ({ status, size = 'md' }) => {
  const s = status.toLowerCase();

  let styles = 'bg-slate-100 text-slate-700 border-slate-200';

  if (s === 'critical' || s === 'out of stock' || s === 'write-off') {
    styles = 'bg-rose-50 text-rose-700 border-rose-200';
  } else if (s === 'low' || s === 'low stock' || s === 'discount' || s === 'submitted') {
    styles = 'bg-amber-50 text-amber-700 border-amber-200';
  } else if (s === 'healthy' || s === 'normal' || s === 'received' || s === 'completed') {
    styles = 'bg-emerald-50 text-emerald-700 border-emerald-200';
  } else if (s === 'overstock' || s === 'markdown') {
    styles = 'bg-blue-50 text-blue-700 border-blue-200';
  } else if (s === 'dead_stock' || s === 'dead stock') {
    styles = 'bg-purple-50 text-purple-700 border-purple-200';
  } else if (s === 'draft') {
    styles = 'bg-slate-100 text-slate-700 border-slate-200';
  }

  const sizeClasses = size === 'sm' ? 'px-2 py-0.5 text-[10px]' : 'px-2.5 py-1 text-xs';

  return (
    <span
      className={`inline-flex items-center font-bold rounded-full border capitalize tracking-wide shadow-2xs ${sizeClasses} ${styles}`}
    >
      <span className="w-1.5 h-1.5 rounded-full bg-current mr-1.5 opacity-90" />
      {status.replace(/_/g, ' ')}
    </span>
  );
};
