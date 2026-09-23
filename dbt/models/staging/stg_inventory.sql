SELECT
    inventory_date,
    store_id,
    product_id,
    stock_quantity,
    reorder_level
FROM {{ source('retail360', 'raw_inventory') }}