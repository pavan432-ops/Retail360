SELECT
    product_id,
    product_name,
    category,
    subcategory,
    brand,
    cost_price,
    selling_price
FROM {{ ref('stg_products') }}