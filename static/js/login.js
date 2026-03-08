// ======================= Login Page =======================
function showError(message) {
    const error = document.getElementById("error");
    error.innerText = message;
    error.classList.add("show");
}

function hideError() {
    const error = document.getElementById("error");
    error.classList.remove("show");
}

function login() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    hideError();

    if (!username && !password) {
        showError("Please enter username and password");
        return;
    }

    if (!username || !password) {
        showError("All fields are required");
        return;
    }

    if (username === "admin" && password === "1234") {
        localStorage.setItem("loggedUser", username); // Save login
        window.location.href = "dashboard.html";
    } else {
        showError("Invalid username or password");
    }
}



// =================== Add Bill Page ===================
function dashboard(){
          window.location.href = "dashboard.html";
    }
if (window.location.pathname.includes("addBill.html")) {
    // Login check
    if (!localStorage.getItem("loggedUser")) {
        window.location.href = "login.html";
    }
    const customers = [
        { name: "Rahul", products: [{ name: "Rice 1kg", price: 60 }, { name: "Oil 1L", price: 180 }] },
        { name: "Amit", products: [{ name: "Sugar 1kg", price: 45 }, { name: "Tea Powder 250g", price: 120 }] },
        { name: "Suresh", products: [{ name: "Wheat Flour 1kg", price: 55 }, { name: "Oil 1L", price: 180 }] }
    ];

    let selectedProducts = [];
    const customerInput = document.getElementById("customer");
    const customerList = document.getElementById("customerList");
    const tbody = document.getElementById("billItems");

    function searchCustomer() {
        customerList.innerHTML = "";
        const value = customerInput.value.toLowerCase();
        if (!value) return;

        customers.filter(c => c.name.toLowerCase().includes(value))
            .forEach(c => {
                const div = document.createElement("div");
                div.innerText = c.name;
                div.onclick = () => selectCustomer(c);
                customerList.appendChild(div);
            });
    }

    function selectCustomer(customer) {
        customerInput.value = customer.name;
        customerList.innerHTML = "";
        selectedProducts = customer.products;
        tbody.innerHTML = "";
        addRow();
    }

    function addRow() {
        if (selectedProducts.length === 0) return;

        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>
                <select onchange="updateRow(this)">
                    <option value="">Select</option>
                    ${selectedProducts.map((p,i)=>`<option value="${i}">${p.name}</option>`).join("")}
                </select>
            </td>
            <td><input type="number" value="1" min="1" oninput="updateRow(this)"></td>
            <td><input type="number" readonly></td>
            <td><input type="number" readonly></td>
            <td><button class="remove" onclick="removeRow(this)">×</button></td>
        `;
        tbody.appendChild(tr);
    }

    function updateRow(el) {
        const row = el.closest("tr");
        const pIndex = row.children[0].children[0].value;
        const qty = Number(row.children[1].children[0].value);
        if (pIndex === "") return;

        const price = selectedProducts[pIndex].price;
        row.children[2].children[0].value = price;
        row.children[3].children[0].value = price * qty;
        calcGrand();
    }

    function removeRow(btn) {
        btn.closest("tr").remove();
        calcGrand();
    }

    function calcGrand() {
        let total = 0;
        document.querySelectorAll("#billItems tr").forEach(r => {
            total += Number(r.children[3].children[0].value || 0);
        });
        document.getElementById("grandTotal").innerText = total;
    }

    function saveBill() {
        const status = document.getElementById("status").value;
        const error = document.getElementById("errorMsg");

        if (!customerInput.value || !status) {
            error.innerText = "Please fill all fields";
            return;
        }

        const bills = JSON.parse(localStorage.getItem("bills")) || [];
        bills.push({
            customer: customerInput.value,
            total: document.getElementById("grandTotal").innerText,
            status,
            date: new Date().toISOString().split("T")[0]
        });

        localStorage.setItem("bills", JSON.stringify(bills));
        window.location.href = "dashboard.html";
    }

    function goBack() {
        window.location.href = "dashboard.html";
    }

    window.searchCustomer = searchCustomer;
    window.selectCustomer = selectCustomer;
    window.addRow = addRow;
    window.updateRow = updateRow;
    window.removeRow = removeRow;
    window.calcGrand = calcGrand;
    window.saveBill = saveBill;
    window.goBack = goBack;
    window.logout = function() {
        localStorage.removeItem("loggedUser");
        window.location.href = "login.html";
    };
}


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});