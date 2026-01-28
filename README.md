🛒 E-Commerce Sales & Order Management System

An end-to-end data analytics project that demonstrates how e-commerce data can be generated, stored, and analyzed using Python, MySQL, and Power BI.

This project follows industry-style architecture with proper configuration management, relational database design, and interactive dashboards.

📌 Project Overview

The goal of this project is to analyze:

Sales performance

Customer behavior

Payment success rates

Delivery efficiency

The system uses:

Python for data generation and ETL

MySQL as the relational database

Power BI for analytics and visualization

🧱 Project Architecture
Python  →  MySQL  →  Power BI


Python generates realistic transactional data and inserts it into MySQL.

MySQL stores normalized relational data with foreign key constraints.

Power BI connects to MySQL and provides interactive dashboards using DAX.


🗄️ Database Design
Tables Used

products

customers

orders

payments

delivery

Relationships

One customer → many orders

One order → one payment

One order → one delivery

This follows a star schema–like design, optimized for analytics.

🐍 Python Usage

Python is used as the data engineering layer.

Key Responsibilities:

Generate realistic dummy data using faker

Insert data directly into MySQL

Maintain foreign key integrity

Handle NULL values and constraints

Centralize configuration using config.py

⚙️ Configuration Management

All database credentials and record counts are stored in:

config/config.py


This avoids hardcoding and makes the project scalable and secure.

Example:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "********",
    "database": "ecommerce_db"
}

📊 Power BI Dashboard

The Power BI report contains 3 pages:

1️⃣ Sales Overview

Total Revenue

Total Orders

Delivery Rate %

Revenue trends over time

Orders by city and status

2️⃣ Customer Insights

Total, New, and Repeat customers

Customer distribution by city

Top customers by revenue

3️⃣ Payment & Delivery

Payment success vs failure

Payment mode distribution

Delivery status analysis

All visuals are fully interactive using slicers.

📐 DAX Measures

Key KPIs created using DAX:

Total Revenue

Total Orders

Average Order Value

Delivered Orders

Delivery Rate %

Successful & Failed Payments

New vs Repeat Customers

▶ How to Run the Project
1️⃣ Activate Virtual Environment
.venv\Scripts\activate

2️⃣ Generate & Insert Data
python scripts/generate_and_insert_data.py

3️⃣ Open Dashboard

Open dashboard/Ecommerce_PowerBI_Dashboard.pbix

Refresh data in Power BI

🧠 Key Learnings

Relational database design with foreign keys

ETL pipelines using Python

Handling NULL values and constraints

Power BI data modeling and DAX

Building business-oriented dashboards
