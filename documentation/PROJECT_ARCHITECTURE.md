# Retail360 – Project Architecture

## Project Overview

Retail360 is an end-to-end retail analytics project designed to simulate a real-world MNC data analytics workflow.

The project takes raw retail data through data ingestion, data cleaning, SQL storage, dbt transformation, analytical modeling, and Power BI reporting.

## Architecture

DATA SOURCES
Excel / CSV / API
        ↓
PYTHON
Ingestion / Cleaning / Data Quality
        ↓
MYSQL DATABASE
Raw / Staging Data
        ↓
DBT
Transformation / Testing / Modeling
        ↓
ANALYTICAL MODEL
Fact Tables + Dimension Tables
        ↓
POWER BI
DAX / KPIs / Dashboards
        ↓
BUSINESS INSIGHTS
Decisions / Actions

## Tools Used

- Python – Data ingestion, cleaning, and data quality checks
- Pandas – Data manipulation and cleaning
- NumPy – Data processing
- MySQL – Database storage
- dbt – Data transformation, testing, and analytical modeling
- Power BI – Dashboard development and business analysis
- DAX – Measures and analytical calculations
- GitHub – Version control and project documentation
- VS Code – Development workspace

## Data Sources

The project uses realistic synthetic business data representing:

- Customers
- Products
- Stores
- Sales
- Inventory
- Returns

## Data Pipeline

Excel / CSV
    ↓
Python
    ↓
MySQL
    ↓
dbt
    ↓
Fact + Dimension Model
    ↓
Power BI
    ↓
Business Insights

## Main Analytical Areas

### Executive Overview

Provides a high-level view of:

- Net Sales
- Orders
- Units Sold
- Average Order Value
- Gross Profit
- Gross Margin
- Sales by Region
- Sales by Category
- Sales by Channel

### Sales & Customer Analytics

Analyzes:

- Customer Status
- Customer Segments
- Customer Sales
- Average Order Value
- Payment Methods
- Customer Acquisition

### Product, Inventory & Returns

Analyzes:

- Product Performance
- Product Sales
- Gross Margin
- Return Risk
- Return Reasons
- Inventory Status
- Products Below Reorder Level

## Automation Flow

Excel / CSV / API
        ↓
Python
        ↓
MySQL
        ↓
dbt
        ↓
Power BI Import
        ↓
Scheduled Refresh

## Business Objective

The objective of Retail360 is to transform raw retail data into reliable analytical datasets and business dashboards that help organizations understand sales performance, customer behavior, product profitability, inventory conditions, and product returns.