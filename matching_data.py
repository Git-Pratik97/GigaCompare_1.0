import pandas as pd
import openpyxl

def find_matching_rows(primary_file, secondary_file, primary_column, secondary_columns):
    # Read data from Excel files using openpyxl engine
    primary_data = pd.read_excel(primary_file, sheet_name='Sheet1', engine='openpyxl')
    secondary_data = pd.read_excel(secondary_file, sheet_name='Sheet1', engine='openpyxl')

    # Iterate through each value in the primary column
    for value in primary_data[primary_column]:
        # Iterate through each secondary column to check for matches
        for column in secondary_columns:
            # Find rows where the value matches in any of the secondary columns
            matched_rows = secondary_data[secondary_data[column] == value]
            # Print the matched rows
            if not matched_rows.empty:
                print(f"Matching rows for value '{value}' in {column}:")
                print(matched_rows)
            else:
                print("No Matching Data")


# Example usage:
primary_file = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/test_final_1.xls"
secondary_file = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/reference_1.xls"
primary_column = "VIN_List"  # Column to search from in the primary file
secondary_columns = ["VIN_NUM", "Data_1"]
  # Columns to search in the secondary file

find_matching_rows(primary_file, secondary_file, primary_column, secondary_columns)
