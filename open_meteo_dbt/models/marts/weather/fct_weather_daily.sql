{{ config(materialized='table') }}

select
    cast(observed_at_utc as date) as weather_date,
    avg(temperature)              as avg_temperature,
    min(temperature)              as min_temperature,
    max(temperature)              as max_temperature,
    count(*)                      as record_count
from {{ ref('stg_weather') }}
group by 1
order by 1



