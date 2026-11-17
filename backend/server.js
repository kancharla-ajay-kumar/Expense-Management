const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const mongoSanitize = require('express-mongo-sanitize');
const mongoose = require('mongoose');

dotenv.config();

const connectDB = require('./config/db');
const { notFound, errorHandler } = require('./middleware/errorHandler');
const { apiLimiter } = require('./middleware/rateLimiter');

const authRoutes = require('./routes/authRoutes');
const expenseRoutes = require('./routes/expenseRoutes');
const budgetRoutes = require('./routes/budgetRoutes');
const metaRoutes = require('./routes/metaRoutes');

// Initiate database connection
connectDB();

const app = express();

// Trust reverse proxy (essential for Render, Vercel, and rate limiting)
app.set('trust proxy', 1);

// --- Security & parsing middleware ---
app.use(helmet());

const allowedOrigins = process.env.CLIENT_URL
  ? process.env.CLIENT_URL.split(',').map((u) => u.trim().replace(/\/$/, ''))
  : ['http://localhost:5173', 'http://localhost:3000'];

const isOriginAllowed = (origin) => {
  if (!origin) return true;
  const normalized = origin.replace(/\/$/, '');
  if (
    allowedOrigins.includes(normalized) ||
    normalized.endsWith('.vercel.app') ||
    normalized.includes('localhost') ||
    process.env.NODE_ENV !== 'production'
  ) {
    return true;
  }
  return true; // Allow client origins in production to prevent CORS blocks
};

app.use(
  cors({
    origin: (origin, callback) => callback(null, isOriginAllowed(origin)),
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With'],
  })
);
app.options('*', cors());

app.use(express.json({ limit: '10kb' }));
app.use(mongoSanitize());
app.use(apiLimiter);

if (process.env.NODE_ENV !== 'production') {
  app.use(morgan('dev'));
}

// --- Health and root status routes ---
app.get('/', (req, res) => {
  const state = mongoose.connection.readyState;
  const states = { 0: 'disconnected', 1: 'connected', 2: 'connecting', 3: 'disconnecting' };
  res.json({
    success: true,
    name: 'SpendWise API',
    status: 'running',
    database: states[state] || 'unknown',
  });
});

const handleHealth = (req, res) => {
  const state = mongoose.connection.readyState;
  const states = { 0: 'disconnected', 1: 'connected', 2: 'connecting', 3: 'disconnecting' };
  const isConnected = state === 1;

  res.status(isConnected ? 200 : 503).json({
    success: isConnected,
    status: isConnected ? 'healthy' : 'database_unavailable',
    database: {
      status: states[state] || 'unknown',
      connected: isConnected,
      host: mongoose.connection.host || null,
      name: mongoose.connection.name || null,
    },
    message: isConnected
      ? 'SpendWise API and Database are healthy'
      : 'Database connection is not ready. Please verify MongoDB Atlas IP whitelist (0.0.0.0/0).',
    timestamp: new Date().toISOString(),
    uptime: Math.floor(process.uptime()),
  });
};

app.get('/health', handleHealth);
app.get('/api/health', handleHealth);

// --- Database connection guard for functional API routes ---
app.use('/api', (req, res, next) => {
  if (req.path === '/health' || req.path === '/meta') return next();
  if (mongoose.connection.readyState !== 1) {
    return res.status(503).json({
      success: false,
      message:
        'Database connection is not ready. Please ensure MongoDB Atlas Network Access has IP 0.0.0.0/0 (Allow access from anywhere) whitelisted and MONGO_URI in Render is valid.',
    });
  }
  next();
});

// --- API Routes ---
app.use('/api/auth', authRoutes);
app.use('/api/expenses', expenseRoutes);
app.use('/api/budgets', budgetRoutes);
app.use('/api/meta', metaRoutes);

// --- Error handling (must be last) ---
app.use(notFound);
app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running in ${process.env.NODE_ENV || 'development'} mode on port ${PORT}`);
});
