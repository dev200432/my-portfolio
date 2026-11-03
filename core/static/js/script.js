// Theme Toggle Functionality
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const icon = themeToggle.querySelector('i');

themeToggle.addEventListener('click', () => {
    if (body.getAttribute('data-theme') === 'dark') {
        body.setAttribute('data-theme', 'light');
        icon.classList.replace('fa-moon', 'fa-sun');
    } else {
        body.setAttribute('data-theme', 'dark');
        icon.classList.replace('fa-sun', 'fa-moon');
    }
});

// Mobile Hamburger Navbar Toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
const navItems = document.querySelectorAll('.nav-item');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    const iconElem = hamburger.querySelector('i');
    if (navLinks.classList.contains('active')) {
        iconElem.classList.replace('fa-bars', 'fa-times');
    } else {
        iconElem.classList.replace('fa-times', 'fa-bars');
    }
});

// Close navbar on clicking any link on mobile
navItems.forEach(item => {
    item.addEventListener('click', () => {
        navLinks.classList.remove('active');
        hamburger.querySelector('i').classList.replace('fa-times', 'fa-bars');
    });
});

// Project Description Read More / Read Less Toggle Functionality
function toggleDescription(descId, btn) {
    const descElement = document.getElementById(descId);
    descElement.classList.toggle('expanded');
    if (descElement.classList.contains('expanded')) {
        btn.textContent = "Read Less";
    } else {
        btn.textContent = "Read More";
    }
}

// Typewriter Effect
const words = ["Python & Django Developer", "Full-Stack Web Engineer", "MySQL & Database Specialist", "UI/UX & Frontend Designer"];
let i = 0, j = 0, currentWord = "", isDeleting = false;
function type() {
    if (i < words.length) {
        if (!isDeleting && j <= words[i].length) {
            currentWord = words[i].substring(0, j++);
            document.getElementById("typewriter").innerHTML = currentWord;
            setTimeout(type, 100);
        } else if (isDeleting && j >= 0) {
            currentWord = words[i].substring(0, j--);
            document.getElementById("typewriter").innerHTML = currentWord;
            setTimeout(type, 50);
        } else {
            isDeleting = !isDeleting;
            if (!isDeleting) { i = (i + 1) % words.length; }
            setTimeout(type, 1000);
        }
    }
}
type();

// Scroll Observer for Fade-in & Progress Bars
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            const fills = entry.target.querySelectorAll('.fill');
            fills.forEach(fill => {
                fill.style.width = fill.getAttribute('data-width');
            });
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll('section').forEach(sec => observer.observe(sec));