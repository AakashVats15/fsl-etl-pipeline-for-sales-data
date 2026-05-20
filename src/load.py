import os
import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Base paths
BASE_DIR = r"E:\Personal\GitHub\Python Code Repo\fsl-etl-pipeline-for-sales-data"
CLEAN_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "clean_data.csv")


def load_to_postgres(df: pd.DataFrame, table_name: str):
    """
    Load cleaned DataFrame into PostgreSQL table.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataset to load.
    table_name : str
        Target table name in PostgreSQL.
    """

    # Read DB credentials from environment variables
    DB_USER = os.getenv("PG_USER", "postgres")
    DB_PASS = os.getenv("PG_PASS", "password")
    DB_HOST = os.getenv("PG_HOST", "localhost")
    DB_PORT = os.getenv("PG_PORT", "5432")
    DB_NAME = os.getenv("PG_DB", "salesdb")

    connection_string = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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