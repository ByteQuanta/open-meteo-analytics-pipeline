from sqlalchemy import create_engine
from config import MYSQL_CONFIG

def load_to_mysql(df, table_name: str):
    engine = create_engine(
        f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}"
        f"@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}"
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )
