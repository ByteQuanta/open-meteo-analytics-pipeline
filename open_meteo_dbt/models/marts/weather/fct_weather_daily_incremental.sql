{{  
  config(
    materialized='incremental',
    unique_key='weather_date'
  ) 
}}

with daily_weather as (

    select
        cast(observed_at_utc as date) as weather_date,
        avg(temperature)              as avg_temperature,
        min(temperature)              as min_temperature,
        max(temperature)              as max_temperature,
        count(*)                      as record_count
    from {{ ref('stg_weather') }}

    {% if is_incremental() %}
        where cast(observed_at_utc as date) > (
            select max(weather_date) from {{ this }}
        )
    {% endif %}

    group by 1
)

select *
from daily_weather


