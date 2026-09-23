SELECT
    customer_id,
    total_orders,
    total_units,
    total_sales,
    average_order_value,
    first_order_date,
    last_order_date,

    DATEDIFF('2026-08-31', last_order_date) AS recency_days,

    CASE
        WHEN DATEDIFF('2026-08-31', last_order_date) <= 30
            THEN 'Active'

        WHEN DATEDIFF('2026-08-31', last_order_date) <= 90
            THEN 'At Risk'

        ELSE 'Inactive'
    END AS customer_status

FROM {{ ref('int_customer_metrics') }}