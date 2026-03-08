// This function works for Add Bill / Pending Bills / Reports page
function printBill(bill){
    if(!bill){
        alert("Bill not found or save the bill first!");
        return;
    }

    document.getElementById("cName").innerText = bill.customer;
    document.getElementById("cPhone").innerText = bill.phone || "-";
    document.getElementById("bDate").innerText = bill.date;
    document.getElementById("grandTotal").innerText = bill.totalAmount;
    document.getElementById("payStatus").innerText = bill.status;

    const tbody = document.getElementById("billProducts");
    tbody.innerHTML = "";
    bill.products.forEach(p => {
        const tr = document.createElement("tr");
        tr.innerHTML = `<td>${p.name}</td><td>${p.qty}</td><td>${p.price}</td><td>${p.total}</td>`;
        tbody.appendChild(tr);
    });

    let w = window.open();
    w.document.write(document.getElementById("billTemplate").innerHTML);
    w.print();
    w.close();
}


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});