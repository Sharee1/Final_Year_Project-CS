const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

require("./db");
require("./models/user");

app.get("/", function (req, res) {
  res.send("this is homepage");
});

app.post("/signup", function (req, res) {});
app.listen("3000", function () {
  console.log("running");
});
