import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date) -> pd.DataFrame:
    """Henter aksjeprisdata for gitt ticker fra Yahoo Finance
    
    Args:
        ticker (str)
        start_date (str)
        end_date (str)
        
        Returns:
        pd.Dataframe
    """
    
    data = yf.download(ticker, start=start_date, end=end_date)
    
    if data.empty: 
        raise ValueError("Ingen data for gitt ticker og datoer")
        return pd.DataFrame()
    data.reset_index(inplace=True)
    return data
