# Retail360 – dbt Transformation

## Overview

dbt is used in Retail360 for data transformation, testing, and analytical modeling.

The raw data is stored in MySQL and dbt transforms it into clean staging models, dimensions, facts, and analytical models used by Power BI.

## dbt Flow

MySQL Raw Tables
        ↓
Staging Models
        ↓
Dimension & Fact Models
        ↓
Intermediate Analytical Models
        ↓
Power BI

## Staging Models

The staging layer creates views from the raw MySQL tables.

Staging models:

- stg_customers
- stg_products
- stg_stores
- stg_sales
- stg_inventory
- stg_returns

The staging layer provides a clean and consistent starting point for downstream transformations.

## Dimension Models

### dim_customers

Contains customer master information.

### dim_products

Contains product master information.

### dim_stores

Contains store master information.

### dim_date

Provides the date dimension used for time-based analysis.

The date dimension covers:

- Date
- Year
- Quarter
- Month
- Month Name
- Month Year
- Day
- Day of Week
- Day Name
- Weekend Indicator

## Fact Models

### fct_sales

Contains sales transaction data and calculates:

- Gross Sales
- Discount Amount
- Net Sales
- Missing Price Flag
- Missing Customer Flag
- Missing Order Date Flag

### fct_returns

Contains product return transactions and return audit information.

### fct_inventory

Contains inventory observations and inventory quality/status flags.

## Intermediate Analytical Models

### int_inventory_snapshot

Creates one analytical snapshot per date, store, and product.

It also handles duplicate inventory grain observations using controlled aggregation.

### int_customer_metrics

Calculates customer-level metrics including:

- Total Orders
- Total Units
- Total Sales
- Average Order Value
- First Order Date
- Last Order Date

### int_customer_status

Classifies customers into:

- Active
- At Risk
- Inactive

### int_product_metrics

Calculates product-level:

- Total Orders
- Total Units
- Total Sales
- Total Cost
- Gross Profit
- Gross Margin %

### int_product_performance

Classifies products based on sales and gross margin performance.

Performance groups:

- High Sales - High Margin
- High Sales - Low Margin
- Low Sales - High Margin
- Low Sales - Low Margin
- Data Quality Review

### int_return_metrics

Aggregates return information at the product level.

### int_product_return_rate

Combines product sales and return information to calculate product-level return rates without creating fact-to-fact multiplication.

## dbt Testing

dbt tests are used to validate important data quality rules.

Examples:

- not_null
- unique
- relationships

Tests are applied to important primary keys and foreign-key relationships.

## Materialization

Staging models are materialized as:

Views

Analytical models are materialized as:

Tables

## dbt Project Structure

dbt
│
├── models
│   ├── staging
│   └── marts
│
├── dbt_project.yml
└── packages.yml

## Transformation Objective

The objective of the dbt layer is to convert raw database data into reliable, tested, and business-ready analytical models for Power BI.

## Final Flow

Raw MySQL Data
        ↓
dbt Staging
        ↓
Dimensions + Facts
        ↓
Intermediate Analytics
        ↓
Power BI