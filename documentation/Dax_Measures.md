Total Net Sales =
SUM('retail360 fct_sales'[net_sales])

Purpose: Calculates the total net sales after discounts.


Total Orders =
DISTINCTCOUNT('retail360 fct_sales'[order_id])

Purpose: Calculates the number of unique orders.


Total Units =
SUM('retail360 fct_sales'[quantity])

Purpose: Calculates the total number of product units sold.


Average Order Value =
DIVIDE(
    [Total Net Sales],
    [Total Orders]
)

Purpose: Calculates the average net sales value generated per order.


Gross Profit =
SUM('retail360 int_product_metrics'[gross_profit])

Purpose: Calculates the total gross profit generated from sales.


Gross Margin % =
DIVIDE(
    [Gross Profit],
    [Total Net Sales]
)

Purpose: Calculates gross profit as a percentage of net sales.


Top Sales Region =
VAR RegionTable =
    TOPN(
        1,
        ALLSELECTED('retail360 dim_stores'[region]),
        [Total Net Sales],
        DESC
    )
RETURN
    CONCATENATEX(
        RegionTable,
        'retail360 dim_stores'[region],
        ", "
    )

Purpose: Dynamically identifies the region with the highest net sales based on the current filter context.


Top Sales Category =
VAR CategoryTable =
    TOPN(
        1,
        ALLSELECTED('retail360 dim_products'[category]),
        [Total Net Sales],
        DESC
    )
RETURN
    CONCATENATEX(
        CategoryTable,
        'retail360 dim_products'[category],
        ", "
    )

Purpose: Dynamically identifies the product category with the highest net sales based on the current filter context.


Top Sales Channel =
VAR ChannelTable =
    TOPN(
        1,
        ALLSELECTED('retail360 fct_sales'[channel]),
        [Total Net Sales],
        DESC
    )
RETURN
    CONCATENATEX(
        ChannelTable,
        'retail360 fct_sales'[channel],
        ", "
    )

Purpose: Dynamically identifies the sales channel with the highest net sales based on the current filter context.


Active Customers =
CALCULATE(
    DISTINCTCOUNT('retail360 int_customer_status'[customer_id]),
    'retail360 int_customer_status'[customer_status] = "Active"
)

Purpose: Counts the customers classified as Active.


At Risk Customers =
CALCULATE(
    DISTINCTCOUNT('retail360 int_customer_status'[customer_id]),
    'retail360 int_customer_status'[customer_status] = "At Risk"
)

Purpose: Counts the customers classified as At Risk.


Inactive Customers =
CALCULATE(
    DISTINCTCOUNT('retail360 int_customer_status'[customer_id]),
    'retail360 int_customer_status'[customer_status] = "Inactive"
)

Purpose: Counts the customers classified as Inactive.


Net Sales by Customer Status =
CALCULATE(
    [Total Net Sales],
    TREATAS(
        VALUES('retail360 int_customer_status'[customer_id]),
        'retail360 fct_sales'[customer_id]
    )
)

Purpose: Calculates net sales associated with customers belonging to the selected customer status.


Below Reorder Products =
CALCULATE(
    DISTINCTCOUNT('retail360 int_inventory_snapshot'[product_id]),
    'retail360 int_inventory_snapshot'[below_reorder_flag] = 1
)

Purpose: Counts distinct products that are below the reorder threshold.


Returned Units =
SUM('retail360 fct_returns'[return_quantity])

Purpose: Calculates the total number of returned product units.


Return Rate % =
DIVIDE(
    [Returned Units],
    [Total Units]
)

Purpose: Calculates returned units as a percentage of total units sold.


Gross Margin % by Performance =
DIVIDE(
    SUM('retail360 int_product_performance'[gross_profit]),
    SUM('retail360 int_product_performance'[total_sales])
)

Purpose: Calculates gross margin percentage for the product performance analysis.


Below Reorder Observations =
CALCULATE(
    COUNTROWS('retail360 int_inventory_snapshot'),
    'retail360 int_inventory_snapshot'[below_reorder_flag] = 1
)

Purpose: Counts inventory snapshot observations that are below the reorder threshold.


Inventory Status =
IF(
    'retail360 int_inventory_snapshot'[below_reorder_flag] = 1,
    "Below Reorder",
    "Healthy"
)

Purpose: Categorizes inventory observations as Healthy or Below Reorder for the Inventory Status visual.


Signup Month =
IF(
    ISBLANK('retail360 dim_customers'[signup_date]),
    BLANK(),
    DATE(
        YEAR('retail360 dim_customers'[signup_date]),
        MONTH('retail360 dim_customers'[signup_date]),
        1
    )
)

Purpose: Converts customer signup dates to the first day of the signup month for monthly customer acquisition analysis.