SELECT
    inventory_date,
    store_id,
    product_id,

    AVG(stock_quantity) AS avg_stock_quantity,
    AVG(reorder_level) AS avg_reorder_level,

    COUNT(*) AS observation_count,

    CASE
        WHEN COUNT(*) > 1 THEN 1
        ELSE 0
    END AS duplicate_grain_flag,

    CASE
        WHEN COUNT(stock_quantity) = 0 THEN 1
        ELSE 0
    END AS stock_missing_flag,

    CASE
        WHEN AVG(stock_quantity) < AVG(reorder_level) THEN 1
        ELSE 0
    END AS below_reorder_flag

FROM {{ ref('fct_inventory') }}

GROUP BY
    inventory_date,
    store_id,
    product_id