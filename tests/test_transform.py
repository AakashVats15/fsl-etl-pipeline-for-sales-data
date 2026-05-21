import pandas as pd
from pandas.testing import assert_frame_equal

from src.transform import clean_data


def test_clean_data():
    # Sample raw input
    raw_df = pd.DataFrame({
        "Order ID": ["A-1", "A-2"],
        "Amount": ["100", "200"],
        "Profit": ["10", None],
        "Quantity": ["1", "2"],
        "Category": ["Electronics", "Furniture"],
        "Sub-Category": ["Phones", "Chairs"],
        "PaymentMode": ["COD", "Credit Card"]
    })

    # Expected cleaned output
    expected_df = pd.DataFrame({
        "order_id": ["A-1", "A-2"],
        "amount": [100.0, 200.0],
        "profit": [10.0, 0.0],
        "quantity": [1, 2],
        "category": ["Electronics", "Furniture"],
        "sub_category": ["Phones", "Chairs"],
        "payment_mode": ["COD", "Credit Card"]
    })

    # Run transform
    cleaned_df = clean_data(raw_df)

    # Column names match
    assert list(cleaned_df.columns) == list(expected_df.columns)

    # Data types match
    assert cleaned_df.dtypes.to_list() == expected_df.dtypes.to_list()

    # Values match exactly
    assert_frame_equal(cleaned_df, expected_df)