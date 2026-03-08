// Dummy bill-wise data
let bills = [
    {billId: 101, customer: "Sushil Rawool", date: "2026-02-19", amount: 500, status: "Pending"},
    {billId: 102, customer: "Sushil Rawool", date: "2026-02-18", amount: 700, status: "Pending"},
    {billId: 103, customer: "Rahul Sharma", date: "2026-02-17", amount: 500, status: "Pending"},
    {billId: 104, customer: "Anita Patil", date: "2026-02-15", amount: 1000, status: "Paid"},
];

const tbody = document.getElementById('pendingBillList');

function renderTable() {
    tbody.innerHTML = "";
    bills.forEach(b => {
        if(b.status === "Pending"){
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${b.billId}</td>
                <td>${b.customer}</td>
                <td>${b.date}</td>
                <td>₹ ${b.amount}</td>
                <td>${b.status}</td>
                <td><button class="mark-paid-btn" onclick="markBillPaid(${b.billId})">Mark as Paid</button></td>
                <button class="print-btn" onclick="printBill(${b.billId})">Print / Download</button>
            `;
            tbody.appendChild(tr);
        }
    });
}

function markBillPaid(id){
    const bill = bills.find(b => b.billId === id);
    if(bill){
        bill.status = "Paid";
        renderTable();
        alert(`Bill ID ${bill.billId} marked as Paid`);
    }
}

function logout() {
    alert("Logging out...");
    window.location.href = "/template/login.html";
}

// Initial render
renderTable();


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});







function printBill(billIdOrObject){
    let bill;

    // अगर object आहे, तर direct use करा
    if(typeof billIdOrObject === 'object'){
        bill = billIdOrObject;
    } else {
        // number असल्यास, तुमच्या bills array मधून fetch करा
        bill = bills.find(b => b.billId === billIdOrObject);
    }

    if(!bill){
        alert("Bill not found");
        return;
    }

    // Populate template
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

    // Print / Download
    let w = window.open();
    w.document.write(document.getElementById("billTemplate").innerHTML);
    w.print();
    w.close();
}
