import openpyxl
import pandas as pd

def read_excel_file(file_path):
    try:
        # Load the workbook
        workbook = openpyxl.load_workbook(file_path, data_only=True)
        # Get the active sheet
        sheet = workbook.active
        # Extract data from the sheet
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        print(df)
    except Exception as e:
        print("Error:", e)


# Example usage:
file_path = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/reference_3.xlsx"
read_excel_file(file_path)
