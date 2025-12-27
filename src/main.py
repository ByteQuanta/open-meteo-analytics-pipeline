from extract import extract_weather
from load import load_to_mysql
import os
import logging

# Logging ayarı (development için ideal)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("MYSQL_DB FROM PYTHON:", os.getenv("MYSQL_DB"))

def run():
    logging.info("🚀 ETL Stage 1 started")

    df = extract_weather()
    logging.info(f"📥 Extracted {len(df)} rows from Open-Meteo")

    load_to_mysql(df, "weather_raw")
    logging.info("✅ Data successfully loaded into MySQL (weather_raw)")

    logging.info("🏁 ETL Stage 1 finished successfully")

if __name__ == "__main__":
    run()

