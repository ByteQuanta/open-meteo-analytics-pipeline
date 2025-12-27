import logging
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from snowflake_conn import get_snowflake_engine

load_dotenv(override=True)

logger = logging.getLogger(__name__)

def load_mysql_to_snowflake(table_name: str):
    mysql_engine = create_engine(
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
    )

    logger.info(f"📤 Reading data from MySQL table: {table_name}")
    df = pd.read_sql(f"SELECT * FROM {table_name}", mysql_engine)

    sf_engine = get_snowflake_engine()

    logger.info("📥 Loading data into Snowflake (RAW layer)")
    df.to_sql(
        table_name.upper(),
        sf_engine,
        if_exists="replace",
        index=False
    )

    logger.info(f"✅ Loaded {len(df)} rows into Snowflake RAW.{table_name.upper()}")
