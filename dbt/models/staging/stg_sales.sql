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
    channel
FROM {{ source('retail360', 'raw_sales') }}