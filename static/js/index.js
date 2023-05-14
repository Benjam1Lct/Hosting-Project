const typedText = new Typed('#typed-text', {
    strings: ['Extract text from image',' Discover your prediciton', 'Complet your documents'],
    typeSpeed: 70,
    backSpeed: 70,
    loop: true,
    startDelay: 500,
    backDelay: 3000
  });
const wrapper = document.querySelector(".wrapper");
const fileName = document.querySelector(".file-name");
const cancelBtn = document.querySelector("#cancel-btn");
const defaultBtn = document.querySelector("#default-btn");
const customBtn = document.querySelector("#custom-btn");
const img = document.querySelector("#img-upload");
const fileInput = document.querySelector('input[type="file"]');
const submitButton = document.querySelector('button[type="submit"]');

let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_]+$/;

function defaultBtnActive(){
    defaultBtn.click();
}
defaultBtn.addEventListener("change", function(){
    const file = this.files[0];
    if(file){
        const reader = new FileReader();
        reader.onload = function(){
            const result = reader.result;
            img.src = result;
            wrapper.classList.add('active');
        }
        cancelBtn.addEventListener("click", function(){
            img.src = "./static/img/transparent.png";
            fileInput.value = null;
            wrapper.classList.remove('active');
        })
        reader.readAsDataURL(file);
    }
    if(this.value){
        let valueStore = this.value.match(regExp);
        fileName.textContent = valueStore;
    }
});

submitButton.addEventListener('click', (event) => {
    if (fileInput.value === '') {
      event.preventDefault();
    }
  });

function showLoader() {
    // Masquer la page
    document.getElementById('page').style.display = 'none';
    // Afficher le loader
    img.src = "./static/img/4loader.gif";
}