// Toggle Add Product Form
const toggleFormBtn = document.getElementById('toggleFormBtn');
const addProductForm = document.getElementById('addProductForm');
const productForm = document.getElementById('productForm');
const formBtn = document.getElementById('formBtn');
const cancelBtn = document.getElementById('cancelBtn');

toggleFormBtn.addEventListener('click', () => {
    addProductForm.style.display = 'block';
    productForm.reset();
    formBtn.textContent = 'Add Product';
    document.getElementById('product_id').value = '';
});

cancelBtn.addEventListener('click', () => {
    addProductForm.style.display = 'none';
    productForm.reset();
});

// Edit Button Click
document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', () => {
        const id = button.getAttribute('data-id');
        const name = button.getAttribute('data-name');
        const price = button.getAttribute('data-price');
        const quantity = button.getAttribute('data-quantity');
        const unit = button.getAttribute('data-unit');

        // Fill form with product data
        document.getElementById('product_id').value = id;
        document.getElementById('product_name').value = name;
        document.getElementById('price').value = price;
        document.getElementById('quantity').value = quantity;
        document.getElementById('unit').value = unit;

        formBtn.textContent = 'Update Product';
        addProductForm.style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});


toggleFormBtn.addEventListener('click', () => {
    addProductForm.style.display = 'block';

    if (!document.getElementById('product_id').value) {
        productForm.reset();
        formBtn.textContent = 'Add Product';
    }
});
const productSearch = document.getElementById("productSearch");

productSearch.addEventListener("keyup", function(){

    let filter = productSearch.value.toLowerCase();
    let table = document.getElementById("productTable");
    let rows = table.getElementsByTagName("tr");

    for(let i=1;i<rows.length;i++){

        let nameCell = rows[i].getElementsByTagName("td")[1];

        if(nameCell){

            let text = nameCell.textContent.toLowerCase();

            if(text.includes(filter)){
                rows[i].style.display="";
            }
            else{
                rows[i].style.display="none";
            }

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