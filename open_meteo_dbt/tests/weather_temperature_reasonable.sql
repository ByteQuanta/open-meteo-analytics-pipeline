select *
from {{ ref('fct_weather_daily') }}
where min_temperature < -80
   or max_temperature > 60
