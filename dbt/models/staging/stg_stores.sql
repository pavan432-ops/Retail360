SELECT
    store_id,
    store_name,
    city,
    state,
    region,
    store_type
FROM {{ source('retail360', 'raw_stores') }}