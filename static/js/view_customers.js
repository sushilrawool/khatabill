// Populate customers from backend (replace dummy data with actual backend data)
const customers = [
    {id: 1, name: "Sushil Rawool", phone: "9876543210", email: "sushil@example.com", totalBills: 5, pendingBills: 2, pendingAmount: 1200},
    {id: 2, name: "Rahul Sharma", phone: "9123456780", email: "rahul@example.com", totalBills: 3, pendingBills: 1, pendingAmount: 500},
    {id: 3, name: "Anita Patil", phone: "9988776655", email: "anita@example.com", totalBills: 7, pendingBills: 0, pendingAmount: 0}
];

const tbody = document.getElementById('customerList');

// Function to render customers in table
function renderCustomers(list) {
    tbody.innerHTML = ''; // Clear existing rows
    list.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${c.id}</td>
            <td>${c.name}</td>
            <td>${c.phone}</td>
            <td>${c.email}</td>
            <td>${c.totalBills}</td>
            <td>${c.pendingBills}</td>
            <td>₹ ${c.pendingAmount}</td>
        `;
        tbody.appendChild(tr);
    });
}

// Initial render
renderCustomers(customers);

// Search functionality
const searchInput = document.getElementById('searchBox');
searchInput.addEventListener('input', function() {
    const filter = this.value.toLowerCase();
    const filtered = customers.filter(c => c.name.toLowerCase().includes(filter));
    renderCustomers(filtered);
});

// Logout button
function logout() {
    alert("Logging out...");
    window.location.href = "/template/login.html";
}



searchInput.addEventListener("keyup", function() {

    let filter = searchInput.value.toLowerCase();
    let table = document.getElementById("customerTable");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {

        let nameCell = rows[i].getElementsByTagName("td")[1];
        if (!nameCell) continue;

        let name = nameCell.textContent.toLowerCase();

        if (name.includes(filter)) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }

});



document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});