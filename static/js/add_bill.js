// ===============================
// ADD BILL JS
// ===============================

const data = JSON.parse(document.getElementById('flaskData').textContent);
const customers = data.customers;
const products = data.products;

const billForm = document.getElementById("billForm");

// ===============================
// CUSTOMER SEARCH
// ===============================
function searchCustomer() {
    const val = document.getElementById("customer").value.toLowerCase();
    const list = document.getElementById("customerList");
    list.innerHTML = "";

    if (!val) {
        document.getElementById("customer_id").value = "";
        list.style.display = "none";
        return;
    }

    customers
        .filter(c => c.name.toLowerCase().includes(val))
        .forEach(c => {
            const div = document.createElement("div");
            div.textContent = c.name;
            div.onclick = () => {
                document.getElementById("customer").value = c.name;
                document.getElementById("customer_id").value = c.id;
                list.innerHTML = "";
                list.style.display = "none";
            };
            list.appendChild(div);
        });

    list.style.display = list.children.length ? "block" : "none";
}

// ===============================
// ADD PRODUCT ROW
// ===============================
function addRow() {
    const tbody = document.getElementById("billItems");
    const tr = document.createElement("tr");
    tr.classList.add("new-row");

    tr.innerHTML = `
        <td>
            <input type="text" list="productList" onchange="productChanged(this)" required>
            <datalist id="productList">
                ${products.map(p => `<option value="${p.product_name}"></option>`).join("")}
            </datalist>
            <input type="hidden" name="product_id[]">
            <input type="hidden" name="price[]">
            <input type="hidden" name="unit[]">
        </td>

        <td><input type="number" name="quantity[]" value="1" min="1" onchange="calculateRow(this)" required></td>
        <td class="unit">-</td>
        <td class="price">0.00</td>
        <td class="row-total">0.00</td>
        <td><button type="button" class="remove-btn" onclick="removeRow(this)">✕</button></td>
    `;

    tbody.appendChild(tr);

    // Animate new row
    setTimeout(() => tr.classList.add("show"), 10);
}

// ===============================
// PRODUCT CHANGE
// ===============================
function productChanged(input) {
    const row = input.closest("tr");
    const product = products.find(
        p => p.product_name.toLowerCase() === input.value.toLowerCase()
    );

    if (!product) {
        row.querySelector('input[name="product_id[]"]').value = "";
        row.querySelector('input[name="price[]"]').value = 0;
        row.querySelector('input[name="unit[]"]').value = "";
        row.querySelector(".price").textContent = "0.00";
        row.querySelector(".unit").textContent = "-";
        calculateRow(row.querySelector('input[name="quantity[]"]'));
        return;
    }

    row.querySelector('input[name="product_id[]"]').value = product.id;
    row.querySelector('input[name="price[]"]').value = product.price;
    row.querySelector('input[name="unit[]"]').value = product.unit;

    row.querySelector(".price").textContent = parseFloat(product.price).toFixed(2);
    row.querySelector(".unit").textContent = product.unit;

    calculateRow(row.querySelector('input[name="quantity[]"]'));
}

// ===============================
// CALCULATE ROW & GRAND TOTAL
// ===============================
function calculateRow(input) {
    const row = input.closest("tr");
    const price = parseFloat(row.querySelector('input[name="price[]"]').value) || 0;
    const qty = parseFloat(input.value) || 0;

    row.querySelector(".row-total").textContent = (price * qty).toFixed(2);

    calculateGrandTotal();
}

function calculateGrandTotal() {
    let sum = 0;
    document.querySelectorAll(".row-total").forEach(td => {
        sum += parseFloat(td.textContent) || 0;
    });
    document.getElementById("grandTotal").textContent = sum.toFixed(2);
}

// ===============================
// REMOVE ROW
// ===============================
function removeRow(btn) {
    btn.closest("tr").remove();
    calculateGrandTotal();
}

// ===============================
// INIT
// ===============================
document.addEventListener("DOMContentLoaded", () => {
    addRow(); // add one default row

    billForm.addEventListener("submit", e => {
        const customerId = document.getElementById("customer_id").value;
        if (!customerId) {
            e.preventDefault();
            alert("Please select a customer!");
            return;
        }

        const productIds = document.querySelectorAll('input[name="product_id[]"]');
        if ([...productIds].some(p => !p.value)) {
            e.preventDefault();
            alert("Please select valid products!");
        }
    });
});

// ===============================
// PAYMENT STATUS STYLING
// ===============================
const status = document.getElementById("status");
const statusWrapper = status.parentElement;

status.addEventListener("change", () => {
    status.classList.remove("status-paid", "status-pending");

    if (status.value === "PAID") status.classList.add("status-paid");
    else if (status.value === "PENDING") status.classList.add("status-pending");
});

// Ripple effect on mousedown
status.addEventListener("mousedown", () => {
    const ripple = document.createElement("span");
    ripple.className = "select-ripple";
    statusWrapper.appendChild(ripple);
    setTimeout(() => ripple.remove(), 400);
});