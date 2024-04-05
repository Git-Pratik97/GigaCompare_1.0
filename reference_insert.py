import pandas as pd
import psycopg2
from psycopg2 import Error

def excel_to_postgres(file_path, table_name, connection_string):
    conn = None
    try:
        print(file_path)
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{column} TEXT' for column in df.columns])})"
        cursor.execute(create_table_query)
        conn.commit()

        # Insert data into the table
        for index, row in df.iterrows():
            insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s']*len(row))})"
            cursor.execute(insert_query, tuple(row))
            conn.commit()

        print("Data inserted successfully.")

    except FileNotFoundError:
        print("File not found.")
    except Error as e:
        print("An error occurred:", e)
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed.")

# Example usage:
file_path = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/ISIS_reference_1.xlsx"  # Change this to the path of your Excel file
table_name = "ISIS_REFERENCE_1"   # Change this to the desired table name in your PostgreSQL database
connection_string = "dbname='innovation_1' user='postgres' host='localhost' password='root'"

excel_to_postgres(file_path, table_name, connection_string)
