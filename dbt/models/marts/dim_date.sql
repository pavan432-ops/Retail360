WITH RECURSIVE date_spine AS (

    SELECT CAST('2025-01-01' AS DATE) AS date_day
    UNION ALL

    SELECT DATE_ADD(date_day, INTERVAL 1 DAY)
    FROM date_spine
    WHERE date_day < '2026-12-31'

)

SELECT
    date_day,

    YEAR(date_day) AS year,

    QUARTER(date_day) AS quarter,

    MONTH(date_day) AS month,

    MONTHNAME(date_day) AS month_name,

    DATE_FORMAT(date_day, '%b %Y') AS month_year,

    YEAR(date_day) * 100 + MONTH(date_day) AS year_month_sort,

    DAY(date_day) AS day,

    DAYOFWEEK(date_day) AS day_of_week,

    DAYNAME(date_day) AS day_name,

    CASE
        WHEN DAYOFWEEK(date_day) IN (1, 7) THEN 1
        ELSE 0
    END AS is_weekend

FROM date_spine