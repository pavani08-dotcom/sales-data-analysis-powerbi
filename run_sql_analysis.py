import pandas as pd
import sqlite3
import os

def run_analysis():
    print("Loading cleaned_sales_data.csv into memory...")
    df = pd.read_csv("cleaned_sales_data.csv")
    
    # Create an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    
    # Write the dataframe to the database
    df.to_sql("cleaned_sales_data", conn, index=False)
    
    print("Executing queries from analysis_queries.sql...")
    with open("analysis_queries.sql", "r") as f:
        sql_script = f.read()
        
    # Split queries by semicolon
    queries = [q.strip() for q in sql_script.split(';') if q.strip()]
    
    with open("analysis_results.txt", "w") as out_f:
        for i, query in enumerate(queries):
            print(f"Running query {i+1}...")
            out_f.write(f"--- Query {i+1} ---\n")
            out_f.write(f"{query}\n\n")
            out_f.write("--- Results ---\n")
            
            try:
                result_df = pd.read_sql_query(query, conn)
                out_f.write(result_df.to_string(index=False))
            except Exception as e:
                out_f.write(f"Error executing query: {e}")
            out_f.write("\n\n" + "="*50 + "\n\n")
            
    conn.close()
    print("Analysis complete. Results saved to analysis_results.txt.")

if __name__ == "__main__":
    run_analysis()
