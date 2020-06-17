class MobileMenu {
    constructor() {
        this.menuIcon = document.querySelector(".site-nav__menu-icon")
        this.menuContent = document.querySelector(".site-nav__overlay")
        this.events()
    }

    events() {
        this.menuIcon.addEventListener("click", () => this.toggleTheMenu())
    }

    toggleTheMenu() {

        this.menuContent.classList.toggle("site-nav__overlay--is-visible")
        this.menuIcon.classList.toggle("site-nav__menu-icon--close-x")
    }
}

new MobileMenu();

// In case of modules for js. For now only a small file, so one file will do.
// export default MobileMenu 
