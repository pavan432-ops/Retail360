import mysql.connector
from getpass import getpass
import pandas as pd
from pathlib import Path


# ---------------------------------------------------------
# PROJECT PATH
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "Data" / "processed"


# ---------------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------------

def connect_to_mysql():
    password = getpass("Enter MySQL password: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="retail360"
    )

    print("MySQL connection successful!")
    return connection


# ---------------------------------------------------------
# CLEAR STAGING TABLES
# ---------------------------------------------------------

def clear_staging_tables(connection):

    cursor = connection.cursor()

    tables = [
        "raw_customers",
        "raw_products",
        "raw_stores",
        "raw_sales",
        "raw_inventory",
        "raw_returns"
    ]

    for table in tables:
        cursor.execute(f"TRUNCATE TABLE {table}")
        print(f"Cleared: {table}")

    cursor.close()


# ---------------------------------------------------------
# LOAD CUSTOMERS
# ---------------------------------------------------------

def load_customers(connection):

    customers = pd.read_csv(
        PROCESSED_DIR / "customers_clean.csv"
    )

    print("Customers loaded into Python:", len(customers))

    insert_query = """
    INSERT INTO raw_customers (
        customer_id,
        customer_name,
        gender,
        age,
        city,
        state,
        region,
        signup_date,
        segment
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = customers.astype(object).where(
        pd.notnull(customers), None
    ).values.tolist()

    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()

    print("Customers inserted into MySQL:", cursor.rowcount)

    cursor.close()


# ---------------------------------------------------------
# LOAD PRODUCTS
# ---------------------------------------------------------

def load_products(connection):

    products = pd.read_csv(
        PROCESSED_DIR / "products_clean.csv"
    )

    print("Products loaded into Python:", len(products))

    insert_query = """
    INSERT INTO raw_products (
        product_id,
        product_name,
        category,
        subcategory,
        brand,
        cost_price,
        selling_price
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = products.astype(object).where(
        pd.notnull(products), None
    ).values.tolist()

    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()

    print("Products inserted into MySQL:", cursor.rowcount)

    cursor.close()


# ---------------------------------------------------------
# LOAD STORES
# ---------------------------------------------------------

def load_stores(connection):

    stores = pd.read_csv(
        PROCESSED_DIR / "stores_clean.csv"
    )

    print("Stores loaded into Python:", len(stores))

    insert_query = """
    INSERT INTO raw_stores (
        store_id,
        store_name,
        city,
        state,
        region,
        store_type
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = stores.astype(object).where(
        pd.notnull(stores), None
    ).values.tolist()

    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()

    print("Stores inserted into MySQL:", cursor.rowcount)

    cursor.close()


# ---------------------------------------------------------
# LOAD SALES
# ---------------------------------------------------------

def load_sales(connection):

    sales = pd.read_csv(
        PROCESSED_DIR / "sales_clean.csv"
    )

    print("Sales loaded into Python:", len(sales))

    insert_query = """
    INSERT INTO raw_sales (
        order_id,
        order_date,
        customer_id,
        product_id,
        store_id,
        quantity,
        unit_price,
        discount,
        payment_method,
        channel
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = sales.astype(object).where(
        pd.notnull(sales), None
    ).values.tolist()

    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()

    print("Sales inserted into MySQL:", cursor.rowcount)

    cursor.close()


# ---------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------
# ---------------------------------------------------------
# LOAD INVENTORY
# ---------------------------------------------------------

def load_inventory(connection):

    inventory = pd.read_csv(
        PROCESSED_DIR / "inventory_clean.csv"
    )

    print("Inventory loaded into Python:", len(inventory))

    insert_query = """
    INSERT INTO raw_inventory (
        inventory_date,
        store_id,
        product_id,
        stock_quantity,
        reorder_level
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    data = inventory.astype(object).where(
        pd.notnull(inventory), None
    ).values.tolist()

    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()

    print("Inventory inserted into MySQL:", cursor.rowcount)

    cursor.close()
 # ---------------------------------------------------------
# LOAD RETURNS
# ---------------------------------------------------------

def load_returns(connection):

    returns = pd.read_csv(
        PROCESSED_DIR / "returns_clean.csv"
    )

    print("Returns loaded into Python:", len(returns))

    insert_query = """
    INSERT INTO raw_returns (
        return_id,
        order_id,
        product_id,
        return_date,
        return_quantity,
        return_reason,
        order_exists_in_sales,
        return_quantity_exceeds_sold,
        return_before_order
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = returns.astype(object).where(
        pd.notnull(returns), None
    ).values.tolist()

    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()

    print("Returns inserted into MySQL:", cursor.rowcount)

    cursor.close()


# ---------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------

def main():

    connection = connect_to_mysql()

    try:
        clear_staging_tables(connection)

        load_customers(connection)
        load_products(connection)
        load_stores(connection)
        load_sales(connection)
        load_inventory(connection)
        load_returns(connection)

        print("\n========== MYSQL LOAD COMPLETE ==========")

    finally:
        connection.close()
        print("MySQL connection closed.")


# ---------------------------------------------------------
# RUN PIPELINE
# ---------------------------------------------------------

if __name__ == "__main__":
    main()