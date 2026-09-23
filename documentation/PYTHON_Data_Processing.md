# Retail360 – Python Data Processing

## Overview

Python is used in Retail360 for data ingestion, data cleaning, validation, and data quality checks.

Pandas is used for tabular data processing and NumPy is used for numerical/data processing operations.

## Python Data Processing Flow

Raw Excel / CSV Files
        ↓
Python + Pandas
        ↓
Data Cleaning
        ↓
Data Quality Checks
        ↓
Processed CSV Files
        ↓
MySQL

## Libraries Used

- Python
- Pandas
- NumPy

## Datasets Processed

Python processes the following datasets:

- Customers
- Products
- Stores
- Sales
- Inventory
- Returns

## Customer Data Cleaning

Raw records: 25,100

Final records: 25,000

Cleaning performed:

- Removed exact duplicate rows.
- Resolved conflicting duplicate customer IDs.
- Converted invalid ages to NULL.
- Identified missing cities.
- Identified invalid/missing signup dates.

Final output:

Data/processed/customers_clean.csv

## Product Data Cleaning

Records: 3,000

Cleaning performed:

- Standardized the category value "Electronic" to "Electronics".
- Converted invalid negative selling prices to NULL.
- Validated product records.

Final output:

Data/processed/products_clean.csv

## Store Data Cleaning

Records: 100

Cleaning performed:

- Identified corrupted city values.
- Corrected invalid city values using store and location consistency checks.
- Validated store records.

Final output:

Data/processed/stores_clean.csv

## Sales Data Cleaning

Raw records: 250,500

Final records: 249,850

Cleaning performed:

- Removed duplicate rows.
- Removed invalid negative quantities.
- Converted invalid order dates to NULL.
- Retained missing customer IDs as NULL.
- Converted invalid unit prices to NULL.
- Performed customer lifecycle validation.

Final output:

Data/processed/sales_clean.csv

## Inventory Data Cleaning

Records: 300,000

Cleaning performed:

- Converted negative stock quantities to NULL.
- Validated inventory dates.
- Validated reorder levels.
- Identified duplicate date-store-product grain observations.
- Preserved duplicate observations for controlled downstream aggregation.

Final output:

Data/processed/inventory_clean.csv

## Returns Data Cleaning

Records: 20,000

Cleaning performed:

- Converted invalid negative return quantities to NULL.
- Validated return orders against sales.
- Checked whether returned quantity exceeded sold quantity.
- Checked whether returns occurred before the original order date.

Final output:

Data/processed/returns_clean.csv

## Data Quality Gate

The final Python data quality checks include:

- Duplicate row validation
- Missing value validation
- Invalid quantity validation
- Missing price validation
- Missing customer validation
- Missing date validation
- Inventory duplicate grain validation
- Return data validation

## Final Data Quality Results

Customers: 25,000 rows | duplicate rows: 0 | null cells: 258

Products: 3,000 rows | duplicate rows: 0 | null cells: 40

Stores: 100 rows | duplicate rows: 0 | null cells: 0

Sales: 249,850 rows | duplicate rows: 0 | null cells: 3,566

Inventory: 300,000 rows | duplicate rows: 0 | null cells: 100

Returns: 20,000 rows | duplicate rows: 0 | null cells: 30

Inventory duplicate grain keys: 2,464

Sales invalid quantities: 0

Sales missing prices: 3,346

Sales missing customers: 120

Sales missing dates: 100

Returns invalid quantities: 0

## Python to MySQL

After processing and validation, the cleaned datasets are loaded into MySQL using the Python MySQL loader.

Flow:

Python Processed Data
        ↓
MySQL Raw Tables
        ↓
dbt Transformation

## Data Processing Objective

The objective of the Python layer is to ensure that raw business data is cleaned, validated, and prepared before it enters the database and downstream analytical pipeline.