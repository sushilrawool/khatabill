// Animate number helper
function animateNumber(id){
    let el = document.getElementById(id);
    if(!el) return;

    // Remove non-digit characters
    let raw = el.textContent.replace(/[^0-9.]/g,''); 
    let target = parseFloat(raw) || 0;
    let count = 0;
    let step = Math.max(1, Math.ceil(target / 100)); // avoid 0 step

    let interval = setInterval(()=>{
        count += step;
        if(count >= target){ count = target; clearInterval(interval); }
        el.textContent = '₹ ' + count.toLocaleString();
    }, 10);
}

// Animate all cards after DOM ready
// Animate number helper
function animateNumber(id, isAmount = false){  // <-- add flag
    let el = document.getElementById(id);
    if(!el) return;

    // Remove non-digit characters
    let raw = el.textContent.replace(/[^0-9.]/g,''); 
    let target = parseFloat(raw) || 0;
    let count = 0;
    let step = Math.max(1, Math.ceil(target / 100));

    let interval = setInterval(()=>{
        count += step;
        if(count >= target){ count = target; clearInterval(interval); }
        if(isAmount){
            el.textContent = '₹ ' + count.toLocaleString();
        }else{
            el.textContent = count.toLocaleString();
        }
    }, 10);
}

// Animate all cards after DOM ready
window.addEventListener('DOMContentLoaded', ()=> {
    animateNumber('totalCustomers'); // number only
    animateNumber('totalBills');     // number only
    animateNumber('pendingAmount', true); // ₹
    animateNumber('todayCollection', true); // ₹

    // Welcome card
    const card = document.getElementById("welcome-card");
    if(card){
        if(!localStorage.getItem("welcomeShown")){
            localStorage.setItem("welcomeShown","true");
            setTimeout(()=>card.classList.add("show"),300);
            setTimeout(()=>card.classList.add("hide"),3000);
        }
    }
});
// Refresh / logout
function refreshDashboard(){ window.location.reload(); }
function logout(){ window.location.href = "/logout"; }





document.addEventListener("DOMContentLoaded", ()=>{
    // Fade-in on page load
    document.body.classList.add('fade-enter');
    setTimeout(()=> document.body.classList.add('fade-enter-active'), 50);

    // Handle link clicks for fade-out
    document.querySelectorAll('a').forEach(link=>{
        link.addEventListener('click', e=>{
            const href = link.getAttribute('href');
            if(!href.startsWith('http') && !href.startsWith('#')){
                e.preventDefault();
                document.body.classList.add('fade-exit-active');
                setTimeout(()=> window.location.href = href, 400); // match transition
            }
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


function updateDateTime(){
    const now = new Date();

    const dateOptions = { day: '2-digit', month: 'long', year: 'numeric' };
    const date = now.toLocaleDateString('en-IN', dateOptions);

    const time = now.toLocaleTimeString('en-IN');

    document.getElementById("date").textContent = date;
    document.getElementById("time").textContent = time;
}

setInterval(updateDateTime,1000);
updateDateTime();