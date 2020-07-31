
// var Nav = document.querySelector(".navigation");
var back = document.querySelector(".background");
var checkBox = document.getElementById("#check");

document.querySelector('.check').addEventListener('click',()=>{
    back.classList.toggle('in');
});

document.querySelector('.background__link').addEventListener('click',()=>{
    back.classList.toggle('in');
});


var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("slideshow__slides");

    for( i = 0; i < slides.length; i++){
        slides[i].style.display = "none";
    }

    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";

    setTimeout(showSlides,10000);
}






