import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(override=True)

def get_snowflake_engine():
    engine = create_engine(
        f"snowflake://{os.getenv('SNOWFLAKE_USER')}:{os.getenv('SNOWFLAKE_PASSWORD')}"
        f"@{os.getenv('SNOWFLAKE_ACCOUNT')}/"
        f"{os.getenv('SNOWFLAKE_DATABASE')}/"
        f"{os.getenv('SNOWFLAKE_SCHEMA')}?"
        f"warehouse={os.getenv('SNOWFLAKE_WAREHOUSE')}&"
        f"role={os.getenv('SNOWFLAKE_ROLE')}"
    )
    return engine
