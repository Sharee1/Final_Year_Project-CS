const mongoose = require("mongoose");
//creeating new datrabase is overwhelming in mongo db but in mongoose u just have to write url with a name of database at the end (/druitsDB)

//IN mongoose we have to create a structure for the collectins we will create inside this database they are called
//schemas
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
  },
  username: { type: String, required: true },
  password: { type: String, required: true },
});

//here we define the collection where first parameter takes the name of collections and second parameter takes the schema the colletion will be built upon
const User = mongoose.model("User", userSchema);
