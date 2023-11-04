const express = require("express");
const bodyParser = require("body-parser");
const port = 3000;

const app = express();

require("dotenv").config();
require("./db");
require("./models/user");
const authentication = require("./routes/authentication");

app.use(bodyParser.json());
app.use(authentication);

app.get("/", function (req, res) {
  res.send("this is homepage");
});

app.listen(port, function () {
  console.log("running");
});
