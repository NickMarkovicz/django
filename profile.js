document.addEventListener("DOMContentLoaded", function() {
  function showMessage() {
    let message = "Я бы сохранил это, но пока некуда :)";
    alert(message);
  }

  const button = document.getElementById("save-button");

  button.addEventListener("click", showMessage);
});
