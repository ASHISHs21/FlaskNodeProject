const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");
const app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

// Show form
app.get("/", (req, res) => {
  res.render("form");
});

// Submit To-Do item
app.post("/submit", async (req, res) => {
  const { itemName, itemDescription } = req.body;
  try {
    // Flask backend service name used (from docker-compose)
    const response = await axios.post("http://flask-backend:5000/submittodoitem", {
      itemName,
      itemDescription,
    });
    res.render("index", { result: response.data.message });
  } catch (error) {
    console.error(error);
    res.render("index", { result: "Error submitting data to Flask backend!" });
  }
});

app.listen(3000, "0.0.0.0", () => {
  console.log("✅ Frontend running on http://localhost:3000");
});
