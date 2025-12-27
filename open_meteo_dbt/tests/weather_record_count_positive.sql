select *
from {{ ref('fct_weather_daily') }}
where record_count <= 0
