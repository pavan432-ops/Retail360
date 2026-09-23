# Retail360 – Power BI Dashboard

## Overview

Power BI is used in Retail360 to create the final business intelligence layer.

The Power BI dashboard connects to the analytical models created through dbt and presents business-focused KPIs, charts, slicers, and insights.

## Dashboard Structure

Retail360 contains exactly 3 dashboard pages:

1. Executive Overview
2. Sales & Customer Analytics
3. Product, Inventory & Returns

## Page 1 – Executive Overview

### KPIs

- Total Net Sales
- Total Orders
- Total Units
- Average Order Value
- Gross Profit
- Gross Margin %

### Dynamic Insights

- Top Sales Region
- Top Sales Category
- Top Sales Channel

### Visuals

- Gross Margin by Category
- Net Sales by Channel
- Net Sales by Category
- Monthly Net Sales Trend
- Net Sales by Region

### Slicers

- Date
- Region
- Channel
- Category
- Store Type

## Page 2 – Sales & Customer Analytics

### KPIs

- Active Customers
- At Risk Customers
- Inactive Customers
- Average Order Value

### Visuals

- Customer Count by Status
- Net Sales by Customer Segment
- Net Sales by Customer Status
- Average Order Value by Customer Segment
- Net Sales by Payment Method
- Customer Acquisition Trend

### Slicers

- Date
- Region
- Channel
- Customer Segment
- Customer Status
- Payment Method

## Page 3 – Product, Inventory & Returns

### KPIs

- Returned Units
- Below Reorder Products
- Total Products
- Gross Profit
- Gross Margin %
- Return Rate %

### Visuals

- Product Performance Summary
- Product Sales vs Gross Margin
- Product Return Risk
- Returned Units by Return Reason
- Inventory Status

### Slicers

- Date
- Region
- Category
- Store Type

## DAX

DAX is used to create business measures and analytical calculations such as:

- Total Net Sales
- Total Orders
- Total Units
- Average Order Value
- Gross Profit
- Gross Margin %
- Customer Status Metrics
- Return Rate %
- Below Reorder Products
- Dynamic Top Sales Insights

The complete DAX documentation is maintained separately in:

DAX_Measures.md

## Dashboard Design Principles

The dashboard follows these principles:

1. Every visual has a business purpose.
2. The visual type is selected according to the analytical question.
3. Duplicate or unnecessary visuals are avoided.
4. KPIs receive strong visual hierarchy.
5. The dashboard is readable for both freshers and experienced BI professionals.
6. The layout is clean and uncluttered.
7. Visuals are designed to support business insights and actions.
8. Data quality and metric definitions are maintained.
9. Consistent formatting is used across all pages.
10. The final dashboard is designed for professional portfolio and LinkedIn presentation.

## Theme

The dashboard uses a consistent dark professional theme.

- Background: Dark charcoal
- Panels: Dark gray
- Primary text: White
- Secondary text: Light gray
- Accent: Red
- Borders: Subtle red

## Data Model

Power BI uses a dimensional analytical model consisting of fact and dimension tables.

Main dimensions:

- dim_customers
- dim_products
- dim_stores
- dim_date

Main facts:

- fct_sales
- fct_returns
- fct_inventory

Additional analytical models are used for customer, product, inventory, and return analysis.

## Refresh Flow

Data Sources
        ↓
Python
        ↓
MySQL
        ↓
dbt
        ↓
Power BI Import
        ↓
Dashboard

The Power BI model is designed to use refreshed analytical data from the upstream pipeline.

## Business Objective

The objective of the Power BI layer is to transform analytical data into clear business intelligence that helps users understand:

- Overall sales performance
- Customer behavior
- Product profitability
- Inventory conditions
- Product returns
- Regional and channel performance