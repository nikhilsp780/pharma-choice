# 💊 Pharma Choice - Pharmacy Management System

A full-stack Pharmacy Management System developed using **Flask** and **MySQL**, featuring secure user authentication, medicine inventory management, category management, shopping cart, and order tracking with a responsive web interface.

![Pharma Choice](https://img.shields.io/badge/Flask-2.0+-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [License](#license)

---

## ✨ Features

### 👑 Admin Module
- Secure admin login and authentication
- Add, view, update, and delete medicines (CRUD operations)
- Manage medicine categories
- Track stock availability
- Update order status (Placed → Shipped → Delivered)
- Dashboard with overview statistics

### 👤 User Module
- User registration and secure login
- Browse medicines by category
- Search medicines by name or category
- Add medicines to shopping cart
- View and manage cart items
- Place orders with total price calculation
- Track order status in real-time

### 🛒 Cart & Order Management
- Dynamic cart with quantity management
- Automatic price calculation with discounts
- Order history and status tracking
- Transaction handling for data consistency

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Flask (Python) |
| **Database** | MySQL 8.0+ |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Templating** | Jinja2 |
| **Session Management** | Flask-Session |
| **Database Connector** | PyMySQL / MySQL-connector-python |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/nikhilsp780/pharma-choice.git
cd pharma-choice
