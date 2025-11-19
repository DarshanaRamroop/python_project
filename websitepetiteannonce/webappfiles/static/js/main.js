function openServiceOfferModal(advertId) {
    var modalId = `serviceOfferModal${advertId}`;
    var modal = document.getElementById(modalId);
    modal.style.display = "block";
    var form = document.getElementById(`serviceOfferForm${advertId}`);
    form.action = "/make_offer/service"; 
}

function openProductOfferModal(advertId) {
    var modalId = `productOfferModal${advertId}`;
    var modal = document.getElementById(modalId);
    modal.style.display = "block";
    var form = document.getElementById(`productOfferForm${advertId}`);
    form.action = "/make_offer/product";
}

function closeOfferModal(advertId) {
    var modal = document.getElementById("offerModal" + advertId);
    modal.style.display = "none";
}

window.onclick = function (event) {
    var modals = document.querySelectorAll(".modal");
    modals.forEach(function (modal) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};


let slideIndex = 0;
showSlide(slideIndex);

function changeSlide(n) {
    showSlide(slideIndex += n);
}

function showSlide(n) {
    const testimonials = document.getElementsByClassName("testimonial");
    if (n >= testimonials.length) {
        slideIndex = 0;
    } else if (n < 0) {
        slideIndex = testimonials.length - 1;
    }

    for (let i = 0; i < testimonials.length; i++) {
        testimonials[i].classList.remove("active");
    }

    testimonials[slideIndex].classList.add("active");
}

setInterval(() => {
    changeSlide(1);
}, 5000); 