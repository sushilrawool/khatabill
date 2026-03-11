from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash, send_file
import mysql.connector
import pdfkit
import pandas as pd
import io
from fpdf import FPDF

from flask import send_file
import pandas as pd
from io import BytesIO

from fpdf import FPDF
import csv
from fpdf import FPDF
from datetime import datetime


import os
from fpdf import FPDF

import os
import pdfkit




def init_unicode_pdf():
    pdf = FPDF()
    pdf.add_page()
    font_path = os.path.join(os.getcwd(), 'fonts', 'segoeui.ttf')
    pdf.add_font("Segoe", "", font_path, uni=True)
    pdf.add_font("Segoe", "B", font_path, uni=True)
    pdf.set_font("Segoe", "", 10)
    return pdf

    # Windows system font path (NO DOWNLOAD)
    font_path = os.path.join(os.getcwd(), 'fonts', 'segoeui.ttf')
    pdf.add_font("Segoe", "", font_path, uni=True)
    
    pdf.add_font("Segoe", "", font_path, uni=True)
    pdf.add_font("Segoe", "B", font_path, uni=True)
    pdf.set_font("Segoe", "", 10)

    return pdf

app = Flask(__name__)
app.secret_key = "khatabill_secret_key"
import os
app.secret_key = os.environ.get("SECRET_KEY", "fallback_secret_key")

@app.template_filter('datetimeformat')
def datetimeformat(value, format="%d-%m-%Y %H:%M"):
    if value:
        return value.strftime(format)
    return ""


from fpdf import FPDF

def init_unicode_pdf():
    pdf = FPDF()
    pdf.add_page()

    # Windows default Unicode font (already present)
    font_path = r"C:\Windows\Fonts\segoeui.ttf"

    pdf.add_font("Segoe", "", font_path, uni=True)
    pdf.add_font("Segoe", "B", font_path, uni=True)
    pdf.set_font("Segoe", "", 10)

    return pdf



def pdf_safe(value):
    if value is None:
        return ""
    return str(value)

# ---------------- NO CACHE ----------------
@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# ---------------- DB CONNECTION ----------------
import mysql.connector
import os

import mysql.connector
import os

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("MYSQLHOST"),
<<<<<<< HEAD
            user=os.environ.get("MYSQLUSER"),
            password=os.environ.get("MYSQLPASSWORD"),
            database=os.environ.get("MYSQLDATABASE"),
            port=int(os.environ.get("MYSQLPORT", 3306))
        )
        return conn
    except mysql.connector.Error as err:
        # Print the error to console/logs
        print("Database connection failed:", err)
        raise

=======
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database=os.environ.get("MYSQL_DATABASE"),
            port=int(os.environ.get("MYSQL_PORT", 3306))
        )
        return conn
    except mysql.connector.Error as err:
        print(f"[DB CONNECTION ERROR] {err}")
        return None
        return conn
    except mysql.connector.Error as err:
        print(f"[DB CONNECTION ERROR] {err}")
        return None  # Don't crash Flask, return None
