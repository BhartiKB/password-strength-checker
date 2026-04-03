# Password Strength Checker

A simple full-stack cybersecurity mini project built with Flask, HTML, CSS, and JavaScript.

## Features
- Password strength analysis
- Suggestions to improve weak passwords
- Breach lookup using the Have I Been Pwned k-anonymity API
- Strong password generator
- Simple and clean UI

# Password Strength Checker

A simple full-stack cybersecurity mini project built using Flask, HTML, CSS, and JavaScript. It checks password strength, gives improvement suggestions, generates strong passwords, and checks whether a password appears in known breach results.

## Features

- Password strength analysis
- Suggestions to improve weak passwords
- Breach lookup using Have I Been Pwned k-anonymity API
- Strong password generator
- Simple and clean UI

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure

```text
password-strength-checker/
|__ app.py
|__ requirements.txt
|__ README.md
|__ templates/
|   |__ index.html
|__ static/
|   |__ style.css
|   |__ script.js

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`

## Deploy on Render
Build command:
```bash
pip install -r requirements.txt
```

Start command:
```bash
gunicorn app:app
```

## Live Demo
[View Live Project](https://password-strength-checker-pd50.onrender.com/)

