import pandas as pd
import psycopg2
from openpyxl import workbook
from openpyxl.workbook import Workbook


def read_file(excel_file):
    excel_data = pd.read_excel(excel_file)
    excel_records = []
    for index, row in excel_data.iterrows():
        excel_value = row["VIN_List"]
        excel_records.append(excel_value)

    print("Data from Test File...")
    count = 0
    for row in excel_records:
        # print(count, row)
        count = count + 1

    return excel_records


def read_reference(excel_file):
    excel_data = pd.read_excel(excel_file)
    excel_records = []
    for index, row in excel_data.iterrows():
        excel_value = row[['Data', 'VIN_NUM']]
        excel_records.append(excel_value)

    print("Data from Reference File...")
    count = 0
    for row in excel_records:
        # print(count, row)
        count = count + 1

    return excel_records

def check_matches(reference, test):
    matching_count = 0
    wb = Workbook()
    # Select the active worksheet
    ws = wb.active
    output = []
    ws.append("Moment")
    record_count = {}
    for row in reference:

        if row['VIN_NUM'] in test:
            if row['VIN_NUM'] in record_count:
                record_count[row['VIN_NUM']] += 1
            else:
                record_count[row['VIN_NUM']] = 1
            matching_count = matching_count + 1
            print(matching_count, " -- ", row['Data'])
            # ws.append(matching_count, row['Data'])
            # ws.append(row['Data'])
            output.append(row['Data'])

        # else:
        #     vin_dict[row['VIN_NUM']] = 1
    occurrences = {}
    for record, count in record_count.items():
        occurrences[record] = count
    # wb.save('output.xlsx')
    # wb.save(new_file)
    print(matching_count)
    print("Occurrences:", occurrences)
    print("Output Size -- ", len(output))

    for index, record in enumerate(output, start=1):
        ws.cell(row=index, column=1, value= record)

    wb.save("output_1.xlsx")


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


    # Print the count of matching records
    print("Total matching records:", matching_count)

# Example usage:
excel_file_1 = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/test_final.xlsx"
excel_file_2 = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/ISIS_reference.xlsx"

database_connection = psycopg2.connect(
    dbname="innovation_1",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
database_table = "isis_reference_1"
# database_records = fetch_database_records(database_connection, database_table)
# print(database_records)
# check_records_in_database(excel_file_1, database_records, excel_file_2)
# read_file(excel_file_1)
reference_data = []
test_data = []
# read_reference(excel_file_2)
reference_data = read_reference(excel_file_2)
test_data = read_file(excel_file_1)
# print(test_data)
# print(reference_data)
check_matches(reference_data, test_data)
database_connection.close()
