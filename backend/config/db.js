const mongoose = require('mongoose');

let isConnecting = false;

const connectDB = async () => {
  if (mongoose.connection.readyState === 1) {
    return;
  }
  if (isConnecting) {
    return;
  }

  let rawUri = process.env.MONGO_URI;

  if (!rawUri) {
    console.error('MongoDB connection error: MONGO_URI environment variable is not defined.');
    return;
  }

  // Clean and sanitize the connection string (remove accidental quotes, spaces, prefix, or placeholder brackets)
  let mongoUri = rawUri.trim();
  if (
    (mongoUri.startsWith('"') && mongoUri.endsWith('"')) ||
    (mongoUri.startsWith("'") && mongoUri.endsWith("'"))
  ) {
    mongoUri = mongoUri.slice(1, -1).trim();
  }
  if (mongoUri.startsWith('MONGO_URI=')) {
    mongoUri = mongoUri.replace(/^MONGO_URI=/, '').trim();
  }

  // Automatically remove accidental < and > placeholder brackets (e.g. <username>:<password>)
  mongoUri = mongoUri.replace(/[<>]/g, '').trim();

  const maskedUri = mongoUri.replace(/:([^@]+)@/, ':****@');
  console.log(`Connecting to MongoDB: ${maskedUri}`);

  isConnecting = true;
  try {
    const conn = await mongoose.connect(mongoUri, {
      serverSelectionTimeoutMS: 5000,
      socketTimeoutMS: 45000,
    });
    console.log(`MongoDB connected successfully: ${conn.connection.host}`);
    isConnecting = false;
  } catch (error) {
    isConnecting = false;
    console.error(`MongoDB connection error: ${error.message}`);
    console.error(
      '-> TROUBLESHOOTING CHECKLIST:\n' +
      '   1. Network Access: Ensure IP 0.0.0.0/0 (anywhere) is Active in MongoDB Atlas Network Access.\n' +
      '   2. Database Access: Confirm database user exists, has readWrite role, and correct password.\n' +
      '   3. Connection String: Check MONGO_URI in Render environment variables.'
    );
    // Retry connection after 5 seconds instead of crashing the server process
    setTimeout(connectDB, 5000);
  }
};

mongoose.connection.on('disconnected', () => {
  console.warn('MongoDB disconnected. Retrying connection in 5 seconds...');
  setTimeout(connectDB, 5000);
});

module.exports = connectDB;
