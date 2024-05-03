/* abre e fecha menu lateral em modo mobile */

const menuMobile = document.querySelector('.menu-mobile'); 
const body = document.querySelector('body');

menuMobile.addEventListener("click", () => {
    menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.contains("bi-list", "bi-x") /* i e else ternario*/ 
    : menuMobile.classList.replace("bi-x", "bi-list");
body.classList.toggle("menu-nav-active")
});