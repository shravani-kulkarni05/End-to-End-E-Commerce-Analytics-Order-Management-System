import random
import mysql.connector
from faker import Faker
import sys
import os

# 🔥 Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config import DB_CONFIG, DATA_CONFIG

fake = Faker("en_IN")
random.seed(42)

NUM_PRODUCTS = DATA_CONFIG["num_products"]
NUM_CUSTOMERS = DATA_CONFIG["num_customers"]
NUM_ORDERS = DATA_CONFIG["num_orders"]

# ---------------- DB CONNECTION ----------------
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# ---------------- PRODUCTS ----------------
categories = ["Electronics", "Accessories", "Fashion", "Home", "Furniture"]

for _ in range(NUM_PRODUCTS):
    cursor.execute("""
        INSERT INTO products (product_name, category, price, stock)
        VALUES (%s, %s, %s, %s)
    """, (
        fake.word().capitalize(),
        random.choice(categories),
        random.randint(500, 60000),
        random.randint(10, 300)
    ))

# ---------------- CUSTOMERS ----------------
cities = ["Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad", "Chennai", "Kolkata"]

for _ in range(NUM_CUSTOMERS):
    cursor.execute("""
        INSERT INTO customers (customer_name, email, city, customer_type)
        VALUES (%s, %s, %s, %s)
    """, (
        fake.name(),
        fake.email(),
        random.choice(cities),
        random.choice(["New", "Repeat"])
    ))

# ---------------- ORDERS ----------------
cursor.execute("SELECT customer_id FROM customers")
customer_ids = [row[0] for row in cursor.fetchall()]

order_ids = []

for _ in range(NUM_ORDERS):
    cursor.execute("""
        INSERT INTO orders (customer_id, order_date, order_status, total_amount)
        VALUES (%s, %s, %s, %s)
    """, (
        random.choice(customer_ids),
        fake.date_between(start_date="-6M", end_date="today"),
        random.choice(["Delivered", "Cancelled", "Pending", "Returned"]),
        random.randint(500, 90000)
    ))
    order_ids.append(cursor.lastrowid)

# ---------------- PAYMENTS ----------------
for order_id in order_ids:
    cursor.execute("""
        INSERT INTO payments (order_id, payment_mode, payment_status, payment_date)
        VALUES (%s, %s, %s, %s)
    """, (
        order_id,
        random.choice(["UPI", "Card", "COD", "NetBanking"]),
        random.choice(["Success", "Failed", "Pending"]),
        fake.date_between(start_date="-6M", end_date="today")
    ))

# ---------------- DELIVERY ----------------
for order_id in order_ids:
    status = random.choice(["Delivered", "In Transit", "Cancelled"])
    cursor.execute("""
        INSERT INTO delivery (order_id, delivery_status, delivery_date)
        VALUES (%s, %s, %s)
    """, (
        order_id,
        status,
        fake.date_between(start_date="-6M", end_date="today") if status == "Delivered" else None
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data generated & inserted using config file")
