// customer_detail.js

// Show edit form using data-attributes
document.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const form = document.getElementById('editCustomerForm');
        form.style.display = 'block';
        document.getElementById('customer_id').value = btn.dataset.id;
        document.getElementById('customer_name').value = btn.dataset.name;
        document.getElementById('phone').value = btn.dataset.phone;
        document.getElementById('email').value = btn.dataset.email;
        document.getElementById('formBtn').textContent = 'Update Customer';
    });
});

// Cancel edit form
document.getElementById('cancelBtn').addEventListener('click', () => {
    const form = document.getElementById('editCustomerForm');
    form.style.display = 'none';
    document.getElementById('customerForm').reset();
});

// Optional: logout function
function logout() {
    window.location.href = "/logout"; // create logout route in Flask
}
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});