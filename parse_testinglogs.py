import re
import csv
from datetime import datetime
import os

# Function to decode a CAN message
def decode_can_message(raw_can_data):
    # Define a regular expression pattern to match the timestamp, CAN interface, message ID, and data payload
    pattern = r'\((.*?)\) (\S+) (\S+)#(.+)'
    match = re.match(pattern, raw_can_data)

    if match:
        timestamp = float(match.group(1))
        utc_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        can_interface = match.group(2)
        message_id_hex = match.group(3)
        data_payload_hex = match.group(4)

        # Convert the hexadecimal message ID to decimal
        message_id_decimal = int(message_id_hex, 16)

        return {
            "UTC Timestamp": utc_time,
            "CAN Interface": can_interface,  # Provide a description here
            "Message ID (Hex)": message_id_hex,
            "Message ID (Decimal)": message_id_decimal,  # Added this line
            "Data Payload (Hex)": data_payload_hex,
            "Data Payload (Decimal)": int(data_payload_hex, 16)
        }
    else:
        return None


# Define the output directory
output_directory = './output/'

# Ensure the output directory exists, create it if necessary
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# Input and output file paths
input_file_path = "./data/testing.log"
output_file_path = os.path.join(output_directory, 'parsed_testinglogs.csv')  # Use a CSV file extension

# Open the input file
with open(input_file_path, "r") as input_file:
    # Read all lines from the input file
    lines = input_file.readlines()

# Create a list to store the decoded data
decoded_data_list = []

# Decode the CAN messages and store them in the list
for line in lines:
    decoded_data = decode_can_message(line.strip())
    if decoded_data:
        decoded_data_list.append(decoded_data)

# Write the decoded data to a CSV file
with open(output_file_path, "w", newline="") as output_file:
    fieldnames = [
        "UTC Timestamp",
        "CAN Interface",
        "Message ID (Hex)",
        "Message ID (Decimal)",
        "Data Payload (Hex)",
        "Data Payload (Decimal)"
    ]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row

    for decoded_data in decoded_data_list:
        writer.writerow(decoded_data)

print(f"Decoded CAN data with descriptions has been written to '{output_file_path}'.")