>>>>>>> 09d2c6b (Initial commit)
def db_fetch(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or [])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def db_fetch_customer_summary(customer_id=None, from_date=None, to_date=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT c.name, COUNT(b.id) as total_bills, 
               SUM(CASE WHEN b.status='PENDING' THEN b.total_amount ELSE 0 END) as total_pending,
               SUM(CASE WHEN b.status='PAID' THEN b.total_amount ELSE 0 END) as total_paid
        FROM customers c
        LEFT JOIN bills b ON c.id = b.customer_id
        WHERE 1=1
    """
    params = []
    if customer_id:
        query += " AND c.id=%s"
        params.append(customer_id)
    if from_date:
        query += " AND b.date >= %s"
        params.append(from_date)
    if to_date:
        query += " AND b.date <= %s"
        params.append(to_date)
    query += " GROUP BY c.id"
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
# ---------------- LOGIN ----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '1234':
            session['user'] = username
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM customers")
    total_customers = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) AS total FROM bills")
    total_bills = cursor.fetchone()['total']

    cursor.execute("SELECT IFNULL(SUM(total_amount),0) AS total FROM bills WHERE status='Pending'")
    total_pending_amount = cursor.fetchone()['total']

    cursor.execute("SELECT IFNULL(SUM(total_amount),0) AS total FROM bills WHERE status='Paid' AND DATE(created_at) = CURDATE()")
    todays_collection = cursor.fetchone()['total']

    cursor.execute("""
        SELECT c.name AS customer_name, b.total_amount AS amount, b.status
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        WHERE DATE(b.created_at) = CURDATE()
        ORDER BY b.id DESC
    """)
    todays_bills = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('dashboard.html',
                           username=session['user'],
                           total_customers=total_customers,
                           total_bills=total_bills,
                           total_pending_amount=total_pending_amount,
                           todays_collection=todays_collection,
                           todays_bills=todays_bills)

# ---------------- ADD CUSTOMER ----------------
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        opening_balance = request.form.get('opening_balance') or 0

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customers (name, phone, email, address, opening_balance) VALUES (%s,%s,%s,%s,%s)",
            (name, phone, email, address, opening_balance)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Customer added successfully!", "success")
        return redirect(url_for('add_customer'))

    return render_template('add_customer.html')

# ---------------- VIEW CUSTOMERS ----------------
@app.route('/view_customers')
def view_customers():
    if 'user' not in session:
        return redirect(url_for('login'))

    search = request.args.get('search', '')
    updated_id = request.args.get('updated_id', type=int)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        c.*,
        COUNT(b.id) AS total_bills,
        SUM(CASE WHEN b.status='PENDING' THEN 1 ELSE 0 END) AS pending_bills,
        IFNULL(
            SUM(CASE WHEN b.status='PENDING' THEN b.total_amount ELSE 0 END),
            0
        ) AS pending_amount
    FROM customers c
    LEFT JOIN bills b ON c.id = b.customer_id
    WHERE c.name LIKE %s OR c.phone LIKE %s
    GROUP BY c.id
    ORDER BY c.name ASC
    """

    cursor.execute(query, (f"%{search}%", f"%{search}%"))
    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'view_customers.html',
        customers=customers,
        updated_id=updated_id,
        search=search
    )

