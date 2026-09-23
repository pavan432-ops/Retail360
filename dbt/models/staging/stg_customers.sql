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
FROM {{ source('retail360', 'raw_customers') }}