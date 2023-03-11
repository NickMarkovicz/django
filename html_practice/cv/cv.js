document.addEventListener("DOMContentLoaded", function() {
  function showMessage() {
    let message = "Ваш очереднярский реквест отправлен Папичу";
    alert(message);
  }

  const button = document.getElementById("submit-button");

  button.addEventListener("click", showMessage);
});
