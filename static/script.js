const passwordInput = document.getElementById('password');
const checkBtn = document.getElementById('checkBtn');
const generateBtn = document.getElementById('generateBtn');
const toggleBtn = document.getElementById('toggleBtn');
const resultBox = document.getElementById('result');
const strengthText = document.getElementById('strengthText');
const progressFill = document.getElementById('progressFill');
const suggestionsList = document.getElementById('suggestionsList');
const breachBox = document.getElementById('breachBox');

function getBarColor(strength) {
    if (strength === 'Weak') return '#dc2626';
    if (strength === 'Medium') return '#f59e0b';
    return '#16a34a';
}

function getBarWidth(score) {
    return `${Math.min((score / 6) * 100, 100)}%`;
}

checkBtn.addEventListener('click', async () => {
    const password = passwordInput.value;

    if (!password) {
        alert('Please enter a password.');
        return;
    }

    const response = await fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password })
    });

    const data = await response.json();

    resultBox.classList.remove('hidden');
    strengthText.textContent = data.strength;
    progressFill.style.width = getBarWidth(data.score);
    progressFill.style.background = getBarColor(data.strength);

    suggestionsList.innerHTML = '';
    if (data.suggestions.length === 0) {
        const li = document.createElement('li');
        li.textContent = 'Your password looks good.';
        suggestionsList.appendChild(li);
    } else {
        data.suggestions.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            suggestionsList.appendChild(li);
        });
    }

    breachBox.className = 'breach-box';
    breachBox.classList.remove('hidden');

    if (data.breach_found === true) {
        breachBox.textContent = `Warning: this password was found in breaches ${data.breach_count} times.`;
        breachBox.classList.add('breach-danger');
    } else if (data.breach_found === false) {
        breachBox.textContent = 'Good news: this password was not found in known breach results.';
        breachBox.classList.add('breach-safe');
    } else {
        breachBox.textContent = 'Breach check could not be completed right now.';
        breachBox.classList.add('breach-unknown');
    }
});

generateBtn.addEventListener('click', async () => {
    const response = await fetch('/generate');
    const data = await response.json();
    passwordInput.value = data.password;
});

toggleBtn.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = 'Hide';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = 'Show';
    }
});
