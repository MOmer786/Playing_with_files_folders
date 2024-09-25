import pandas as pd


# Function to rename 'replaced' to 'subid' and extract the relevant part
def process_subid(input_file, output_file):
    # Load the input CSV file
    df = pd.read_csv(input_file)

    # Rename the 'replaced' column to 'subid' and extract only the ID part (e.g., S000001)
    df = df.rename(columns={'replaced': 'subid'})
    df['subid'] = df['subid'].str.split('_').str[0]

    # Save the updated data to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Updated data saved to {output_file}")


# Define the input and output file paths
input_file = 'final_SKKU_data_with_ID.csv'  # Replace with your actual input file path
output_file = 'updated_SKKU_data_subid_final.csv'  # The path where the output CSV will be saved

# Run the function
process_subid(input_file, output_file)
