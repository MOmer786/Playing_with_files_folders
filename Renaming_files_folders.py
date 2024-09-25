import os
import pandas as pd

def revert_folders(data_dir, csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Loop through all the subfolders in the data directory
    for folder_name in os.listdir(data_dir):
        folder_path = os.path.join(data_dir, folder_name)

        # Check if the current path is a folder
        if os.path.isdir(folder_path):
            # Find the corresponding row in the CSV based on subid (folder_name)
            row = df[df['subid'] == folder_name]
            if not row.empty:
                date = row['ODT'].values[0]
                gender = row['SEX'].values[0]
                age = row['AGE'].values[0]

                # Convert the date from MM/DD/YYYY to YYYYMMDD
                try:
                    date_str = pd.to_datetime(date).strftime('%Y%m%d')
                except Exception as e:
                    print(f"Error converting date: {date}, {e}")
                    continue

                # Construct the original folder name
                original_folder_name = f"{folder_name}_{date_str}_{gender}_{age}"

                # Construct the new folder path
                new_folder_path = os.path.join(data_dir, original_folder_name)

                # Rename the folder if the new name doesn't already exist
                if not os.path.exists(new_folder_path):
                    os.rename(folder_path, new_folder_path)
                    print(f"Renamed folder: {folder_name} -> {original_folder_name}")
                else:
                    print(f"Folder with name {original_folder_name} already exists, skipping.")
            else:
                print(f"No matching subid found for folder: {folder_name}")

# Define the directory containing the folders and the CSV file path
data_directory = r"D:\AI_New_DATA\[SKKU]OCT\data"  # Replace with the path to your actual data folder
csv_file = r"D:\AI_New_DATA\updated_SKKU_data_subid_final.csv"  # Replace with the path to your CSV file

# Run the renaming function
revert_folders(data_directory, csv_file)
