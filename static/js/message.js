document.addEventListener('DOMContentLoaded', function() {
  const notification = document.getElementById('notification');

  if (notification) {
    // Показываем уведомление с анимацией
    setTimeout(() => {
      notification.classList.remove('notification--hidden');
      notification.classList.add('notification--visible');
    }, 100); // Небольшая задержка для корректного запуска анимации

    // Обработчик закрытия по кнопке
    const closeButton = notification.querySelector('.notification__close');
    if (closeButton) {
      closeButton.addEventListener('click', hideNotification);
    }

    // Автоматически скрываем через 5 секунд
    setTimeout(hideNotification, 5000);
  }

  function hideNotification() {
    notification.classList.remove('notification--visible');
    notification.classList.add('notification--hidden');

    // Удаляем элемент из DOM после завершения анимации скрытия
    setTimeout(() => {
      if (notification.parentNode) {
        notification.parentNode.removeChild(notification);
      }
    }, 500); // Время должно соответствовать transition в CSS
  }
});

