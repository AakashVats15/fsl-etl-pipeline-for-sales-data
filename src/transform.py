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
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "clean_data.csv")


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw sales data.

    Steps:
    - Strip column names
    - Remove duplicates
    - Fix data types
    - Handle missing values
    - Standardize category fields
    - Validate numeric columns
    """

    logging.info("Starting data cleaning...")

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    logging.info(f"Removed {before - len(df)} duplicate rows.")

    # Fix data types
    numeric_cols = ["Amount", "Profit", "Quantity"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Handle missing values
    df["Category"] = df["Category"].fillna("Unknown")
    df["Sub-Category"] = df["Sub-Category"].fillna("Unknown")
    df["PaymentMode"] = df["PaymentMode"].fillna("Unknown")

    # Standardize text fields
    df["Category"] = df["Category"].str.title()
    df["Sub-Category"] = df["Sub-Category"].str.title()
    df["PaymentMode"] = df["PaymentMode"].str.upper()

    # Remove rows with invalid numeric values
    df = df[df["Quantity"] > 0]
    df = df[df["Amount"] >= 0]
    df = df[df["Profit"].notna()]

    logging.info("Data cleaning completed successfully.")
    return df


def save_clean_data(df: pd.DataFrame, output_path: str):
    """Save cleaned data to processed folder."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logging.info(f"Cleaned data saved to: {output_path}")


if __name__ == "__main__":
    # Load raw data
    df_raw = pd.read_csv(RAW_DATA_PATH)

    # Clean it
    df_clean = clean_sales_data(df_raw)

    # Save cleaned output
    save_clean_data(df_clean, PROCESSED_DATA_PATH)

    print(df_clean.head())