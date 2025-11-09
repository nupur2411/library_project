# 📚 Library Management System (Django Project)

## 🔍 Overview  
This is a **Django-based Library Management System** that allows users to manage **Books, Authors, and Categories** efficiently.  
It demonstrates CRUD (Create, Read, Update, Delete) operations and integrates Django’s powerful **Admin Panel** for backend management.

---

## ⚙️ Tech Stack  
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (Django Templates)  
- **Database:** SQLite (default)  
- **Tools:** Git, VS Code, Django Admin  

---

## 🧩 Features  
✅ Add, Edit, Delete, and View Books  
✅ Manage Authors and Categories  
✅ Admin Dashboard using Django’s built-in admin  
✅ Simple and clean user interface  
✅ Modular structure for scalability  

---

library_project/
│
├── books/ # App for managing books, authors, and categories
│ ├── models.py # Database models
│ ├── views.py # Handles logic for CRUD operations
│ ├── urls.py # App-level routing
│ ├── templates/ # HTML templates for UI
│
├── library/ # Main project folder
│ ├── settings.py # Project configuration
│ ├── urls.py # Global URL routing
│
├── db.sqlite3 # Database file
├── manage.py # Django management script
└── README.md # Project documentation


---

## 🚀 How to Run the Project

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>


Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate       # For Windows

Install dependencies

pip install django

Run migrations

python manage.py makemigrations

python manage.py migrate

Create a superuser

python manage.py createsuperuser

Start the development server

python manage.py runserver


Visit in browser:
👉 http://127.0.0.1:8000/admin
👉 http://127.0.0.1:8000/books/

🧠 Learning Outcomes
Hands-on experience with Django MVC pattern
Understanding of Django ORM and Models
CRUD functionality using views and templates
Managing Django Admin and authentication

👩‍💻 Author
Nupur Bhargav
Full Stack Developer | Python | Django | React
**GitHub:** [https://github.com/nupurbhargav]
**LinkedIn:** [https://linkedin.com/in/nupurbhargav]


