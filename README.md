# 💊 Pharma Choice - Pharmacy Management System

A full-stack **Pharmacy Management System** developed using **Flask** and **MySQL**. The application provides a secure platform for managing medicines, categories, user accounts, shopping carts, and orders through separate **Admin** and **User** dashboards.

---

## 📌 Project Overview

Pharma Choice is a web-based pharmacy management application that simplifies medicine inventory management and online medicine ordering. It allows administrators to manage medicines, categories, stock, and orders while enabling customers to browse medicines, add them to a cart, and place orders securely.

---

## ✨ Features

### 👨‍💼 Admin Module
- Secure Admin Login
- Dashboard with Pharmacy Statistics
- Add New Medicines
- Update Medicine Details
- Delete Medicines
- Add & Manage Categories
- View Customer Orders
- Inventory Management

### 👤 User Module
- User Registration
- Secure Login Authentication
- Browse Available Medicines
- Search Medicines by Name
- Filter Medicines by Category
- Add Medicines to Cart
- Place Orders
- View Order History

### ⚙️ System Features
- CRUD Operations
- User Authentication
- Session Management
- Responsive User Interface
- Form Validation
- MySQL Database Integration

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Database
- MySQL

### Tools
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```
pharma-choice/
│
├── app.py
├── dbconnection.py
├── dbtransaction.py
│
├── templates/
│
├── static/
│   ├── css/
│   └── js/
│
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nikhilsp780/pharma-choice.git
```

### 2️⃣ Navigate to the Project

```bash
cd pharma-choice
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

Create a database named:

```
pharma_choice_db
```

Update your MySQL credentials in:

```
dbconnection.py
```

### 5️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Login Page

*(Add Screenshot Here)*

### Register Page

*(Add Screenshot Here)*

### Admin Dashboard

*(Add Screenshot Here)*

### Category Management

*(Add Screenshot Here)*

### Medicine Listing

*(Add Screenshot Here)*

### Customer Dashboard

*(Add Screenshot Here)*

---

## 🔐 Authentication

The application provides separate authentication for:

- Admin
- Customers

User sessions are maintained securely using Flask session management.

---

## 🗄️ Database

Database Used:

```
MySQL
```

Main Tables:

- Users
- Categories
- Drugs
- Orders
- Cart

---

## 📈 Future Enhancements

- Online Payment Gateway
- Email Notifications
- Medicine Recommendation System
- Prescription Upload
- REST API
- JWT Authentication
- Sales Analytics Dashboard
- Inventory Alerts
- Cloud Deployment

---

## 👨‍💻 Author

**Nikhil SP**

GitHub:
https://github.com/nikhilsp780

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

Thank you for visiting!
