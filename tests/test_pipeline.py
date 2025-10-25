from src.pipeline import fetch_stock_data
import pandas as pd
import pytest

def test_fetch_stock_data():
    df = fetch_stock_data('AAPL', '2023-01-01', '2023-02-01')
    assert isinstance(df, pd.DataFrame)

def test_fetch_stock_data_columns():
    df = fetch_stock_data('AAPL', '2023-01-01', '2023-02-01')
    expected_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    assert all(col in df.columns for col in expected_columns), f"Manglende kolonner: {set(expected_columns) - set(df.columns)}"

def test_fetch_stock_data_not_empty():
    df = fetch_stock_data('AAPL', '2023-01-01', '2023-02-01')
    assert not df.empty

def test_fetch_stock_data_valueerror():
    with pytest.raises(ValueError, match="Ingen data for gitt ticker og datoer"):
        fetch_stock_data('ASDASD', '2023-01-01', '2023-02-01')

def test_fetch_stock_data_date_type():
    df = fetch_stock_data('AAPL', '2023-01-01', '2023-02-01')
    assert pd.api.types.is_datetime64_any_dtype(df['Date'])

