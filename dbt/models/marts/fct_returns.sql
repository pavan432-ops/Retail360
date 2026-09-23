SELECT
    return_id,
    order_id,
    product_id,
    return_date,
    return_quantity,
    return_reason,
    order_exists_in_sales,
    return_quantity_exceeds_sold,
    return_before_order
FROM {{ ref('stg_returns') }}