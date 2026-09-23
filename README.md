# 📊 Retail360 – End-to-End Retail Analytics Project

## 🚀 Project Overview

Retail360 is an end-to-end retail analytics project designed to simulate a real-world MNC-style Data Analyst workflow.

The project transforms realistic synthetic retail data into reliable analytical models and interactive Power BI dashboards.

The complete pipeline covers:

- Data ingestion
- Data cleaning
- Data quality validation
- MySQL database loading
- dbt transformation
- Analytical modeling
- DAX calculations
- Power BI dashboards
- Business insights

## 🏗️ Project Architecture

Excel / CSV / API → Python → MySQL → dbt → Analytical Model → Power BI → Business Insights

Python handles ingestion, cleaning, and data quality validation.

MySQL stores the raw and staging data.

dbt performs transformation, testing, and analytical modeling.

Power BI is used for DAX calculations, KPIs, visualization, and business analysis.

Git/GitHub is used for version control, documentation, and portfolio presentation.

VS Code is used as the development environment.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Data ingestion, cleaning and validation |
| 🐼 Pandas | Data manipulation and cleaning |
| 🔢 NumPy | Numerical and data processing |
| 🗄️ MySQL | Database storage |
| 🔄 dbt | Transformation, testing and analytical modeling |
| 📊 Power BI | Business intelligence and visualization |
| 🧮 DAX | KPI and analytical calculations |
| 🌐 Git/GitHub | Version control and project documentation |
| 💻 VS Code | Development environment |

## 📂 Data Sources

The project uses realistic synthetic retail business data representing:

- 👥 Customers
- 📦 Products
- 🏪 Stores
- 💰 Sales
- 📋 Inventory
- 🔄 Returns

The datasets intentionally contain data-quality issues to simulate real-world business data.

## 🐍 Python Data Processing

Python is used for:

- Data ingestion
- Data cleaning
- Data validation
- Data quality checks
- Preparing processed datasets for MySQL

### 🧹 Cleaning Activities

- Duplicate record removal
- Invalid value detection
- Missing value identification
- Data standardization
- Invalid date handling
- Invalid quantity handling
- Price validation
- Customer ID validation
- Inventory grain validation
- Return data validation

### 📊 Final Processed Records

- Customers: 25,000
- Products: 3,000
- Stores: 100
- Sales: 249,850
- Inventory: 300,000
- Returns: 20,000

Processed datasets are stored in the `Data/processed` folder.

## 🗄️ MySQL Database

MySQL is used as the central database layer between Python processing and dbt transformation.

### Database

`retail360`

### 📋 Raw Tables

- `raw_customers`
- `raw_products`
- `raw_stores`
- `raw_sales`
- `raw_inventory`
- `raw_returns`

The Python MySQL loader performs a full refresh and loads the processed datasets into the raw tables.

## 🔄 dbt Transformation

dbt is used for:

- Data transformation
- Data testing
- Data modeling
- Analytical model creation

### 🧱 Staging Models

- `stg_customers`
- `stg_products`
- `stg_stores`
- `stg_sales`
- `stg_inventory`
- `stg_returns`

### 📐 Dimension Models

- `dim_customers`
- `dim_products`
- `dim_stores`
- `dim_date`

### 📊 Fact Models

- `fct_sales`
- `fct_returns`
- `fct_inventory`

### 🔍 Analytical Models

- `int_inventory_snapshot`
- `int_customer_metrics`
- `int_customer_status`
- `int_product_metrics`
- `int_product_performance`
- `int_return_metrics`
- `int_product_return_rate`

### ✅ dbt Testing

Important data-quality tests include:

- `not_null`
- `unique`
- `relationships`

Staging models are materialized as views.

Analytical models are materialized as tables.

## 📈 Power BI Dashboard

### 🖼️ Dashboard Preview

#### 1️⃣ Executive Overview

![Executive Overview](screenshots/Executive%20overview%20.png)

#### 2️⃣ Sales & Customer Analytics

![Sales & Customer Analytics](screenshots/sales%20and%20customer%20analytics.png)

#### 3️⃣ Product, Inventory & Returns

![Product, Inventory & Returns](screenshots/Product%2C%20Inventory%20%26%20Returns.png)

The final Power BI solution contains exactly three pages.

### 1️⃣ Executive Overview

#### 🎯 KPIs

- Total Net Sales
- Total Orders
- Total Units
- Average Order Value
- Gross Profit
- Gross Margin %

#### 💡 Dynamic Insights

- Top Sales Region
- Top Sales Category
- Top Sales Channel

#### 📊 Visuals

- Gross Margin by Category
- Net Sales by Channel
- Net Sales by Category
- Monthly Net Sales Trend
- Net Sales by Region

#### 🔎 Slicers

- Date
- Region
- Channel
- Category
- Store Type

### 2️⃣ Sales & Customer Analytics

#### 🎯 KPIs

- Active Customers
- At Risk Customers
- Inactive Customers
- Average Order Value

#### 📊 Visuals

- Customer Count by Status
- Net Sales by Customer Segment
- Net Sales by Customer Status
- Average Order Value by Customer Segment
- Net Sales by Payment Method
- Customer Acquisition Trend

#### 🔎 Slicers

- Date
- Region
- Channel
- Customer Segment
- Customer Status
- Payment Method

### 3️⃣ Product, Inventory & Returns

#### 🎯 KPIs

- Returned Units
- Below Reorder Products
- Total Products
- Gross Profit
- Gross Margin %
- Return Rate %

#### 📊 Visuals

