const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const mongoSanitize = require('express-mongo-sanitize');

dotenv.config();

const connectDB = require('./config/db');
const { notFound, errorHandler } = require('./middleware/errorHandler');
const { apiLimiter } = require('./middleware/rateLimiter');

const authRoutes = require('./routes/authRoutes');
const expenseRoutes = require('./routes/expenseRoutes');
const budgetRoutes = require('./routes/budgetRoutes');
const metaRoutes = require('./routes/metaRoutes');

connectDB();

const app = express();

// --- Security & parsing middleware ---
app.use(helmet());

const allowedOrigins = process.env.CLIENT_URL
  ? process.env.CLIENT_URL.split(',').map((u) => u.trim().replace(/\/$/, ''))
  : ['http://localhost:5173', 'http://localhost:3000'];

app.use(
  cors({
    origin: (origin, callback) => {
      if (!origin) return callback(null, true);
      const normalized = origin.replace(/\/$/, '');
      if (
        allowedOrigins.includes(normalized) ||
        process.env.NODE_ENV !== 'production' ||
        normalized.endsWith('.vercel.app')
      ) {
        return callback(null, true);
      }
      return callback(null, true);
    },
    credentials: true,
  })
);

app.use(express.json({ limit: '10kb' }));
app.use(mongoSanitize());
app.use(apiLimiter);

if (process.env.NODE_ENV !== 'production') {
  app.use(morgan('dev'));
}

// --- Health and root status routes ---
app.get('/', (req, res) => res.json({ success: true, name: 'SpendWise API', status: 'running' }));
app.get('/health', (req, res) => res.json({ success: true, message: 'SpendWise API is healthy' }));
app.get('/api/health', (req, res) => res.json({ success: true, message: 'SpendWise API is healthy' }));

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
