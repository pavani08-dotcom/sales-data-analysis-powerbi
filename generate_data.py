import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales_data(num_records=50000):
    np.random.seed(42)
    random.seed(42)

    print(f"Generating {num_records} mock sales records...")

    # Data generation setup
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Toys']
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Monitor', 'Tablet'],
        'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Sneakers', 'Hat'],
        'Home & Garden': ['Coffee Maker', 'Blender', 'Vacuum Cleaner', 'Plant Pot', 'Lamp'],
        'Sports': ['Yoga Mat', 'Dumbbells', 'Tennis Racket', 'Basketball', 'Water Bottle'],
        'Toys': ['Action Figure', 'Board Game', 'Lego Set', 'Doll', 'Puzzle']
    }

    # Price ranges by category
    price_ranges = {
        'Electronics': (50, 1500),
        'Clothing': (15, 120),
        'Home & Garden': (20, 300),
        'Sports': (10, 150),
        'Toys': (10, 80)
    }

    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    days_range = (end_date - start_date).days

    data = []

    for i in range(num_records):
        order_id = f"ORD-{i+1:06d}"
        
        # Generate random date
        random_days = random.randint(0, days_range)
        order_date = start_date + timedelta(days=random_days)
        
        customer_id = f"CUST-{random.randint(1, 5000):04d}"
        
        category = random.choice(categories)
        product = random.choice(products[category])
        
        quantity = random.randint(1, 10)
        
        min_price, max_price = price_ranges[category]
        unit_price = round(random.uniform(min_price, max_price), 2)
        
        # Introduce some "dirty" data intentionally for the cleaning phase
        # 1. Missing CustomerID (2% chance)
        if random.random() < 0.02:
            customer_id = np.nan
        
        # 2. Negative quantity (1% chance)
        if random.random() < 0.01:
            quantity = -quantity
            
        # 3. Missing UnitPrice (1.5% chance)
        if random.random() < 0.015:
            unit_price = np.nan

        data.append([order_id, order_date, customer_id, product, category, quantity, unit_price])

    # Create DataFrame
    columns = ['OrderID', 'Date', 'CustomerID', 'Product', 'Category', 'Quantity', 'UnitPrice']
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    output_file = 'raw_sales_data.csv'
    df.to_csv(output_file, index=False)
    print(f"Successfully generated {output_file} with {len(df)} records.")

if __name__ == "__main__":
    # Generate a bit more than 50,000 to be safe
    generate_sales_data(52438)
