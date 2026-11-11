    const value1 = document.getElementById('value1');
    const value2 = document.getElementById('value2');
    const operation = document.getElementById('operation');
    const result = document.getElementById('result');
    const history = document.getElementById('history');
    const toggle = document.getElementById('toggle') || document.getElementById('toggol');
    const buttons = document.querySelectorAll('.buttons button');

    function applyTheme() {
        const isDarkMode = toggle ? Boolean(toggle.checked) : localStorage.getItem('theme') === 'dark' ||
            window.matchMedia('(prefers-color-scheme: dark)').matches;

        document.body.classList.toggle('dark-mode', isDarkMode);
        document.body.classList.toggle('light-mode', !isDarkMode);
        document.body.dataset.theme = isDarkMode ? 'dark' : 'light';

        document.body.style.backgroundColor = isDarkMode ? '#111827' : '#f5f7fb';
        document.body.style.color = isDarkMode ? '#f9fafb' : '#111827';

        const inputs = document.querySelectorAll('input, select, button, li');
        inputs.forEach((element) => {
            element.style.backgroundColor = isDarkMode ? '#1f2937' : '#ffffff';
            element.style.color = isDarkMode ? '#f9fafb' : '#111827';
            element.style.borderColor = isDarkMode ? '#374151' : '#d1d5db';
        });

        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
    }

    function calculate() {
        const first = Number(value1.value);
        const second = Number(value2.value);
        const op = operation.value;
        let answer;

        if (value1.value.trim() === '' || Number.isNaN(first) ||
            (op !== 'sqrt' && (value2.value.trim() === '' || Number.isNaN(second)))) {
            result.textContent = 'Please enter valid numbers.';
            return;
        }

        switch (op) {
            case '+': answer = first + second; break;
            case '-sup': answer = first - second; break;
            case '*': answer = first * second; break;
            case '^': answer = first ** second; break;
            case 'sqrt': answer = Math.sqrt(first); break;
            case '%': answer = (first * second) / 100; break;
            default: result.textContent = 'Invalid operation.'; return;
        }

        if (!Number.isFinite(answer)) {
            result.textContent = 'Invalid calculation.';
            return;
        }

        result.textContent = `Result: ${answer}`;
        const item = document.createElement('li');
        item.textContent = `${value1.value} ${op} ${op === 'sqrt' ? '' : value2.value} = ${answer}`;
        history.prepend(item);
    }

    function clearCalculator() {
        value1.value = '';
        value2.value = '';
        result.textContent = '';
        history.innerHTML = '';
    }

    buttons[0]?.addEventListener('click', calculate);
    buttons[1]?.addEventListener('click', clearCalculator);

    if (toggle) {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            toggle.checked = true;
        }

        toggle.addEventListener('change', applyTheme);
    }

    applyTheme();