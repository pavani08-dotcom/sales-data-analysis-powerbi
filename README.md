# Sales Data Analysis Dashboard Project

This project demonstrates an end-to-end data analysis workflow, starting from mock data generation to data cleaning, SQL querying, and finally, data visualization. It simulates a real-world scenario of analyzing over 50,000 sales records to uncover business insights.

## Project Highlights
* **Analyzed 50,000+ sales records** using Python and Pandas.
* **Performed data cleaning and preprocessing** to improve data quality, handling missing values, anomalies, and feature engineering.
* **Prepared for interactive Power BI dashboards** showing sales trends and customer behavior.

## Tools Used
* **Python**: Used for programmatic data generation.
* **Pandas**: Used for robust data cleaning, missing value imputation, and feature engineering.
* **SQL**: Used for querying the cleaned dataset to extract high-level KPIs and behavioral metrics.
* **Power BI**: (Instructions provided) Used for building interactive and dynamic data visualizations.

## Project Structure

* `generate_data.py`: A Python script that creates `raw_sales_data.csv` with 50,000+ rows of transactional data, complete with intentional "dirty" data (missing IDs, negative quantities) to simulate real-world data issues.
* `data_cleaning.py`: A Python script that uses Pandas to read the raw data, perform data cleaning (handling nulls, correcting data types, deduping), engineer new features (TotalRevenue, YearMonth), and output `cleaned_sales_data.csv`.
* `analysis_queries.sql`: A collection of SQL queries designed to answer key business questions (e.g., Monthly Sales Trends, Top Selling Categories, Customer Lifetime Value).
* `power_bi_dashboard_guide.md`: A step-by-step guide on how to ingest the cleaned data into Power BI, create DAX measures, and build the interactive dashboard.

## How to Run the Project

1. **Prerequisites**: Ensure you have Python installed along with the `pandas` and `numpy` libraries.
   ```bash
   pip install pandas numpy
   ```

2. **Generate the Data**: Run the data generation script to create your raw dataset.
   ```bash
   python generate_data.py
   ```

3. **Clean the Data**: Run the data cleaning script to process the raw dataset and prepare it for analysis.
   ```bash
   python data_cleaning.py
   ```

4. **Analyze (SQL)**: You can import the resulting `cleaned_sales_data.csv` into a SQL database (like PostgreSQL, MySQL, or SQLite) and run the queries provided in `analysis_queries.sql`.

5. **Visualize (Power BI)**: Follow the instructions in `power_bi_dashboard_guide.md` to connect Power BI to the cleaned CSV and build your dashboard.

## Outcome
By completing this project, you will have a robust portfolio piece demonstrating your ability to handle the entire data pipeline—from raw, messy data to clean, actionable insights visualized in a professional dashboard.
