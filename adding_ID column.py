import pandas as pd


# Function to process the file, add the ID column, and save it
def add_id_and_duplicate(input_file, output_file):
    # Load the input CSV file
    df = pd.read_csv(input_file)

    # Duplicate the entries
    df_duplicated = pd.concat([df.copy(), df.copy()], ignore_index=True)

    # Add the 'ID' column with 0 for the first 6752 records and 1 for the next 6752 records
    df_duplicated['ID'] = [0] * 6752 + [1] * 6752

    # Move the 'ID' column to the left of the 'replaced' column
    columns = ['ID'] + [col for col in df_duplicated.columns if col != 'ID']
    df_final = df_duplicated[columns]

    # Save the updated data to a CSV file
    df_final.to_csv(output_file, index=False)

    print(f"Updated data saved to {output_file}")


# Define input and output file paths
input_file = 'sorted_SKKU_data.csv'  # Replace with your actual input file path
output_file = 'final_SKKU_data_with_ID.csv'  # The path where the output CSV will be saved

# Run the function
add_id_and_duplicate(input_file, output_file)
