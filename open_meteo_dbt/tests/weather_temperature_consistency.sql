select *
from {{ ref('fct_weather_daily') }}
where not (
    min_temperature <= avg_temperature
    and avg_temperature <= max_temperature
)