- Product Performance Summary
- Product Sales vs Gross Margin
- Product Return Risk
- Returned Units by Return Reason
- Inventory Status

#### 🔎 Slicers

- Date
- Region
- Category
- Store Type

## 🎯 Key Business Metrics

The project calculates important retail KPIs including:

- 💰 Net Sales
- 🛒 Total Orders
- 📦 Total Units
- 💵 Average Order Value
- 📈 Gross Profit
- 📊 Gross Margin %
- 👥 Customer Status
- 🔄 Return Rate %
- 📦 Products Below Reorder Level
- 🏷️ Product Performance
- 👤 Customer Acquisition

## 🧮 DAX

DAX is used to create business measures and analytical calculations.

### Main Measures

- Total Net Sales
- Total Orders
- Total Units
- Average Order Value
- Gross Profit
- Gross Margin %
- Top Sales Region
- Top Sales Category
- Top Sales Channel
- Active Customers
- At Risk Customers
- Inactive Customers
- Net Sales by Customer Status
- Below Reorder Products
- Returned Units
- Return Rate %
- Gross Margin % by Performance

Complete DAX documentation is available in `documentation/DAX_Measures.md`.

## ✅ Data Quality

Data quality is treated as an important part of the project.

The pipeline validates:

- Duplicate records
- Missing values
- Invalid dates
- Invalid quantities
- Missing prices
- Missing customer IDs
- Inventory duplicate grain
- Return data consistency

### 📋 Final Data Quality Results

- Customers: 25,000 rows | duplicate rows: 0 | null cells: 258
- Products: 3,000 rows | duplicate rows: 0 | null cells: 40
- Stores: 100 rows | duplicate rows: 0 | null cells: 0
- Sales: 249,850 rows | duplicate rows: 0 | null cells: 3,566
- Inventory: 300,000 rows | duplicate rows: 0 | null cells: 100
- Returns: 20,000 rows | duplicate rows: 0 | null cells: 30
- Inventory duplicate grain keys: 2,464
- Sales invalid quantities: 0
- Sales missing prices: 3,346
- Sales missing customers: 120
- Sales missing dates: 100
- Returns invalid quantities: 0

## ⚙️ Automation Flow

Excel / CSV / API → Python → MySQL → dbt → Analytical Model → Power BI Import → Scheduled Refresh

The pipeline is designed so that new source data can be processed through Python, loaded into MySQL, transformed through dbt, and consumed by Power BI.

## 🎨 Dashboard Design Principles

The dashboard follows these principles:

1. 🎯 Every visual has a business purpose.
2. 📊 Visual types are selected according to the analytical question.
3. 🚫 Duplicate or unnecessary visuals are avoided.
4. 👁️ Important KPIs receive strong visual hierarchy.
5. 👨‍💼 The dashboard is readable for both freshers and experienced BI professionals.
6. 🧹 The layout is clean and uncluttered.
7. 💡 Visuals support business insights and actions.
8. ✅ Data quality and metric definitions are maintained.
9. 🎨 Consistent formatting is used across all pages.
10. 💼 The final dashboard is designed for professional portfolio and LinkedIn presentation.

## 🌑 Dashboard Theme

The dashboard uses a consistent professional dark theme.

- Background: Dark charcoal
- Panels: Dark gray
- Primary text: White
- Secondary text: Light gray
- Accent: Red
- Borders: Subtle red

## 📁 Project Structure

Retail360/
├── Data/
│   ├── raw/
│   └── processed/
├── dbt/
├── documentation/
├── powerbi/
├── python/
├── screenshots/
├── sql/
└── README.md

### 🐍 Python

- `python/ingestion.py`
- `python/mysql_loader.py`

### 📊 Power BI

- `powerbi/Retail360.pbix`

### 📚 Documentation

- `documentation/DAX_Measures.md`
- `documentation/PROJECT_ARCHITECTURE.md`
- `documentation/SQL_Database.md`
- `documentation/DBT_Transformation.md`
- `documentation/PYTHON_Data_Processing.md`
- `documentation/POWERBI_Dashboard.md`

## 📚 Documentation

Detailed project documentation is available in the `documentation` folder:

- 🧮 `DAX_Measures.md` – DAX measures and purposes
- 🏗️ `PROJECT_ARCHITECTURE.md` – Complete project architecture
- 🗄️ `SQL_Database.md` – MySQL database and tables
- 🔄 `DBT_Transformation.md` – dbt models and transformations
- 🐍 `PYTHON_Data_Processing.md` – Python cleaning and data-quality processing
- 📊 `POWERBI_Dashboard.md` – Power BI dashboard structure and design

## 🎯 Business Objective

The objective of Retail360 is to transform raw retail data into reliable, business-ready analytics.

The solution helps analyze:

- Overall sales performance
- Customer behavior
- Product profitability
- Regional performance
- Channel performance
- Inventory conditions
- Product returns
- Customer acquisition

## 🏆 Project Outcome

Retail360 demonstrates the complete Data Analyst workflow:

Raw Data → Data Cleaning → Data Quality → Database → Transformation → Analytical Modeling → DAX → Power BI → Business Insights

The project demonstrates practical skills across:

- 🐍 Python
- 🗄️ SQL
- 🐬 MySQL
- 🔄 dbt
- 📊 Power BI
- 🧮 DAX
- 🌐 Git/GitHub

## 💼 Portfolio Project

Retail360 is designed as a portfolio project to demonstrate practical end-to-end Data Analyst capabilities, data-quality practices, analytical thinking, and business-focused dashboard development.