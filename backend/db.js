const mongoose = require("mongoose");

mongoose
  .connect(
    "mongodb+srv://muhammadadnan:abbottabad18@cluster0.fvlusjk.mongodb.net/?retryWrites=true&w=majority"
  )
  .then(() => {
    console.log("DB connected");
  })
  .catch((err) => {
    console.log("could not connect to database" + err);
  });
