import pandas as pd
import mysql.connector
import os
import sys

# -------------------------------------------------
# Add project root to Python path
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from config.config import DB_CONFIG, EXCEL_FOLDER

# -------------------------------------------------
# MySQL Connection
# -------------------------------------------------
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# -------------------------------------------------
# Function to insert Excel data
# -------------------------------------------------
def insert_excel_to_mysql(excel_file, table_name):
    file_path = os.path.join(PROJECT_ROOT, EXCEL_FOLDER, excel_file)

    df = pd.read_excel(file_path, engine="openpyxl")

    # Convert NaN → None (MySQL NULL)
    df = df.where(pd.notnull(df), None)

    # Convert empty strings → None
    df = df.replace("", None)

    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        try:
            cursor.execute(sql, tuple(row))
        except mysql.connector.Error as err:
            print(f"Skipping row {tuple(row)} → {err}")

    conn.commit()
    print(f"Data inserted into {table_name}")

# -------------------------------------------------
# Excel → Table Mapping
# -------------------------------------------------
files_tables = {
    "products.xlsx": "products",
    "customers.xlsx": "customers",
    "orders.xlsx": "orders",
    "payments.xlsx": "payments",
    "delivery.xlsx": "delivery"
}

# -------------------------------------------------
# Insert all files
# -------------------------------------------------
for file, table in files_tables.items():
    insert_excel_to_mysql(file, table)

# -------------------------------------------------
# Close connection
# -------------------------------------------------
cursor.close()
conn.close()

print("All Excel files uploaded successfully!")
