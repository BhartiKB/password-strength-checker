from flask import Flask, render_template, request, jsonify
import hashlib
import requests
import secrets
import string

app = Flask(__name__)


def password_score(password: str):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if len(password) >= 12:
        score += 1

    common_passwords = {
        "123456", "password", "qwerty", "admin", "letmein",
        "welcome", "abc123", "iloveyou", "12345678"
    }
    if password.lower() in common_passwords:
        suggestions.append("Avoid common passwords.")
        score = max(score - 2, 0)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions


def check_pwned(password: str):
    """Check password against Have I Been Pwned k-anonymity API."""
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            timeout=10,
            headers={"Add-Padding": "true"}
        )
        response.raise_for_status()
        hashes = (line.split(":") for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return True, int(count)
        return False, 0
    except requests.RequestException:
        return None, None


def generate_strong_password(length: int = 14):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(chars) for _ in range(length))
        score, strength, _ = password_score(password)
        if strength == "Strong":
            return password


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_password_route():
    data = request.get_json()
    password = data.get("password", "")

    score, strength, suggestions = password_score(password)
    breach_found, breach_count = check_pwned(password) if password else (False, 0)

    return jsonify({
        "score": score,
        "strength": strength,
        "suggestions": suggestions,
        "breach_found": breach_found,
        "breach_count": breach_count
    })


@app.route("/generate", methods=["GET"])
def generate_password_route():
    password = generate_strong_password()
    return jsonify({"password": password})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
