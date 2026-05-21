import os
import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = r"E:\Personal\GitHub\Python Code Repo\fsl-etl-pipeline-for-sales-data"
CLEAN_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "clean_data.csv")


def load_to_postgres(df: pd.DataFrame, table_name: str):

    DB_USER = os.getenv("PG_USER", "postgres")
    DB_HOST = os.getenv("PG_HOST", "localhost")
    DB_PORT = os.getenv("PG_PORT", "5432")
    DB_NAME = os.getenv("PG_DB", "salesdb")
    DB_PASS = "1234"

    connection_string = (
        f"postgresql+pg8000://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    try:
        engine = create_engine(connection_string)
        logging.info("Connected to PostgreSQL successfully.")

        df.to_sql(table_name, engine, if_exists="replace", index=False)
        logging.info(f"Loaded {len(df)} rows into table '{table_name}'.")

    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    logging.info("Starting load step...")

    if not os.path.exists(CLEAN_DATA_PATH):
        logging.error(f"Cleaned data not found at: {CLEAN_DATA_PATH}")
        raise FileNotFoundError("Run transform.py before load.py")

    df_clean = pd.read_csv(CLEAN_DATA_PATH)

    load_to_postgres(df_clean, table_name="sales_cleaned")

    logging.info("Load step completed successfully.")