WITH sales_by_product AS (

    SELECT
        product_id,
        SUM(quantity) AS sold_units

    FROM {{ ref('fct_sales') }}

    GROUP BY product_id
),

product_return_rate AS (

    SELECT
        p.product_id,
        p.product_name,
        p.category,
        p.subcategory,
        p.brand,

        COALESCE(s.sold_units, 0) AS sold_units,

        COALESCE(r.returned_units, 0) AS returned_units,

        COALESCE(r.return_count, 0) AS return_count,

        r.invalid_quantity_rows,
        r.unmatched_order_rows,
        r.exceeds_sold_rows,
        r.return_before_order_rows,

        CASE
            WHEN COALESCE(s.sold_units, 0) = 0
                THEN NULL
            ELSE
                (COALESCE(r.returned_units, 0) / s.sold_units) * 100
        END AS return_rate_pct

    FROM {{ ref('dim_products') }} p

    LEFT JOIN sales_by_product s
        ON p.product_id = s.product_id

    LEFT JOIN {{ ref('int_return_metrics') }} r
        ON p.product_id = r.product_id
)

SELECT *
FROM product_return_rate
