import logging
from load_to_snowflake import load_mysql_to_snowflake

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    logging.info("🚀 ETL Stage 2.2 started")
    load_mysql_to_snowflake("weather_raw")
    logging.info("🏁 ETL Stage 2.2 finished successfully")

if __name__ == "__main__":
    run()
