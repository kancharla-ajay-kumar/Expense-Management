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

  // Clean and sanitize the connection string (remove accidental quotes, spaces, or prefix)
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
    console.error(`Received URI starts with: "${mongoUri.slice(0, 16)}..."`);
    console.error(
      '-> ACTION REQUIRED: In MongoDB Atlas (cloud.mongodb.com):\n' +
      '   1. Go to Network Access -> Add IP Address -> Select "Allow Access from Anywhere" (0.0.0.0/0).\n' +
      '   2. In Database Access -> Check that the database user has readWrite permissions and correct password.'
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
