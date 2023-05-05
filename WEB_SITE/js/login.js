const logregBox = document.querySelector('.logreg-box');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const signInBtn = document.querySelector('#btn-in');
const signUpBtn = document.querySelector('#btn-up');

// Ajouter un événement onclick
signInBtn.onclick = function(event) {
  // Récupérer la valeur de l'input email
  const emailInput = document.querySelector('#email-in');
  const email = emailInput.value.trim();

  // Vérifier si l'email est valide
  if (!isValidEmail(email)) {
    // Empêcher l'action par défaut du bouton
    event.preventDefault();

    // Afficher un message d'erreur
    alert('Please enter a valid email address');
  }
}

// Ajouter un événement onclick
signUpBtn.onclick = function(event) {
    // Récupérer la valeur de l'input email
    const emailUpput = document.querySelector('#email-up');
    const email = emailUpput.value.trim();
  
    // Vérifier si l'email est valide
    if (!isValidEmail(email)) {
      // Empêcher l'action par défaut du bouton
      event.preventDefault();
  
      // Afficher un message d'erreur
      alert('Please enter a valid email address');
    }
  }

// Fonction pour valider l'email
function isValidEmail(email) {
    // Utiliser une expression régulière pour valider l'email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }