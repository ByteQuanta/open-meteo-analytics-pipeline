with source as (

    select
        timestamp                                  as observed_at_utc,
        convert_timezone(
            'UTC',
            'Europe/Istanbul',
            timestamp
        )                                          as observed_at_local,
        temperature
    from {{ source('raw', 'weather_raw') }}

)

select *
from source


