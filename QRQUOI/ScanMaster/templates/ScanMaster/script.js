document.querySelector('.next-slide').addEventListener('click', function() {
    changeSlide(1);
});
document.querySelector('.prev-slide').addEventListener('click', function() {
    changeSlide(-1);
});

let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');

function changeSlide(direction) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
    document.querySelector('.carousel-slides').style.transform = `translateX(-${currentSlide * 100}%)`;
}