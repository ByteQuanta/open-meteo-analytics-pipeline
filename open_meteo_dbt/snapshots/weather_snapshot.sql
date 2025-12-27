{% snapshot weather_snapshot %}

{{
    config(
      target_schema='SNAPSHOTS',
      unique_key='timestamp',
      strategy='check',
      check_cols=['temperature']
    )
}}

select
    timestamp,
    temperature
from {{ ref('stg_weather') }}

{% endsnapshot %}
