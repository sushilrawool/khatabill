// Dummy reports data
const reports = [
    {billId: 101, customer: "Sushil Rawool", date: "2026-02-19", amount: 500, status: "Paid"},
    {billId: 102, customer: "Sushil Rawool", date: "2026-02-18", amount: 700, status: "Pending"},
    {billId: 103, customer: "Rahul Sharma", date: "2026-02-17", amount: 500, status: "Pending"},
    {billId: 104, customer: "Anita Patil", date: "2026-02-15", amount: 1000, status: "Paid"},
];

const tbody = document.getElementById('reportList');

function renderReports(){
    tbody.innerHTML = "";
    reports.forEach(r => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${r.billId}</td>
            <td>${r.customer}</td>
            <td>${r.date}</td>
            <td>₹ ${r.amount}</td>
            <td>${r.status}</td>
            <td>
                <button class="view-btn" onclick="viewReport(${r.billId})">View</button>
                <button class="download-btn" onclick="downloadReport(${r.billId})">Download</button>
                s
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function viewReport(id){
    alert(`Viewing report for Bill ID ${id}`);
    // You can implement modal or new page to show report
}

function downloadReport(id){
    alert(`Downloading report for Bill ID ${id}`);
    // You can integrate PDF generation & download here
}

function logout(){
    alert("Logging out...");
    window.location.href = "/template/login.html";
}

// Initial render
renderReports();





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


document.getElementById("filter-btn").addEventListener("click", function(){
    let customerId = document.getElementById("customer-filter").value;
    let fromDate = document.getElementById("from-date").value;
    let toDate = document.getElementById("to-date").value;

    let params = new URLSearchParams();
    if(customerId) params.append('customer_id', customerId);
    if(fromDate) params.append('from_date', fromDate);
    if(toDate) params.append('to_date', toDate);

    window.location.href = "/reports?" + params.toString();
});


document.addEventListener('DOMContentLoaded', () => {
    const filterBtn = document.getElementById('filter-btn');
    const customerFilter = document.getElementById('customer-filter');
    const fromDate = document.getElementById('from-date');
    const toDate = document.getElementById('to-date');

    const billsTable = document.getElementById('bills-table').getElementsByTagName('tbody')[0];

    filterBtn.addEventListener('click', () => {
        const customerVal = customerFilter.value;
        const fromVal = fromDate.value;
        const toVal = toDate.value;

        for (let row of billsTable.rows) {
            let customerId = row.dataset.customerId || row.cells[1].dataset.id || "";
            let date = row.cells[2].innerText;

            let show = true;

            // Filter by customer
            if (customerVal && customerId != customerVal) {
                show = false;
            }

            // Filter by from date
            if (fromVal && date < fromVal) {
                show = false;
            }

            // Filter by to date
            if (toVal && date > toVal) {
                show = false;
            }

            row.style.display = show ? '' : 'none';
        }
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