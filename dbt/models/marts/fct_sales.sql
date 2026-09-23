SELECT
    order_id,
    order_date,
    customer_id,
    product_id,
    store_id,
    quantity,
    unit_price,
    discount,
    payment_method,
    channel,

    quantity * unit_price AS gross_sales,

    (quantity * unit_price) * discount AS discount_amount,

    (quantity * unit_price)
        - ((quantity * unit_price) * discount) AS net_sales,

    CASE
        WHEN unit_price IS NULL THEN 1
        ELSE 0
    END AS price_missing_flag,

    CASE
        WHEN customer_id IS NULL THEN 1
        ELSE 0
    END AS customer_missing_flag,

    CASE
        WHEN order_date IS NULL THEN 1
        ELSE 0
    END AS order_date_missing_flag

FROM {{ ref('stg_sales') }}