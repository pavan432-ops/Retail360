SELECT
    customer_id,
    customer_name,
    gender,
    age,
    city,
    state,
    region,
    signup_date,
    segment
FROM {{ ref('stg_customers') }}