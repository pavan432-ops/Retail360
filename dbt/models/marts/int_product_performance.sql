WITH benchmarks AS (

    SELECT
        AVG(total_sales) AS avg_product_sales,
        AVG(gross_margin_pct) AS avg_product_margin

    FROM {{ ref('int_product_metrics') }}

    WHERE total_sales IS NOT NULL
      AND gross_margin_pct IS NOT NULL
),

product_performance AS (

    SELECT
        p.*,

        b.avg_product_sales,
        b.avg_product_margin,

        CASE
            WHEN p.total_sales IS NULL
                 OR p.gross_margin_pct IS NULL
                THEN 'Data Quality Review'

            WHEN p.total_sales >= b.avg_product_sales
                 AND p.gross_margin_pct >= b.avg_product_margin
                THEN 'High Sales - High Margin'

            WHEN p.total_sales >= b.avg_product_sales
                 AND p.gross_margin_pct < b.avg_product_margin
                THEN 'High Sales - Low Margin'

            WHEN p.total_sales < b.avg_product_sales
                 AND p.gross_margin_pct >= b.avg_product_margin
                THEN 'Low Sales - High Margin'

            ELSE 'Low Sales - Low Margin'
        END AS performance_segment

    FROM {{ ref('int_product_metrics') }} p

    CROSS JOIN benchmarks b
)

SELECT *
FROM product_performance