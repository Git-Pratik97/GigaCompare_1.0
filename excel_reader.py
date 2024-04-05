import pandas as pd

def display_excel_data(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Display the data
        print("Data from Excel file:")
        for index, row in df.iterrows():
            row_count = index + 1  # Adding 1 to make it start from 1 instead of 0
            print(f"Row {row_count}: {row}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage:
file_path = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/reference_2.xlsx"  # Change this to the path of your Excel file
display_excel_data(file_path)
