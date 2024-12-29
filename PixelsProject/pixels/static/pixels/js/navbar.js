//Variables Declaration
const navbarToggler = document.getElementById("navbar-toggler");
const navLinks = document.getElementById("nav-links");
const navItems = document.querySelectorAll("li a")

//Event Listeners
navbarToggler.addEventListener("click", toggleMenu);
navItems.forEach(item => item.addEventListener("click", toggleMenu));

//Function to open menu
function toggleMenu() {
    navbarToggler.classList.toggle("active");
    navLinks.classList.toggle("active");
}

//Function to close menu
function closeMenu() {
    navbarToggler.classList.remove("active");
    navLinks.classList.remove("active");
}

// Function to handle navigation item click
function handleNavItemClick(e) {
    e.preventDefault(); // Prevent default anchor click behavior
    closeMenu(); // Close the mobile menu

    // Smooth scroll to the section
    const targetId = this.getAttribute("href").substring(1);
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
        targetElement.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
}