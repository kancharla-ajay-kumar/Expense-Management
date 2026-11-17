import { createContext, useContext, useState, useEffect, useCallback } from 'react';
import api from '../api/axios';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    try {
      const saved = localStorage.getItem('spendwise-user') || localStorage.getItem('ledgerly-user');
      if (!saved || saved === 'undefined' || saved === 'null') return null;
      return JSON.parse(saved);
    } catch {
      localStorage.removeItem('spendwise-user');
      localStorage.removeItem('ledgerly-user');
      return null;
    }
  });
  const [token, setToken] = useState(() => {
    const t = localStorage.getItem('spendwise-token') || localStorage.getItem('ledgerly-token');
    if (!t || t === 'undefined' || t === 'null') return null;
    return t;
  });
  const [loading, setLoading] = useState(true);

  // On mount, if we have a token, verify it and refresh the user profile.
  useEffect(() => {
    const verify = async () => {
      if (!token) {
        setLoading(false);
        return;
      }
      try {
        const { data } = await api.get('/auth/me');
        setUser(data.user);
        localStorage.setItem('spendwise-user', JSON.stringify(data.user));
      } catch {
        setToken(null);
        setUser(null);
        localStorage.removeItem('spendwise-token');
        localStorage.removeItem('spendwise-user');
        localStorage.removeItem('ledgerly-token');
        localStorage.removeItem('ledgerly-user');
      } finally {
        setLoading(false);
      }
    };
    verify();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const persistSession = (newToken, newUser) => {
    localStorage.setItem('spendwise-token', newToken);
    localStorage.setItem('spendwise-user', JSON.stringify(newUser));
    setToken(newToken);
    setUser(newUser);
  };

  const login = async (email, password) => {
    const { data } = await api.post('/auth/login', { email, password });
    persistSession(data.token, data.user);
    return data.user;
  };

  const register = async (payload) => {
    const { data } = await api.post('/auth/register', payload);
    persistSession(data.token, data.user);
    return data.user;
  };

  const logout = useCallback(() => {
    localStorage.removeItem('spendwise-token');
    localStorage.removeItem('spendwise-user');
    localStorage.removeItem('ledgerly-token');
    localStorage.removeItem('ledgerly-user');
    setToken(null);
    setUser(null);
  }, []);

  const updateUser = (updatedUser) => {
    setUser(updatedUser);
    localStorage.setItem('spendwise-user', JSON.stringify(updatedUser));
  };

  return (
    <AuthContext.Provider
      value={{ user, token, loading, login, register, logout, updateUser, isAuthenticated: !!token }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within an AuthProvider');
  return ctx;
};
