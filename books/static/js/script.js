// ===== Search =====
let searchForm = document.querySelector('.search-form');
document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
};

// ===== Login =====
let loginForm = document.querySelector('.login-form-container');
document.querySelector('#login-btn').onclick = () => loginForm.classList.toggle('active');
document.querySelector('#close-login-btn').onclick = () => loginForm.classList.remove('active');

// ===== Header Scroll =====
window.onscroll = () => {
    searchForm.classList.remove('active');
    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
};
window.onload = () => {
    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }
    fadeOut();
};

// ===== Loader =====
function loader() {
    document.querySelector('.loader-container').classList.add('active');
}
function fadeOut() {
    setTimeout(loader, 1500);
}

// ===== Books Data =====
const books = [
    { img: staticUrl + 'image/book-1.png', title: 'کتاب اول', price: 5000, oldPrice: 10000, stars: 4.5 },
    { img: staticUrl + 'image/book-2.png', title: 'کتاب دوم', price: 6000, oldPrice: 12000, stars: 5 },
    { img: staticUrl + 'image/book-3.png', title: 'کتاب سوم', price: 7000, oldPrice: 14000, stars: 4 },
    { img: staticUrl + 'image/book-4.png', title: 'کتاب چهارم', price: 5500, oldPrice: 11000, stars: 4.5 },
    { img: staticUrl + 'image/book-5.png', title: 'کتاب پنجم', price: 6500, oldPrice: 13000, stars: 5 }
];

// ===== Insert Books =====
const arrivalsWrapper = document.getElementById('arrivals-wrapper');
books.forEach(book => {
    const bookSlide = document.createElement('a');
    bookSlide.href = '#';
    bookSlide.classList.add('swiper-slide', 'box');
    bookSlide.innerHTML = `
        <div class="image">
            <img src="${book.img}" alt="${book.title}">
        </div>
        <div class="content">
            <h3>${book.title}</h3>
            <div class="price">${book.price} هزارتومان <span>${book.oldPrice} هزارتومان</span></div>
            <div class="stars">
                ${'<i class="fas fa-star"></i>'.repeat(Math.floor(book.stars))}
                ${book.stars % 1 ? '<i class="fas fa-star-half-alt"></i>' : ''}
            </div>
        </div>
    `;
    arrivalsWrapper.appendChild(bookSlide);
});

// ===== Swipers =====
new Swiper('.arrivals-slider', {
    loop: true,
    spaceBetween: 20,
    navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
    pagination: { el: '.swiper-pagination', clickable: true },
    breakpoints: {
        0: { slidesPerView: 1 },
        640: { slidesPerView: 2 },
        768: { slidesPerView: 3 },
        1024: { slidesPerView: 4 }
    }
});

new Swiper('.reviews-slider', {
    spaceBetween: 10,
    grabCursor: true,
    loop: true,
    autoplay: { delay: 4000, disableOnInteraction: false },
    breakpoints: {
        0: { slidesPerView: 1 },
        768: { slidesPerView: 2 },
        1024: { slidesPerView: 3 }
    }
});
