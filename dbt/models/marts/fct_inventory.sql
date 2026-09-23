SELECT
    inventory_date,
    store_id,
    product_id,
    stock_quantity,
    reorder_level,

    CASE
        WHEN stock_quantity IS NULL THEN 1
        ELSE 0
    END AS stock_missing_flag,

    CASE
        WHEN stock_quantity < reorder_level THEN 1
        ELSE 0
    END AS below_reorder_flag

FROM {{ ref('stg_inventory') }}
