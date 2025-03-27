# E-Commerce Website using Django

## 📌 Overview
This is a fully functional e-commerce website built using Django, providing users with a seamless online shopping experience. The platform allows users to browse products, add them to their cart, place orders.

## 🚀 Features
- User authentication (Sign Up, Login, Logout)
- Product listing and categorization
- Shopping cart and order management
- Responsive UI with HTML, CSS, and JavaScript
- Admin panel for product and order management
- Database optimization using SQL

## 🛠️ Tech Stack
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQL

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
  git clone https://github.com/sparksyntax/ecommerce-django.git
  cd ecommerce-django
```

### 2️⃣ Create a Virtual Environment
```bash
  python -m venv venv
  source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
  pip install -r requirements.txt
```

### 4️⃣ Configure Database
- Update **settings.py** to set up your database configurations.
- Apply migrations:
```bash
  python manage.py migrate
```

### 5️⃣ Create Superuser (Admin Panel)
```bash
  python manage.py createsuperuser
```

### 6️⃣ Run the Server
```bash
  python manage.py runserver
```
Access the website at **http://127.0.0.1:8000/**.

## 🎯 Project Structure
```
📂 ecommerce-django
│-- 📂 ecommerce   # Main Django project
│-- 📂 store       # E-commerce app
│-- 📂 templates   # HTML Templates
│-- 📂 static      # CSS, JavaScript, Images
│-- manage.py      # Django CLI tool
│-- requirements.txt  # Required packages
```

## 🎉 Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!
