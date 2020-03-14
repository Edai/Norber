const express = require("express");
const multer = require("multer");
const crypto = require("crypto");
const path = require("path");
const cors = require("cors");

const storage = multer.diskStorage({
  destination: "videos/",
  filename: function(req, file, cb) {
    crypto.pseudoRandomBytes(16, function(err, raw) {
      if (err) return cb(err);
      cb(null, raw.toString("hex") + path.extname(file.originalname));
    });
  }
});

const upload = multer({ storage: storage });
const router = express.Router();

router.use(cors());

/* GET home page. */
router.get("/", function(req, res, next) {
  res.render("index", { title: "Express" });
});

router.post("/upload", upload.single("video"), function(req, res, next) {
  console.log("POST /upload/");
  const file = req.file;
  if (!file) {
    const error = new Error("Please upload a file");
    error.httpStatusCode = 400;
    return next(error);
  }
  res.send(file);
});

module.exports = router;
