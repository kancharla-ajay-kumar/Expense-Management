import axios from 'axios';

const getBaseURL = () => {
  const envUrl = import.meta.env.VITE_API_URL;
  if (envUrl) {
    return envUrl.endsWith('/api') ? envUrl : `${envUrl.replace(/\/$/, '')}/api`;
  }
  // If deployed on Vercel or any remote origin without build-time VITE_API_URL, default to live Render backend
  if (
    typeof window !== 'undefined' &&
    window.location.hostname !== 'localhost' &&
    window.location.hostname !== '127.0.0.1'
  ) {
    return 'https://expense-management-xswk.onrender.com/api';
  }
  return '/api';
};

const api = axios.create({
  baseURL: getBaseURL(),
  headers: { 'Content-Type': 'application/json' },
});

// Attach the JWT to every outgoing request, if we have one
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('spendwise-token') || localStorage.getItem('ledgerly-token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Centralized 401 handling: bounce the user back to login and clear any stale credentials
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401 && !error.config?.url?.includes('/auth/login')) {
      localStorage.removeItem('spendwise-token');
      localStorage.removeItem('spendwise-user');
      localStorage.removeItem('ledgerly-token');
      localStorage.removeItem('ledgerly-user');
      if (!window.location.pathname.startsWith('/login')) {
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export default api;