# ---------------- CUSTOMER DETAIL ----------------
@app.route('/customer/<int:customer_id>')
def customer_detail(customer_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers WHERE id=%s", (customer_id,))
    customer = cursor.fetchone()

    cursor.execute("SELECT * FROM bills WHERE customer_id=%s ORDER BY created_at DESC", (customer_id,))
    bills = cursor.fetchall()
    

    cursor.close()
    conn.close()
    return render_template('customer_detail.html', customer=customer, bills=bills)




# ---------------- EDIT BILL ----------------
@app.route('/edit_bill/<int:bill_id>', methods=['GET', 'POST'])
def edit_bill(bill_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM bills WHERE id=%s AND status='PENDING'", (bill_id,))
    bill = cursor.fetchone()
    if not bill:
        flash("Bill not found or already paid!", "error")
        return redirect(url_for('dashboard'))

    cursor.execute("SELECT * FROM bill_items WHERE bill_id=%s", (bill_id,))
    items = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    products_dict = {p["id"]: p for p in products}

    if request.method == 'POST':
        product_ids = request.form.getlist('product_id[]')
        qtys = request.form.getlist('quantity[]')
        prices = request.form.getlist('price[]')

        if not (len(product_ids) == len(qtys) == len(prices)):
            flash("Mismatched product data!", "error")
            return redirect(url_for('edit_bill', bill_id=bill_id))

        total_amount = sum(int(qtys[i]) * float(prices[i]) for i in range(len(product_ids)))

        cursor.execute("UPDATE bills SET total_amount=%s WHERE id=%s", (total_amount, bill_id))
        cursor.execute("DELETE FROM bill_items WHERE bill_id=%s", (bill_id,))

        for i in range(len(product_ids)):
            pid = int(product_ids[i])
            cursor.execute("""
                INSERT INTO bill_items (bill_id, product_id, product_name, quantity, price, unit)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (
                bill_id,
                pid,
                products_dict[pid]["product_name"],
                int(qtys[i]),
                float(prices[i]),
                products_dict[pid]["unit"]
            ))

        conn.commit()
        flash("Bill updated successfully!", "success")
        cursor.close()
        conn.close()
        return redirect(url_for('view_bill', bill_id=bill_id))

    cursor.close()
    conn.close()
    
    return render_template('edit_bill.html', bill=bill, items=items, products=products)

# ---------------- DELETE CUSTOMER ----------------
@app.route('/delete_customer/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id=%s", (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_customers'))

# ---------------- ADD / UPDATE CUSTOMER ----------------
@app.route('/add_update_customer', methods=['POST'])
def add_update_customer():
    if 'user' not in session:
        return redirect(url_for('login'))

    customer_id = request.form.get('customer_id')
    name = request.form.get('customer_name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()

    if customer_id:
        cursor.execute("UPDATE customers SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, customer_id))
    else:
        cursor.execute("INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        customer_id = cursor.lastrowid

    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_customers', updated_id=customer_id))

# ---------------- PRODUCTS ----------------
@app.route('/products', methods=['GET', 'POST'])
def products():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        product_id = request.form.get('product_id')
        name = request.form.get('product_name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        unit = request.form.get('unit')

        if product_id:
            cursor.execute("UPDATE products SET product_name=%s, price=%s, quantity=%s, unit=%s WHERE id=%s",
                           (name, price, quantity, unit, product_id))
        else:
            cursor.execute("INSERT INTO products (product_name, price, quantity, unit) VALUES (%s,%s,%s,%s)",
                           (name, price, quantity, unit))

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('products'))

    cursor.execute("SELECT * FROM products ORDER BY id")
    products_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('products.html', products=products_list)

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('products'))

# ---------------- ADD BILL ----------------
@app.route('/add_bill', methods=['GET', 'POST'])
def add_bill():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        customer_id = request.form.get('customer_id')
        status = request.form.get('status')
        product_ids = request.form.getlist('product_id[]')
        qtys = request.form.getlist('quantity[]')
        prices = request.form.getlist('price[]')

        if not customer_id or not product_ids or not all(product_ids):
            cursor.close()
            conn.close()
            return render_template('add_bill.html', customers=fetch_customers(),
                                   products=fetch_products(), error="Select valid customer/products!")

        total_amount = sum(int(qtys[i]) * float(prices[i]) for i in range(len(product_ids)))

        cursor.execute("INSERT INTO bills (customer_id, total_amount, status) VALUES (%s,%s,%s)",
                       (customer_id, total_amount, status))
        bill_id = cursor.lastrowid

        products = fetch_products()
        products_dict = {p["id"]: p for p in products}

        for i in range(len(product_ids)):
            pid = int(product_ids[i])
            cursor.execute("""
                INSERT INTO bill_items
                (bill_id, product_id, product_name, quantity, price, unit)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (bill_id, pid, products_dict[pid]["product_name"], qtys[i], prices[i], products_dict[pid]["unit"]))

        conn.commit()
        cursor.close()
        conn.close()
        flash("Bill saved successfully!", "success")
        return redirect(url_for('view_bill', bill_id=bill_id))

    return render_template('add_bill.html', customers=fetch_customers(), products=fetch_products())

# ---------------- HELPERS ----------------
def fetch_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM customers ORDER BY name")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return customers

def fetch_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, product_name, price, unit FROM products ORDER BY id")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

# ---------------- VIEW / DOWNLOAD BILL ----------------
@app.route('/bill/<int:bill_id>')
def view_bill(bill_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT b.*, c.name AS customer_name
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        WHERE b.id = %s
    """, (bill_id,))
    bill = cursor.fetchone()

    cursor.execute("""
        SELECT bi.*, p.product_name
        FROM bill_items bi
        JOIN products p ON bi.product_id = p.id
        WHERE bi.bill_id = %s
    """, (bill_id,))
    items = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('view_bill.html', bill=bill, items=items)

@app.route('/download_bill/<int:bill_id>')
def download_bill(bill_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT b.*, c.name AS customer_name
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        WHERE b.id = %s
    """, (bill_id,))
    bill = cursor.fetchone()
    if not bill:
        return "Bill not found", 404

    cursor.execute("""
        SELECT bi.*, p.product_name
        FROM bill_items bi
        JOIN products p ON bi.product_id = p.id
        WHERE bi.bill_id = %s
    """, (bill_id,))
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    rendered = render_template('bill_pdf.html', bill=bill, items=items)
    WKHTML_PATH = os.environ.get('WKHTMLTOPDF_PATH', '/usr/local/bin/wkhtmltopdf')
    config = pdfkit.configuration(wkhtmltopdf=WKHTML_PATH)
    options = {'enable-local-file-access': None}
    pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename=bill_{bill_id}.pdf'
    return response

# ---------------- PENDING / MARK PAID ----------------
@app.route('/pending_bills')
def pending_bills():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT b.id, c.name AS customer_name, b.total_amount, b.status, b.created_at
        FROM bills b
        JOIN customers c ON b.customer_id=c.id
        WHERE b.status='PENDING'
        ORDER BY b.id DESC
    """)
    pending = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('pending_bills.html', pending_bills=pending)

@app.route('/mark_paid/<int:bill_id>')
def mark_paid(bill_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE bills SET status = 'PAID' WHERE id=%s", (bill_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('pending_bills'))

# ---------------- REPORTS PAGE ----------------
@app.route('/reports', methods=['GET'])
def reports():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template("reports.html")

# ---------------- BILL REPORT ----------------
@app.route('/bill_report', methods=['GET'])
def bill_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    # ----------- FILTERS -----------
    customer_id = request.args.get('customer_id')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    download = request.args.get('download')  # excel / pdf

    # ----------- BILL LIST -----------
    query = """
        SELECT b.id, c.name AS customer_name, b.created_at,
               b.total_amount, b.status
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        WHERE 1=1
    """
    params = []

    if customer_id:
        query += " AND b.customer_id=%s"
        params.append(customer_id)

    if from_date:
        query += " AND DATE(b.created_at) >= %s"
        params.append(from_date)

    if to_date:
        query += " AND DATE(b.created_at) <= %s"
        params.append(to_date)

    query += " ORDER BY b.created_at DESC"
    bills = db_fetch(query, params)

    # ----------- CUSTOMER SUMMARY -----------
    cust_query = """
        SELECT c.name,
               COUNT(b.id) AS total_bills,
               IFNULL(SUM(CASE WHEN b.status='PENDING' THEN b.total_amount END),0) AS total_pending,
               IFNULL(SUM(CASE WHEN b.status='PAID' THEN b.total_amount END),0) AS total_paid
        FROM customers c
        LEFT JOIN bills b ON c.id=b.customer_id
        GROUP BY c.id
    """
    customer_reports = db_fetch(cust_query)

    # ----------- TOTAL CARDS -----------
    total_customers = db_fetch("SELECT COUNT(*) cnt FROM customers")[0]['cnt']
    total_bills = db_fetch("SELECT COUNT(*) cnt FROM bills")[0]['cnt']
    total_pending = db_fetch(
        "SELECT IFNULL(SUM(total_amount),0) total FROM bills WHERE status='PENDING'"
    )[0]['total']
    total_collection = db_fetch(
        "SELECT IFNULL(SUM(total_amount),0) total FROM bills WHERE status='PAID'"
    )[0]['total']

    total_sales = total_pending + total_collection

    # ----------- EXCEL DOWNLOAD -----------
    if download == 'excel':
        df = pd.DataFrame(bills)
        if not bills:
             df = pd.DataFrame(columns=['id', 'customer_name', 'created_at', 'total_amount', 'status'])
        else:
             df = df[['id', 'customer_name', 'created_at', 'total_amount', 'status']]
        df.columns = ['Bill ID', 'Customer', 'Date', 'Amount', 'Status']

        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)

        return send_file(
            output,
            download_name="bill_report.xlsx",
            as_attachment=True
        )

    # ----------- PDF DOWNLOAD -----------
    if download == 'pdf':
        pdf = init_unicode_pdf()
        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Bill Report", ln=True, align="C")
        pdf.ln(8)

        pdf.set_font("Segoe", "B", 11)
        headers = ["ID", "Customer", "Date", "Amount", "Status"]
        widths = [15, 45, 30, 30, 30]

        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "", 11)
        for b in bills:
            pdf.cell(15, 8, str(b['id']), 1)
            pdf.cell(45, 8, str(b['customer_name']), 1)
            pdf.cell(30, 8, b['created_at'].strftime('%Y-%m-%d'), 1)
            pdf.cell(30, 8, f"₹ {b['total_amount']}", 1)
            pdf.cell(30, 8, str(b['status']), 1)
            pdf.ln()

        return send_file(
            BytesIO(pdf.output(dest='S')),
            download_name="bill_report.pdf",
            as_attachment=True,
            mimetype='application/pdf'
        )

    # ----------- PAGE RENDER -----------
    customers = db_fetch("SELECT id, name FROM customers ORDER BY name")

    return render_template(
        "bill_report.html",
        bills=bills,
        customers=customers
    )

# ---------------- CUSTOMER REPORT ----------------
@app.route('/customer_report', methods=['GET'])
def customer_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    download = request.args.get('download')
    
    query = """
        SELECT c.id, c.name, c.phone, c.email, c.address, 
               IFNULL(SUM(CASE WHEN b.status='PENDING' THEN b.total_amount ELSE 0 END), 0) AS pending_amount,
               IFNULL(SUM(CASE WHEN b.status='PAID' THEN b.total_amount ELSE 0 END), 0) AS paid_amount
        FROM customers c
        LEFT JOIN bills b ON c.id = b.customer_id
        GROUP BY c.id
        ORDER BY c.name
    """
    customers = db_fetch(query)

    if download == 'excel':
        df = pd.DataFrame(customers)
        df.columns = ['ID', 'Name', 'Phone', 'Email', 'Address', 'Pending Amount', 'Paid Amount']
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="customer_report.xlsx", as_attachment=True)

    if download == 'pdf':
        pdf = init_unicode_pdf()
        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Customer Report", ln=True, align="C")
        pdf.ln(8)

        headers = ["ID", "Name", "Phone", "Pending", "Paid"]
        widths = [15, 50, 30, 25, 25]

        pdf.set_font("Segoe", "B", 10)
        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "", 10)
        for c in customers:
            pdf.cell(15, 8, str(c['id']), 1)
            pdf.cell(50, 8, str(c['name']), 1)
            pdf.cell(30, 8, str(c['phone']), 1)
            pdf.cell(25, 8, f"₹ {c['pending_amount']}", 1)
            pdf.cell(25, 8, f"₹ {c['paid_amount']}", 1)
            pdf.ln()

        return send_file(BytesIO(pdf.output(dest='S')), download_name="customer_report.pdf", as_attachment=True, mimetype='application/pdf')

    return render_template("customer_report.html", customers=customers)

# ---------------- PENDING BILLS REPORT ----------------
@app.route('/pending_bills_report', methods=['GET'])
def pending_bills_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    download = request.args.get('download')
    
    query = """
        SELECT b.id, c.name AS customer_name, b.created_at, b.total_amount
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        WHERE b.status = 'PENDING'
        ORDER BY b.created_at DESC
    """
    bills = db_fetch(query)

    total_pending = sum(b['total_amount'] for b in bills)

    if download == 'excel':
        df = pd.DataFrame(bills)
        if not bills:
             df = pd.DataFrame(columns=['id', 'customer_name', 'created_at', 'total_amount'])
        df.columns = ['Bill ID', 'Customer', 'Date', 'Amount']
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="pending_bills_report.xlsx", as_attachment=True)

    if download == 'pdf':
        pdf = init_unicode_pdf()
        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Pending Bills Report", ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("Segoe", "", 11)
        pdf.cell(0, 8, f"Total Pending Amount: ₹ {total_pending}", ln=True)
        pdf.ln(5)

        headers = ["Bill ID", "Customer", "Date", "Amount"]
        widths = [20, 60, 40, 30]

        pdf.set_font("Segoe", "B", 11)
        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "", 11)
        for b in bills:
            pdf.cell(20, 8, str(b['id']), 1)
            pdf.cell(60, 8, str(b['customer_name']), 1)
            pdf.cell(40, 8, b['created_at'].strftime('%Y-%m-%d'), 1)
            pdf.cell(30, 8, f"₹ {b['total_amount']}", 1)
            pdf.ln()

        return send_file(BytesIO(pdf.output(dest='S')), download_name="pending_bills_report.pdf", as_attachment=True, mimetype='application/pdf')

    return render_template("pending_bills_report.html", bills=bills, total_pending=total_pending)

# ---------------- PAYMENT REPORT ----------------
@app.route('/payment_report', methods=['GET'])
def payment_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    download = request.args.get('download')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    query = """
        SELECT b.id, c.name AS customer_name, b.created_at, b.total_amount
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        WHERE b.status = 'PAID'
    """
    params = []
    if from_date:
        query += " AND DATE(b.created_at) >= %s"
        params.append(from_date)
    if to_date:
        query += " AND DATE(b.created_at) <= %s"
        params.append(to_date)
        
    query += " ORDER BY b.created_at DESC"
    bills = db_fetch(query, params)

    total_paid = sum(b['total_amount'] for b in bills)

    if download == 'excel':
        df = pd.DataFrame(bills)
        if not bills:
             df = pd.DataFrame(columns=['id', 'customer_name', 'created_at', 'total_amount'])
        df.columns = ['Bill ID', 'Customer', 'Date', 'Amount']
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="payment_report.xlsx", as_attachment=True)

    if download == 'pdf':
        pdf = init_unicode_pdf()
        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Payment Report", ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("Segoe", "", 11)
        pdf.cell(0, 8, f"Total Payments: ₹ {total_paid}", ln=True)
        pdf.ln(5)

        headers = ["Bill ID", "Customer", "Date", "Amount"]
        widths = [20, 60, 40, 30]

        pdf.set_font("Segoe", "B", 11)
        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "", 11)
        for b in bills:
            pdf.cell(20, 8, str(b['id']), 1)
            pdf.cell(60, 8, str(b['customer_name']), 1)
            pdf.cell(40, 8, b['created_at'].strftime('%Y-%m-%d'), 1)
            pdf.cell(30, 8, f"₹ {b['total_amount']}", 1)
            pdf.ln()

        return send_file(BytesIO(pdf.output(dest='S')), download_name="payment_report.pdf", as_attachment=True, mimetype='application/pdf')

    return render_template("payment_report.html", bills=bills, total_paid=total_paid)

# ---------------- SALES REPORT ----------------
@app.route('/sales_report', methods=['GET'])
def sales_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    download = request.args.get('download')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    # Aggregate sales by date
    query = """
        SELECT DATE(created_at) AS sale_date,
               COUNT(*) AS total_bills,
               SUM(CASE WHEN status='PAID' THEN total_amount ELSE 0 END) AS collected,
               SUM(CASE WHEN status='PENDING' THEN total_amount ELSE 0 END) AS pending,
               SUM(total_amount) AS total_sales
        FROM bills
        WHERE 1=1
    """
    params = []
    if from_date:
        query += " AND DATE(created_at) >= %s"
        params.append(from_date)
    if to_date:
        query += " AND DATE(created_at) <= %s"
        params.append(to_date)
        
    query += " GROUP BY DATE(created_at) ORDER BY sale_date DESC"
    sales = db_fetch(query, params)
    
    grand_total = sum(s['total_sales'] for s in sales)
    grand_collected = sum(s['collected'] for s in sales)
    grand_pending = sum(s['pending'] for s in sales)

    if download == 'excel':
        df = pd.DataFrame(sales)
        if not sales:
             df = pd.DataFrame(columns=['sale_date', 'total_bills', 'collected', 'pending', 'total_sales'])
        df.columns = ['Date', 'Total Bills', 'Collected (₹)', 'Pending (₹)', 'Total Sales (₹)']
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="sales_report.xlsx", as_attachment=True)

    if download == 'pdf':
        pdf = init_unicode_pdf()
        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Sales Report", ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("Segoe", "", 11)
        pdf.cell(0, 8, f"Total Sales: ₹ {grand_total}", ln=True)
        pdf.cell(0, 8, f"Total Collected: ₹ {grand_collected}", ln=True)
        pdf.cell(0, 8, f"Total Pending: ₹ {grand_pending}", ln=True)
        pdf.ln(5)

        headers = ["Date", "Bills", "Collected", "Pending", "Total Sales"]
        widths = [35, 20, 30, 30, 35]

        pdf.set_font("Segoe", "B", 11)
        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "", 11)
        for s in sales:
            pdf.cell(35, 8, str(s['sale_date']), 1)
            pdf.cell(20, 8, str(s['total_bills']), 1)
            pdf.cell(30, 8, f"₹ {s['collected']}", 1)
            pdf.cell(30, 8, f"₹ {s['pending']}", 1)
            pdf.cell(35, 8, f"₹ {s['total_sales']}", 1)
            pdf.ln()

        return send_file(BytesIO(pdf.output(dest='S')), download_name="sales_report.pdf", as_attachment=True, mimetype='application/pdf')

    return render_template(
        "sales_report.html", 
        sales=sales,
        grand_total=grand_total,
        grand_collected=grand_collected,
        grand_pending=grand_pending
    )





# ---------------- PRODUCT REPORT ----------------
@app.route('/product_report', methods=['GET'])
def product_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    download = request.args.get('download')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    product_id = request.args.get('product_id')

    query = """
        SELECT 
            bi.product_name,
            bi.unit,
            bi.price,
            SUM(bi.quantity) AS total_quantity,
            SUM(bi.quantity * bi.price) AS total_sale
        FROM bill_items bi
        JOIN bills b ON bi.bill_id = b.id
        WHERE b.status='PAID'
    """
    params = []

    if product_id:
        query += " AND bi.product_id=%s"
        params.append(product_id)
    if from_date:
        query += " AND DATE(b.created_at) >= %s"
        params.append(from_date)
    if to_date:
        query += " AND DATE(b.created_at) <= %s"
        params.append(to_date)

    query += " GROUP BY bi.product_id, bi.product_name, bi.unit, bi.price"
    records = db_fetch(query, params)

    grand_total = sum(r['total_sale'] for r in records)

    # ---------- EXCEL ----------
    if download == 'excel':
        df = pd.DataFrame(records)
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="product_report.xlsx", as_attachment=True)

    # ---------- PDF (SEGEO UI – NO LATIN1, NO DEJAVU) ----------
    if download == 'pdf':
        pdf = init_unicode_pdf()

        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Product Sales Report", ln=True, align="C")
        pdf.ln(5)

        pdf.set_font("Segoe", "", 11)
        pdf.cell(0, 8, f"Grand Total Sale : ₹ {grand_total}", ln=True)
        pdf.ln(5)

        headers = ["Product", "Unit", "Price", "Qty Sold", "Total Sale"]
        widths = [50, 20, 25, 25, 30]

        pdf.set_font("Segoe", "B", 10)
        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "", 10)
        for r in records:
            pdf.cell(50, 8, str(r['product_name']), 1)
            pdf.cell(20, 8, str(r['unit']), 1)
            pdf.cell(25, 8, f"₹ {r['price']}", 1)
            pdf.cell(25, 8, str(r['total_quantity']), 1)
            pdf.cell(30, 8, f"₹ {r['total_sale']}", 1)
            pdf.ln()

        return send_file(
            BytesIO(pdf.output(dest='S')),
            download_name="product_report.pdf",
            as_attachment=True,
            mimetype="application/pdf"
        )

    products = db_fetch("SELECT id, product_name FROM products")
    return render_template("product_report.html", records=records, products=products)




# ---------------- CUSTOMER PRODUCT REPORT ----------------
@app.route('/customer_product_report', methods=['GET'])
def customer_product_report():
    if 'user' not in session:
        return redirect(url_for('login'))

    download = request.args.get('download')
    customer_id = request.args.get('customer_id')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    query = """
        SELECT 
            c.name AS customer_name,
            b.id AS bill_id,
            DATE(b.created_at) AS bill_date,
            bi.product_name,
            bi.unit,
            bi.price,
            bi.quantity,
            (bi.quantity * bi.price) AS total_amount
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        JOIN bill_items bi ON bi.bill_id = b.id
        WHERE 1=1
    """
    params = []

    if customer_id:
        query += " AND c.id=%s"
        params.append(customer_id)
    if from_date:
        query += " AND DATE(b.created_at) >= %s"
        params.append(from_date)
    if to_date:
        query += " AND DATE(b.created_at) <= %s"
        params.append(to_date)

    records = db_fetch(query, params)

    # ---------- EXCEL ----------
    if download == 'excel':
        df = pd.DataFrame(records)
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="customer_product_report.xlsx", as_attachment=True)

    # ---------- PDF (UNICODE SAFE) ----------
    if download == 'pdf':
        pdf = init_unicode_pdf()

        pdf.set_font("Segoe", "B", 16)
        pdf.cell(0, 10, "Customer Wise Product Report", ln=True, align="C")
        pdf.ln(5)

        headers = ["Customer", "Bill", "Date", "Product", "Qty", "Price", "Total"]
        widths = [35, 15, 22, 40, 15, 20, 25]

        pdf.set_font("Segoe", "B", 9)
        for i in range(len(headers)):
            pdf.cell(widths[i], 8, headers[i], 1)
        pdf.ln()

        pdf.set_font("Segoe", "B", 9)
        for r in records:
            pdf.cell(35, 8, str(r['customer_name']), 1)
            pdf.cell(15, 8, str(r['bill_id']), 1)
            pdf.cell(22, 8, str(r['bill_date']), 1)
            pdf.cell(40, 8, str(r['product_name']), 1)
            pdf.cell(15, 8, str(r['quantity']), 1)
            pdf.cell(20, 8, f"₹ {r['price']}", 1)
            pdf.cell(25, 8, f"₹ {r['total_amount']}", 1)
            pdf.ln()

        return send_file(
            BytesIO(pdf.output(dest='S')),
            download_name="customer_product_report.pdf",
            as_attachment=True,
            mimetype="application/pdf"
        )

    customers = db_fetch("SELECT id, name FROM customers")
    return render_template("customer_product_report.html", records=records, customers=customers)








# ---------------- LOGOUT / STATIC PAGES ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


