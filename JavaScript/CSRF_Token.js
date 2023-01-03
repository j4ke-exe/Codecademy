const express = require('express');
const partials = require('express-partials');
const path = require('path');
const app = express();

const csurf = require('csurf');
const cookieParser = require('cookie-parser');

const PORT = 4001;

app.set("views", path.join(__dirname, "/views"));
app.set("view engine", "ejs");
app.set('trust proxy', 1); 
app.use(partials());

app.use(cookieParser());

app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.use(express.static(path.join(__dirname, "/public")));

app.get('/', (req, res) => {
  res.render('form')
});

app.post('/submit', (req, res) => {
  res.send(`<p>Post successful!</p> <p>CSRF token used: ${req.body._csrf}</p>`);
});

app.listen(PORT, () => console.log(`Listening on http://localhost:${PORT}`) );
