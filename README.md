🚗 CarDeal Project

A Django + PostgreSQL project for managing Customers, Products, Orders, and Shippers, with REST APIs and web views.

📌 Features

🔑 User Authentication → Register, Login, Logout.

📊 Analytics Dashboard → Dropdown menus for 10 SQL-based queries.

🌐 REST APIs (CRUD) → Implemented with Django REST Framework.

CRUD for Customers, Products, Orders, Shippers (Task required 2, completed 4 ✅).

💾 Database → PostgreSQL integrated & monitored with DBeaver.

🎨 Frontend → Bootstrap templates for Customers, Products, Orders, Shippers listing.

📂 Project Structure
main_project/
│── accounts/          # Authentication (login, register, logout)
│── customer/          # Customer model, views, serializers, API
│── product/           # Product model, views, serializers, API
│── order/             # Order model, views, serializers, API
│── shipper/           # Shipper model, views, serializers, API
│── reports_app/       # Analytics dropdown queries
│── templates/         # HTML templates (base, login, tables, analytics)
│── static/            # CSS/JS assets

⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/cardeal.git
cd cardeal

2. Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)

3. Install Requirements
pip install -r requirements.txt

4. Database Setup (PostgreSQL)

Update settings.py with your DB credentials:

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'cardeal_db',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}


Run migrations:

python manage.py makemigrations
python manage.py migrate

5. Create Superuser
python manage.py createsuperuser

6. Run Server
python manage.py runserver


Open → http://127.0.0.1:8000/

🔗 API Endpoints (via DRF)
Entity	Method	Endpoint	Description
Customers	GET	/api/customers/	List all customers
	POST	/api/customers/	Create new customer
	GET	/api/customers/{id}/	Retrieve customer by ID
	PUT	/api/customers/{id}/	Update customer
	DELETE	/api/customers/{id}/	Delete customer
Products	(same)	/api/products/	CRUD for products
Orders	(same)	/api/orders/	CRUD for orders
Shippers	(same)	/api/shippers/	CRUD for shippers
📑 API Documentation

Documented in Postman collection (Task 2 deliverable).

Includes at least 5 endpoints across Customers & Products (requirement ✅).

Status codes and JSON responses verified.

✅ Success Metrics

 Backend runs without errors

 Database connected in PostgreSQL/DBeaver

 REST APIs working (CRUD tested in Postman)

 User login/logout working

 Analytics queries implemented in dropdowns
