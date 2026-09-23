SELECT
    customer_id,

    COUNT(DISTINCT order_id) AS total_orders,

    SUM(quantity) AS total_units,

    SUM(net_sales) AS total_sales,

    SUM(net_sales) / COUNT(DISTINCT order_id) AS average_order_value,

    MIN(order_date) AS first_order_date,

    MAX(order_date) AS last_order_date

FROM {{ ref('fct_sales') }}

WHERE customer_id IS NOT NULL

GROUP BY
    customer_id