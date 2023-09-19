import pandas as pd
import os

# Load the CSV file
input_file_path = "output/parsed_testinglogs.csv"

df = pd.read_csv(input_file_path)

# Create a directory to save the individual CSV files (optional)
output_dir = "individual_csv_files"
os.makedirs(output_dir, exist_ok=True)

# Get unique counts for 'CAN Interface' and save to a CSV file
unique_can_interface_counts = df['CAN Interface'].value_counts().reset_index()
unique_can_interface_counts.columns = ['CAN Interface', 'Count']
unique_can_interface_counts.to_csv(os.path.join(output_dir, 'unique_CAN_interface.csv'), index=False)

# Get unique counts for 'Message ID (Hex)' and save to a CSV file
unique_message_id_counts = df['Message ID (Hex)'].value_counts().reset_index()
unique_message_id_counts.columns = ['Message ID (Hex)', 'Count']
unique_message_id_counts.to_csv(os.path.join(output_dir, 'unique_message_ID_hex.csv'), index=False)

# Get unique counts for 'Data Payload (Hex)' and save to a CSV file
unique_data_payload_counts = df['Data Payload (Hex)'].value_counts().reset_index()
unique_data_payload_counts.columns = ['Data Payload (Hex)', 'Count']
unique_data_payload_counts.to_csv(os.path.join(output_dir, 'unique_data_payload_hex.csv'), index=False)

print("Unique counts CSV files have been generated.")
