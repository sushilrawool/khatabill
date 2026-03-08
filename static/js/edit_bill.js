// Parse products from JSON
const productsData = JSON.parse(document.getElementById('products-data').textContent);

// Remove row
function removeRow(button) {
    button.closest("tr").remove();
    updateTotal();
}

// Set price on select
function setPrice(select) {
    const price = parseFloat(select.options[select.selectedIndex].dataset.price) || 0;
    const row = select.closest("tr");
    row.querySelector("input[name='price[]']").value = price.toFixed(2);
    updateTotal();
}

// Add new row
function addRow() {
    const table = document.querySelector(".customer-bills tbody");
    const newRow = document.createElement("tr");

    let options = '<option value="">-- Select Product --</option>';
    productsData.forEach(p => {
        options += `<option value="${p.id}" data-price="${p.price}">${p.product_name}</option>`;
    });

    newRow.innerHTML = `
        <td>
            <select name="product_id[]" onchange="setPrice(this)">
                ${options}
            </select>
        </td>
        <td><input type="number" name="quantity[]" value="1" min="0" oninput="updateTotal()"></td>
        <td><input type="number" name="price[]" value="0" min="0" step="0.01" oninput="updateTotal()"></td>
        <td><button type="button" class="btn remove-btn" onclick="removeRow(this)">Remove</button></td>
    `;
    table.appendChild(newRow);
}

// Update total
function updateTotal() {
    const rows = document.querySelectorAll(".customer-bills tbody tr");
    let total = 0;
    rows.forEach(row => {
        const quantity = parseFloat(row.querySelector("input[name='quantity[]']").value) || 0;
        const price = parseFloat(row.querySelector("input[name='price[]']").value) || 0;
        total += quantity * price;
    });
    document.getElementById("totalAmount").innerText = total.toFixed(2);
}

// Initialize total on load
window.addEventListener('DOMContentLoaded', updateTotal);