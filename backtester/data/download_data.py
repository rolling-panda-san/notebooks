import yfinance as yf
import pandas as pd
import os

# Define the list of tickers for different asset classes
TICKERS = {
    "Equity": ["ES=F", "NQ=F", "YM=F", "RTY=F"],
    "Bond": ["ZB=F", "ZN=F", "ZF=F", "ZT=F"],
    "FX": ["6E=F", "6J=F", "6B=F", "6A=F", "6C=F", "6S=F"],
    "Commodity": ["CL=F", "GC=F", "SI=F", "HG=F", "NG=F", "RB=F", "HO=F", "PA=F", "PL=F"],
}

# Define the data directory
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def download_data():
    """
    Downloads historical data for the specified tickers and saves it to CSV files.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    all_tickers = [ticker for asset_class in TICKERS.values() for ticker in asset_class]

    for ticker in all_tickers:
        print(f"Downloading data for {ticker}...")
        try:
            data = yf.download(ticker, start="2000-01-01", end="2023-12-31", auto_adjust=False)
            if not data.empty:
                file_path = os.path.join(DATA_DIR, f"{ticker}.csv")
                data["Adj Close"].to_csv(file_path)
                print(f"Data for {ticker} saved to {file_path}")
            else:
                print(f"No data found for {ticker}")
        except Exception as e:
            print(f"Failed to download data for {ticker}: {e}")

if __name__ == "__main__":
    download_data()
