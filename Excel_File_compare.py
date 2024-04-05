import pandas as pd
import psycopg2

def fetch_database_records(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()
    cursor.close()
    # return [record[11] for record in records]  # Assuming the first column contains the records
    return records

def check_records_in_database(excel_file_1, database_records, excel_file_2):
    # Read records from Excel file
    excel_data_1 = pd.read_excel(excel_file_1)
    # excel_data_2 = pd.read.excel(excel_file_2)

    # records_file_1 = [record_1['VIN_NUM'] for record_1 in database_records]
    # records_file_2 = [record_2[0] for record_2 in  ]

    # Initialize count of matching records
    matching_count = 0
    excel_1_data = []
    excel_2_data = []

    # Iterate over each record in the Excel file
    for index, row in excel_data_1.iterrows():
        # Extract the value from the first column in the Excel file
        excel_value = row['VIN_List']
        excel_1_data.append(excel_value)
        # Check if the record exists in the database records
        # if excel_value in records:
        #     # print(database_records[0])
        #     matching_count += 1
        #     print(matching_count, "---", [record[3] for record in database_records])
        #     print("Match found in database:", excel_value , matching_count, "\n\n")

    for index, row in excel_data_2.iterrows():
        # Extract the value from the first column in the Excel file
        excel_value = row[['VIN_NUM', 'Data_4']]
        # excel_2_data.append(excel_value)
        print(excel_value)
        # Check if the record exists in the database records
        # if excel_value in records:
        #     # print(database_records[0])
        #     matching_count += 1
        #     print(matching_count, "---", [record[3] for record in database_records])
        #     print("Match found in database:", excel_value , matching_count, "\n\n")

    # Print the count of matching records
    print("Total matching records:", matching_count)

# Example usage:
excel_file_1 = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/test_final.xlsx"
excel_file_2 = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/isis_reference_1.xlsx"

database_connection = psycopg2.connect(
    dbname="innovation_1",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
database_table = "isis_reference_1"
database_records = fetch_database_records(database_connection, database_table)
# print(database_records)
check_records_in_database(excel_file_1, database_records, excel_file_2)
database_connection.close()
