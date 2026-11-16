const mongoose = require('mongoose');

const connectDB = async () => {
  let rawUri = process.env.MONGO_URI;

  if (!rawUri) {
    console.error('MongoDB connection error: MONGO_URI environment variable is not defined.');
    if (process.env.NODE_ENV === 'production') {
      process.exit(1);
    }
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

  try {
    const conn = await mongoose.connect(mongoUri);
    console.log(`MongoDB connected: ${conn.connection.host}`);
  } catch (error) {
    console.error(`MongoDB connection error: ${error.message}`);
    console.error(`Received URI scheme starts with: "${mongoUri.slice(0, 16)}..."`);
    process.exit(1);
  }
};

module.exports = connectDB;
