import sys
import time
from pathlib import Path
import yfinance as yf
import os
import datetime
import pandas as pd

# Connect context back to project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from config.settings import RAW_MARKET_DIR, TARGET_TICKERS

class MarketDataFetcher:
    """Automates real-world historical OHLCV data extraction for global markets using yfinance."""
    
    def __init__(self):
        RAW_MARKET_DIR.mkdir(parents=True, exist_ok=True)
        # CRITICAL FIX: Define universe so main.py can seamlessly loop through it
        self.universe = TARGET_TICKERS
        
    def fetch_ticker_data(self, ticker: str) -> bool:
        """
        Downloads daily historical data securely using yfinance.
        """
        clean_ticker = ticker.strip().upper()
        output_path = RAW_MARKET_DIR / f"{clean_ticker}.csv"
        
        print(f"[FETCHING] Querying secure yfinance channel for {clean_ticker}...")
        
        try:
            # Restrict period to 2y for realistic active tracking and stability metrics
            ticker_obj = yf.Ticker(clean_ticker)
            df = ticker_obj.history(period="2y")
            
            # Fallback wrapper if the primary history stream is empty
            if df.empty:
                df = yf.download(clean_ticker, period="2y", progress=False)
                
            if df.empty:
                print(f"[ERROR] Asset validation failed or no data returned for '{clean_ticker}'.")
                return False
                
            # Flatten the index so 'Date' becomes a standard column for our csv_loader
            df.reset_index(inplace=True)
            
            # Format the Date column to YYYY-MM-DD cleanly
            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
            
            # Save cleanly to CSV without the pandas index column
            df.to_csv(output_path, index=False)
            print(f"[SUCCESS] Saved raw data file directly to: {output_path}")
            return True
            
        except Exception as e:
            print(f"[CRITICAL] Unexpected data stream collapse: {e}")
            return False

    def batch_sync_universe(self):
        print("\n[SYSTEM] Initiating Smart Cache Data Synchronization...")
        
        # 1. Get today's exact date
        today = datetime.datetime.now().date()
        
        for ticker in self.universe:
            # Adjust this path if your folders are structured differently
            filepath = f"data/raw_market/{ticker}.csv"
            
            # 2. Check if the file already exists
            if os.path.exists(filepath):
                # 3. Check what day the file was last modified
                file_timestamp = os.path.getmtime(filepath)
                file_date = datetime.datetime.fromtimestamp(file_timestamp).date()
                
                # 4. If it was downloaded today, SKIP the network request
                if file_date == today:
                    print(f"[CACHE] Skipping {ticker}: Up-to-date data already exists for today.")
                    continue 

            # 5. If the file doesn't exist OR is from yesterday, download new data
            print(f"[FETCHING] Downloading latest yfinance data for {ticker}...")
            
            try:
                ticker_obj = yf.Ticker(ticker)
                df = ticker_obj.history(period="2y")
                
                if not df.empty:
                    df.to_csv(filepath)
                    print(f"  -> [SUCCESS] Saved to cache.")
                else:
                    print(f"  -> [ERROR] No data returned for {ticker}.")
            except Exception as e:
                print(f"  -> [FAILED] Network error for {ticker}: {e}")

if __name__ == "__main__":
    fetcher = MarketDataFetcher()
    fetcher.batch_sync_universe()
