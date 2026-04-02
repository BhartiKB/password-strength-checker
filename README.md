# Password Strength Checker

A simple full-stack cybersecurity mini project built with Flask, HTML, CSS, and JavaScript.

## Features
- Password strength analysis
- Suggestions to improve weak passwords
- Breach lookup using the Have I Been Pwned k-anonymity API
- Strong password generator
- Simple and clean UI

## Project Structure
password-strength-checker/
│── app.py # Main Flask backend
│── requirements.txt # Dependencies
│── README.md # Project documentation
│
├── templates/
│ └── index.html # Frontend HTML
│
└── static/
├── style.css # Styling
└── script.js # Frontend logic

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
