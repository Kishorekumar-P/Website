document.addEventListener('DOMContentLoaded', function() {
    const enquireButtons = document.querySelectorAll('.enquire-now');
    enquireButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            alert('Thank you for your enquiry! We will get back to you soon.');
        });
    });
});


