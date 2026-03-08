// Add Customer Form Handling
document.addEventListener('DOMContentLoaded', function () {

    const form = document.getElementById('addCustomerForm');

    if (!form) {
        console.error('Add Customer form not found');
        return;
    }

    form.addEventListener('submit', function (e) {

        const name = document.getElementById('name').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const email = document.getElementById('email').value.trim();
        const address = document.getElementById('address').value.trim();
        const opening_balance = document.getElementById('opening_balance').value.trim();

        // ✅ Basic validation
        if (name === '' || phone === '') {
            e.preventDefault(); // ❗ stop submit only on error
            alert('Customer Name and Phone Number are required.');
            return;
        }

        // ✅ Phone number validation (optional but safe)
        if (phone.length < 10) {
            e.preventDefault();
            alert('Please enter a valid phone number.');
            return;
        }

        // ❗ IMPORTANT
        // No preventDefault here
        // Form will submit normally to Flask backend
        // Data will be saved in database

        console.log('Submitting customer:', {
            name,
            phone,
            email,
            address,
            opening_balance
        });
    });

});


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});