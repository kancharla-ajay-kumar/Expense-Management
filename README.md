# SpendWise — Personal Finance and Expense Management System

A full-stack modern personal finance and expense management application built with the **MERN Stack (MongoDB, Express.js, React, Node.js)**. SpendWise empowers users to manage their income and expenses, monitor monthly budgets with proactive alerts, visualize financial patterns through interactive analytics, and track their savings in multiple currencies.

Developed and customized by **[Kancharla Ajay Kumar](https://github.com/kancharla-ajay-kumar)** as a practical MERN stack demonstration project, based on the open-source foundation by **[daniyalnova](https://github.com/daniyalnova/Expense-Management)**.

---

## ✨ Features

- **Secure Authentication**: User registration and login powered by JSON Web Tokens (JWT) and `bcryptjs` password hashing, backed by client and server-side validation.
- **Income & Expense Tracking**: Full CRUD management of financial transactions categorized across groceries, utilities, rent, dining, freelance, salary, and more.
- **Interactive Visual Analytics**: Dashboard visualizations powered by Recharts and MongoDB aggregation pipelines:
  - Monthly Income vs. Expense bar comparisons
  - Category breakdown pie chart
  - 12-month net savings trend area chart
- **Smart Monthly Budgets**: Category-level budgets with spend tracking and dynamic 3-tier status alerts (On Track, Approaching Limit, Over Budget).
- **Data Export**: Instant one-click CSV export of transaction records.
- **Multi-Currency Support**: Native currency formatting for USD, EUR, GBP, INR, CAD, AUD, JPY, and PKR using the `Intl` API.
- **Responsive & Themed UI**: Designed with Tailwind CSS, supporting seamless light and dark mode toggling with zero flash-of-unstyled-content.
- **Robust Security**: Protected with `helmet` security headers, `express-rate-limit` brute-force protection, MongoDB query sanitization (`express-mongo-sanitize`), and user-isolated database queries.

---

## 🧱 Architecture & Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, Vite, React Router v6, Tailwind CSS, Recharts, React Hook Form, Axios, Lucide Icons, React Toastify |
| **Backend** | Node.js, Express.js, Mongoose, Express Validator, Express Async Handler |
| **Database** | MongoDB Atlas (Cloud) / Local MongoDB |
| **Authentication** | JWT (jsonwebtoken) & bcryptjs |
| **Security** | Helmet, Express Rate Limit, Express Mongo Sanitize, CORS |

```
SpendWise/
├── backend/
│   ├── config/db.js              # MongoDB Atlas connection handler
│   ├── controllers/              # Route controllers (auth, expenses, budgets)
│   ├── middleware/               # JWT auth guard, validators, rate limiters, error handling
│   ├── models/                   # Mongoose schemas: User, Expense, Budget
│   ├── routes/                   # API routes: /api/auth, /api/expenses, /api/budgets, /api/meta
│   ├── utils/                    # JWT generator, constants, demo seed script
│   └── server.js                 # Express server entry point
├── frontend/
│   ├── public/                   # Favicon and PWA manifest
│   ├── src/
│   │   ├── api/axios.js          # Centralized Axios client with JWT interceptor
│   │   ├── components/           # UI components, layout, dashboard widgets, modal forms
│   │   ├── context/              # AuthContext, ThemeContext, DataContext
│   │   ├── pages/                # Dashboard, Expenses, Budget, Profile, Login, Register, NotFound
│   │   └── utils/helpers.js      # Formatting helpers, color palettes, error parsers
│   ├── vercel.json               # SPA routing rewrite configuration for Vercel
│   └── vite.config.js            # Vite build and development proxy configuration
```

---

## 🔐 Environment Variables

### Backend (`backend/.env`)

| Variable | Description | Example / Default |
|---|---|---|
| `MONGO_URI` | MongoDB Atlas or local connection string | `mongodb+srv://<user>:<password>@cluster.mongodb.net/spendwise` |
| `JWT_SECRET` | Strong random secret key for signing JWTs | Generated random 64-character string |
| `JWT_EXPIRES_IN` | Token expiration period | `7d` |
| `CLIENT_URL` | Allowed frontend URL(s) for CORS | `http://localhost:5173` or deployed Vercel URL |
| `PORT` | Backend server port | `5000` (auto-assigned on Render) |
| `NODE_ENV` | Environment mode | `development` or `production` |

### Frontend (`frontend/.env`)

| Variable | Description | Example / Default |
|---|---|---|
| `VITE_API_URL` | Base API URL pointing to the backend | `/api` (local proxy) or `https://<render-app>.onrender.com/api` |

---

## 🚀 Local Development Setup

### Prerequisites
- Node.js (v18+)
- MongoDB Atlas account or local MongoDB instance

### 1. Backend Setup
```bash
cd backend
npm install
cp .env.example .env
# Edit .env with your MONGO_URI and JWT_SECRET
npm run dev        # Starts server on http://localhost:5000 with nodemon
```

Optional demo data seeding:
```bash
npm run seed       # Populates sample demo account: demo@spendwise.app / Demo1234
```

### 2. Frontend Setup
```bash
cd ../frontend
npm install
npm run dev        # Starts Vite dev server on http://localhost:5173
```

---

## 🔌 REST API Endpoints

All endpoints are prefixed with `/api`. Protected routes require `Authorization: Bearer <token>`.

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/health` | Public | Service health check |
| `POST` | `/auth/register` | Public | Register new user account |
| `POST` | `/auth/login` | Public | Authenticate user & issue JWT |
| `GET` | `/auth/me` | Private | Retrieve current user profile |
| `PUT` | `/auth/profile` | Private | Update user details & currency preferences |
| `PUT` | `/auth/password` | Private | Change user password |
| `GET` | `/expenses` | Private | Query transactions with pagination, filters & search |
| `POST` | `/expenses` | Private | Create transaction (income or expense) |
| `GET` | `/expenses/:id` | Private | Get single transaction |
| `PUT` | `/expenses/:id` | Private | Update transaction |
| `DELETE` | `/expenses/:id` | Private | Remove transaction |
| `GET` | `/expenses/stats` | Private | Aggregate dashboard analytics & 12-month trend |
| `GET` | `/expenses/export` | Private | Export all transactions to CSV file |
| `GET` | `/budgets` | Private | Retrieve monthly budgets with current spend |
| `POST` | `/budgets` | Private | Set or update category budget |
| `DELETE` | `/budgets/:id` | Private | Delete category budget |
| `GET` | `/meta` | Public/Auth | Category enums, payment methods & currency options |

---

## 🌐 Production Deployment

### Backend on Render
1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository: `https://github.com/kancharla-ajay-kumar/Expense-Management`.
3. Configure settings:
   - **Root Directory**: `backend`
   - **Build Command**: `npm install`
   - **Start Command**: `npm start`
4. Set Environment Variables:
   - `MONGO_URI`: Your MongoDB Atlas connection URI
   - `JWT_SECRET`: Random 32+ character string
   - `NODE_ENV`: `production`
   - `CLIENT_URL`: Your Vercel frontend URL
5. Deploy and note your Render Web Service URL.

### Frontend on Vercel
1. Import the repository on [Vercel](https://vercel.com/).
2. Configure settings:
   - **Root Directory**: `frontend`
   - **Framework Preset**: `Vite`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
3. Set Environment Variable:
   - `VITE_API_URL`: Your Render backend URL (e.g., `https://spendwise-api.onrender.com/api`)
4. Deploy and note your live Vercel domain.

---

## 📄 License & Attribution

- **Original Project**: [Expense-Management](https://github.com/daniyalnova/Expense-Management) by [daniyalnova](https://github.com/daniyalnova).
- **Customizations & Maintenance**: [Kancharla Ajay Kumar](https://github.com/kancharla-ajay-kumar).
- **License**: Released under the [MIT License](LICENSE).
