# Open Meteo Analytics Pipeline (dbt + Snowflake)

## Overview

This project implements an analytics engineering pipeline that transforms raw weather API data into reliable, analytics-ready models using dbt and Snowflake.

The primary goal is to separate unstable upstream data from downstream analytical use cases by applying defensive modeling, testing, and historization patterns commonly used in production analytics environments.

---

## Business Context

Raw weather API data is not suitable for direct analytical use due to potential issues such as:
- Missing or delayed timestamps
- Duplicate records
- Schema or data consistency changes
- Upstream instability beyond analytics team control

This project addresses these challenges by providing a clean, tested, and historized analytics layer that enables reliable daily weather analysis without exposing downstream users to raw data volatility.

The resulting models are designed to support:
- Time-series trend analysis
- Historical comparisons
- BI dashboards and exploratory analytics

---

## Architecture Overview

The pipeline follows a layered analytics engineering approach:

### 1. Source Layer
- Raw weather data ingested from an external API
- Treated as untrusted input
- Explicitly modeled via dbt `source()` definitions

### 2. Staging Layer (`stg_weather`)
- Minimal transformations
- Column selection and type normalization
- Serves as a stable contract for downstream models

### 3. Mart Layer
- `fct_weather_daily`
  - Full-refresh daily aggregation
  - Serves as a baseline, deterministic fact table

- `fct_weather_daily_incremental`
  - Incremental daily aggregation
  - Optimized for performance and scalability
  - Demonstrates incremental modeling patterns in dbt

### 4. Snapshot Layer
- Implements SCD Type 2 snapshotting on weather records
- Preserves historical changes in source data
- Enables point-in-time analysis and auditability

---

## Incremental Modeling Strategy

The incremental fact model aggregates data at a daily grain and appends new records based on date-level filtering.

This approach demonstrates:
- Incremental materialization patterns
- Performance-aware analytics design
- Trade-offs between simplicity and robustness

> Note: The project intentionally highlights assumptions and limitations of naive incremental strategies as part of its learning and evaluation scope.

---

## Data Quality & Testing

The project includes comprehensive data tests to enforce analytical trust:

- `not_null` constraints on key metrics
- `unique` constraints on daily grain
- Custom tests for:
  - Temperature consistency (min ≤ avg ≤ max)
  - Reasonable temperature bounds
  - Positive record counts

These tests ensure downstream consumers can rely on the modeled data without re-validating basic assumptions.

---

## Documentation & Discoverability

- dbt Docs used for model lineage visualization
- Exposure defined for downstream dashboard usage
- Clear DAG representation of data dependencies

This supports collaboration between analytics engineers, analysts, and stakeholders.

---

## Technologies Used

- **dbt** (models, tests, snapshots, exposures)
- **Snowflake** (cloud data warehouse)
- **SQL**
- **Open-Meteo API** (data source)

---

## Design Philosophy

This project prioritizes:
- Clear separation of concerns
- Defensive analytics modeling
- Transparency of assumptions
- Maintainability over premature optimization

It is intentionally designed as a realistic analytics engineering system rather than a purely academic exercise.

---

## Future Improvements

Potential next steps include:
- Source freshness monitoring
- Duplicate detection at ingestion
- More resilient incremental strategies (rolling windows or update-based logic)
- Snapshot-driven downstream models
- Stronger exposure contracts aligned with BI tools

---

## 🚀 How to Run the Project Locally

### Prerequisites
- Python 3.10+
- Conda or virtualenv
- Access to a Snowflake account
- `dbt-core` and `dbt-snowflake`

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/open_meteo_pipeline.git
cd open_meteo_pipeline
```

### 2. Set up Python environment
```bash
conda create -n open_meteo python=3.10
conda activate open_meteo
pip install -r requirements.txt
```

### 3. Configure dbt profile
This project includes a profiles.yml.example file.

Steps:
- Copy the example file
- Rename it to profiles.yml
- Fill in your Snowflake credentials

```bash
cp profiles.yml.example ~/.dbt/profiles.yml
```
profiles.yml and .env files are intentionally excluded from version control.

### 4. Run dbt models and tests
```bash
cd open_meteo_dbt
dbt debug
dbt run
dbt test
```

### 5. Explore dbt documentation
```bash
dbt docs generate
dbt docs serve
```

## Repository Structure (Simplified)
```
open_meteo_pipeline/
├── open_meteo_dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   └── exposures/
│   ├── snapshots/
│   ├── tests/
│   └── dbt_project.yml
├── src/                # Python ingestion & loading
├── profiles.yml.example
├── requirements.txt
└── README.md
```

## Author
Designed and implemented by an analytics engineering practitioner with a strong focus on building reliable, production-oriented data systems and applying real-world defensive modeling practices.

## Data Source
Weather data is sourced from the **Open-Meteo API**, an open and free weather data service.

- Provider: Open-Meteo (https://open-meteo.com/)
- Data type: Historical and near real-time weather observations
- Access: Public API (no authentication required)

The raw API output is ingested as-is and treated as **untrusted upstream data**, meaning:
- Records may arrive late or be missing
- Duplicate timestamps may exist
- Data corrections may occur retroactively

All downstream transformations assume no guarantees from the source and enforce reliability through modeling, testing, and historization.

