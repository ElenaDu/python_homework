import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT l.line_item_id, l.quantity, p.product_id, p.product_name, p.price
                       FROM line_items l JOIN products p
                       ON l.product_id = p.product_id                         
    """
    try:
        df = pd.read_sql_query(sql_statement, conn)
        print("Initial DataFrame:")
        print(df.head())
        df["total"] = df["quantity"]*df["price"]
        print("DataFrame with 'total' column:")
        print(df.head())
        grouped_df = df.groupby("product_id").agg({"line_item_id":"count", "total": "sum", "product_name": "first"}).reset_index()
        print("Grouped DataFrame")
        print(grouped_df.head())
        print("Grouped and Sorted DataFrame")
        grouped_df = grouped_df.sort_values(by='product_name')
        print(grouped_df.head())
        grouped_df.to_csv("order_summary.csv", index=False)
    except sqlite3.Error as e:
        print(f"An error occurred while working with the database: {e}") 
