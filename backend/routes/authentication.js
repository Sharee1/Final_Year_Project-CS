const express = require("express");
const { JsonWebTokenError } = require("jsonwebtoken");
const router = express.Router();
const mongoose = require("mongoose");
const User = mongoose.model("User");
const jwt = require("jsonwebtoken");
require("dotenv").config();

let jwtSecretKey = process.env.JWT_SECRET_KEY;

router.post("/signup", (req, res) => {
  //res.send("this is signup");

  console.log("sent by client", req.body);
  const { email, username, password } = req.body;
  if (!email || !username || !password) {
    return res.status(422).send({ error: "please enter all the fields" });
  }
  User.findOne({ email: email }).then(async (savedUser) => {
    if (savedUser) {
      return res.status(422).send({ error: "invalid credentials" });
    }

    const user = new User({
      email,
      username,
      password,
    });

    try {
      await user.save();
      const token = jwt.sign({ _id: user._id }, jwtSecretKey);

      res.send({ message: "User Registered Successfully", token });
    } catch (err) {
      console.log("db error" + err);
      return res.status(422).send({ error: err.message });
    }
  });
});

module.exports = router;
