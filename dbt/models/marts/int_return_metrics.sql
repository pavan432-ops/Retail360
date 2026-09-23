SELECT
    r.product_id,
    p.product_name,
    p.category,
    p.subcategory,
    p.brand,

    COUNT(*) AS return_count,

    SUM(r.return_quantity) AS returned_units,

    SUM(
        CASE
            WHEN r.return_quantity IS NULL THEN 1
            ELSE 0
        END
    ) AS invalid_quantity_rows,

    SUM(
        CASE
            WHEN r.order_exists_in_sales = 0 THEN 1
            ELSE 0
        END
    ) AS unmatched_order_rows,

    SUM(
        CASE
            WHEN r.return_quantity_exceeds_sold = 1 THEN 1
            ELSE 0
        END
    ) AS exceeds_sold_rows,

    SUM(
        CASE
            WHEN r.return_before_order = 1 THEN 1
            ELSE 0
        END
    ) AS return_before_order_rows

FROM {{ ref('fct_returns') }} r

LEFT JOIN {{ ref('dim_products') }} p
    ON r.product_id = p.product_id

GROUP BY
    r.product_id,
    p.product_name,
    p.category,
    p.subcategory,
    p.brand
