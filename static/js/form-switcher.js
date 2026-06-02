document.addEventListener('DOMContentLoaded', function() {
    const switchButtons = document.querySelectorAll('.switch-btn');
    const loginForm = document.querySelector('.login-form');
    const registerForm = document.querySelector('.register-form');

    switchButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Убираем активный класс у всех кнопок и форм
            switchButtons.forEach(btn => btn.classList.remove('active'));
            loginForm.classList.remove('active');
            registerForm.classList.remove('active');

            // Добавляем активный класс текущей кнопке и соответствующей форме
            this.classList.add('active');

            if (this.dataset.form === 'login') {
                loginForm.classList.add('active');
            } else {
                registerForm.classList.add('active');
            }
        });
    });
});
