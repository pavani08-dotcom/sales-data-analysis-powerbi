import pandas as pd
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(input_file='raw_sales_data.csv', output_file='cleaned_sales_data.csv'):
    logging.info(f"Starting data cleaning process for {input_file}...")
    
    try:
        # Load the data
        df = pd.read_csv(input_file)
        initial_rows = len(df)
        logging.info(f"Loaded {initial_rows} records.")
        
        # 1. Handle Missing Values
        # For CustomerID, we can drop rows with missing IDs as they are essential for customer behavior analysis
        missing_customers = df['CustomerID'].isnull().sum()
        df = df.dropna(subset=['CustomerID'])
        logging.info(f"Dropped {missing_customers} rows with missing CustomerID.")
        
        # For UnitPrice, we can impute the missing values with the median price of the same Product
        missing_prices = df['UnitPrice'].isnull().sum()
        df['UnitPrice'] = df.groupby('Product')['UnitPrice'].transform(lambda x: x.fillna(x.median()))
        logging.info(f"Imputed {missing_prices} missing UnitPrice values with product medians.")
        
        # 2. Correct Data Types
        # Convert Date string to datetime object
        df['Date'] = pd.to_datetime(df['Date'])
        logging.info("Converted 'Date' column to datetime.")
        
        # 3. Handle Anomalies
        # Convert negative quantities to positive (assuming it was an entry error)
        negative_quantities = (df['Quantity'] < 0).sum()
        df['Quantity'] = df['Quantity'].abs()
        logging.info(f"Corrected {negative_quantities} negative Quantity values.")
        
        # 4. Feature Engineering
        # Calculate TotalRevenue for each record
        df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
        logging.info("Calculated 'TotalRevenue' feature.")
        
        # Extract Month and Year for easier time-series analysis in SQL or Power BI
        df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
        logging.info("Extracted 'YearMonth' feature.")
        
        # 5. Remove any duplicates just in case
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            df = df.drop_duplicates()
            logging.info(f"Removed {duplicates} duplicate rows.")
        
        # Save the cleaned dataset
        final_rows = len(df)
        df.to_csv(output_file, index=False)
        logging.info(f"Data cleaning complete. Saved {final_rows} records to {output_file}.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    clean_data()
