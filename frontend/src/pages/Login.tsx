import React, { useState } from 'react';
import { ArrowRight, Lock, User as UserIcon, ShieldAlert } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export const Login: React.FC = () => {
  const { login } = useAuth();
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('Admin@123');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      await login(username, password);
    } catch (err: any) {
      setError(err.message || 'Failed to authenticate');
    } finally {
      setLoading(false);
    }
  };

  const fillCredentials = (u: string, p: string) => {
    setUsername(u);
    setPassword(p);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50/40 to-indigo-50/50 flex flex-col justify-center items-center p-6 relative overflow-hidden">
      {/* Background radiant ambient glow accents */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/3 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="w-full max-w-md z-10">
        {/* Brand identity with official circular logo */}
        <div className="text-center mb-8">
          <div className="inline-flex p-1.5 rounded-full bg-white border-2 border-blue-500/40 shadow-xl shadow-blue-500/15 mb-4 hover:border-blue-500 transition">
            <img
              src="/logo.png"
              alt="STOCKSENSE Official Logo"
              className="w-20 h-20 object-cover rounded-full shadow-inner"
            />
          </div>
          <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 font-mono">
            STOCKSENSE
          </h1>
          <p className="mt-2 text-sm text-slate-600 font-medium">
            Predict Demand. Prevent Stockouts. Make Smarter Decisions.
          </p>
        </div>

        {/* Login Card */}
        <div className="bg-white border border-slate-200/90 rounded-2xl p-8 shadow-xl shadow-slate-200/60">
          {error && (
            <div className="mb-5 p-3 rounded-lg bg-rose-50 border border-rose-200 text-rose-700 text-xs font-semibold flex items-center space-x-2">
              <ShieldAlert className="w-4 h-4 shrink-0 text-rose-600" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                Username
              </label>
              <div className="relative">
                <UserIcon className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="Enter username"
                  className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-300 rounded-lg text-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:bg-white focus:border-blue-600 focus:ring-2 focus:ring-blue-500/20 shadow-2xs transition"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                Password
              </label>
              <div className="relative">
                <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter password"
                  className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-300 rounded-lg text-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:bg-white focus:border-blue-600 focus:ring-2 focus:ring-blue-500/20 shadow-2xs transition"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-2 flex items-center justify-center space-x-2 py-2.5 px-4 bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm rounded-lg shadow-md shadow-blue-500/25 transition disabled:opacity-50 cursor-pointer"
            >
              <span>{loading ? 'Authenticating...' : 'Sign In to Workspace'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </form>

          {/* Quick Demo Access Credentials */}
          <div className="mt-6 pt-5 border-t border-slate-100">
            <span className="block text-center text-xs font-bold text-slate-500 uppercase tracking-wider mb-3">
              Quick Demo Access
            </span>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => fillCredentials('admin', 'Admin@123')}
                className="p-2.5 rounded-lg bg-slate-50 hover:bg-blue-50/80 border border-slate-200 hover:border-blue-300 text-left transition cursor-pointer group"
              >
                <div className="text-xs font-bold text-slate-900 group-hover:text-blue-600">Admin Account</div>
                <div className="text-[10px] text-slate-500 font-mono mt-0.5">admin / Admin@123</div>
              </button>
              <button
                type="button"
                onClick={() => fillCredentials('staff', 'Staff@123')}
                className="p-2.5 rounded-lg bg-slate-50 hover:bg-emerald-50/80 border border-slate-200 hover:border-emerald-300 text-left transition cursor-pointer group"
              >
                <div className="text-xs font-bold text-slate-900 group-hover:text-emerald-600">Staff Account</div>
                <div className="text-[10px] text-slate-500 font-mono mt-0.5">staff / Staff@123</div>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
