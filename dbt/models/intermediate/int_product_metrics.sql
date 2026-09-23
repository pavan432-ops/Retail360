SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.subcategory,
    p.brand,

    COUNT(DISTINCT s.order_id) AS total_orders,

    SUM(s.quantity) AS total_units,

    SUM(s.net_sales) AS total_sales,

    SUM(s.quantity * p.cost_price) AS total_cost,

    SUM(s.net_sales) - SUM(s.quantity * p.cost_price) AS gross_profit,

    (
        (SUM(s.net_sales) - SUM(s.quantity * p.cost_price))
        / NULLIF(SUM(s.net_sales), 0)
    ) * 100 AS gross_margin_pct

FROM {{ ref('dim_products') }} p

LEFT JOIN {{ ref('fct_sales') }} s
    ON p.product_id = s.product_id

GROUP BY
    p.product_id,
    p.product_name,
    p.category,
    p.subcategory,
    p.brand