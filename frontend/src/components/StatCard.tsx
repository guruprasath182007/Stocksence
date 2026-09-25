import React from 'react';

interface StatCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon?: React.ReactNode;
  trend?: {
    value: string;
    isPositive: boolean;
  };
  accentColor?: 'blue' | 'emerald' | 'amber' | 'rose' | 'purple';
}

export const StatCard: React.FC<StatCardProps> = ({
  title,
  value,
  subtitle,
  icon,
  trend,
  accentColor = 'blue',
}) => {
  const accentBorders = {
    blue: 'hover:border-blue-400',
    emerald: 'hover:border-emerald-400',
    amber: 'hover:border-amber-400',
    rose: 'hover:border-rose-400',
    purple: 'hover:border-purple-400',
  };

  const iconColors = {
    blue: 'text-blue-600 bg-blue-50 border-blue-200',
    emerald: 'text-emerald-600 bg-emerald-50 border-emerald-200',
    amber: 'text-amber-600 bg-amber-50 border-amber-200',
    rose: 'text-rose-600 bg-rose-50 border-rose-200',
    purple: 'text-purple-600 bg-purple-50 border-purple-200',
  };

  return (
    <div
      className={`bg-white border border-slate-200/90 rounded-xl p-5 shadow-sm hover:shadow-md transition-all duration-200 ${accentBorders[accentColor]}`}
    >
      <div className="flex items-center justify-between">
        <span className="text-xs font-bold text-slate-500 uppercase tracking-wider">
          {title}
        </span>
        {icon && (
          <div className={`p-2 rounded-lg border text-sm ${iconColors[accentColor]}`}>
            {icon}
          </div>
        )}
      </div>

      <div className="mt-3 flex items-baseline justify-between">
        <h3 className="text-2xl font-extrabold tracking-tight text-slate-900">{value}</h3>
        {trend && (
          <span
            className={`text-xs font-bold px-2 py-0.5 rounded-full ${
              trend.isPositive ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-rose-50 text-rose-700 border border-rose-200'
            }`}
          >
            {trend.value}
          </span>
        )}
      </div>

      {subtitle && <p className="mt-1 text-xs text-slate-500 font-medium">{subtitle}</p>}
    </div>
  );
};
