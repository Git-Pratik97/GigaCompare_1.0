import pandas as pd

def split_excel_file(input_file, output_prefix, chunk_size=65000):
    # Read the original Excel file
    df = pd.read_excel(input_file)

    # Calculate the number of chunks
    num_chunks = (len(df) - 1) // chunk_size + 1

    # Split the DataFrame into chunks
    chunks = [df[i*chunk_size:(i+1)*chunk_size] for i in range(num_chunks)]

    # Save each chunk as a separate Excel file
    for i, chunk in enumerate(chunks):
        output_file = f"{output_prefix}_{i+1}.xlsx"
        chunk.to_excel(output_file, index=False)
        print(f"Chunk {i+1} saved as {output_file}")

# Example usage:
input_file = "C:/Users/pratikam/Downloads/Innovation_at_sales/files/reference_2.xlsx"  # Change this to the path of your input Excel file
output_prefix = "output_chunk"  # Prefix for the output Excel file names
split_excel_file(input_file, output_prefix)
