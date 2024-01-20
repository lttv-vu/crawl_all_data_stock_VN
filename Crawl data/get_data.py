## Define the list of tickers
import csv
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

data_array = []

# Đọc file CSV và đưa dữ liệu vào mảng
with open('LIST_NEW.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_array.append(row)

# In data_array
tickers = [row[0] for row in data_array[0:]]

def crawl_stock_data(stock_symbol, start_date, end_date):
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        
        return stock_data
    
    except Exception as e:
        print(f"Lấy dữ liệu lỗi {stock_symbol}: {e}")
        return None

def main():
    # List of stock symbols in the Vietnamese market
    vietnam_stock_symbols = tickers   

    start_date = "2018-01-01"
    end_date = datetime.today()

    # Create an Excel writer
    excel_writer = pd.ExcelWriter("stock_data_vietnam.xlsx", engine="openpyxl")
    
    for symbol in vietnam_stock_symbols:
        print(f"Lấy dữ liệu của mã: {symbol}...")
        stock_data = crawl_stock_data(f"{symbol}.VN", start_date, end_date)
        
        
        if stock_data is not None:
            
            # Write the data to Excel with symbol sheet
            stock_data.to_excel(excel_writer, sheet_name=symbol)
            
            # Write the data to Excel with 1 sheet
            #stock_data.to_excel(excel_writer, sheet_name='Data_Stock')
            
    # Save and close the Excel file
    excel_writer.save()
    excel_writer.close()
    

    

if __name__ == "__main__":
    main()
