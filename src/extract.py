import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Base paths
BASE_DIR = r"E:\Personal\GitHub\Python Code Repo\fsl-etl-pipeline-for-sales-data"
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "raw_data.csv")


def extract_raw_data(file_path: str) -> pd.DataFrame:
    """
    Extract raw sales data from CSV file.

    Parameters
    ----------
    file_path : str
        Full path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded raw dataset.
    """
    logging.info(f"Starting data extraction from: {file_path}")

    if not os.path.exists(file_path):
        logging.error(f"File not found at: {file_path}")
        raise FileNotFoundError(f"Raw data file does not exist: {file_path}")

    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully extracted {len(df)} rows.")
        return df

    except Exception as e:
        logging.error(f"Error while reading CSV: {e}")
        raise


if __name__ == "__main__":
    df_raw = extract_raw_data(RAW_DATA_PATH)
    print(df_raw.head())
