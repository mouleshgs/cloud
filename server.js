const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const mongoURI = "mongodb+srv://moulesh:14032006@cluster0.0d35x37.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

mongoose.connect(mongoURI)
  .then(() => console.log('✅ Connected to MongoDB Atlas'))
  .catch(err => console.error('❌ MongoDB connection error:', err));

const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  age: Number
});

const User = mongoose.model('User', userSchema);

app.post('/users', async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.send('User Added');
});

app.get('/users', async (req, res) => {
  const users = await User.find();
  res.json(users);
});

app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});

app.put('/update/:id', async (req, res) => {
  await User.findByIdAndUpdate(req.params.id, req.body);
  res.send('User Updated');
});

app.delete('/delete/:id', async (req, res) => {
  await User.findByIdAndDelete(req.params.id);
  res.send('User Deleted');
});

app.listen(3000, () => {
  console.log('🚀 Server running on http://localhost:3000');
});