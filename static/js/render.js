const textWrite = document.getElementById('text-copy').textContent;
const typedText = new Typed('#typed-text', {
  strings: [textWrite],
  typeSpeed: 70,
  backSpeed: 70,
  loop: false,
  startDelay: 500,
  backDelay: 3000,
  showCursor: false
});
const boutonCopie = document.getElementById('button-copy');
const texteACopier = document.getElementById('text-copy').textContent;

boutonCopie.addEventListener('click', function() {
  navigator.clipboard.writeText(texteACopier);
  console.log('Le texte a été copié dans le presse-papiers !');
});