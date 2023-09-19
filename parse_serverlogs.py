import pandas as pd
import re
from datetime import datetime
import os

# Define regular expressions to extract information from log entries
log_pattern = r'(\S+) - - \[([^\]]+)\] "(\S+) ([^"]+)" (\d+) (\d+) "([^"]+)" "([^"]+)" "([^"]+)" (\S+) (\S+)'

# Create a list to store dictionaries representing parsed log entries
parsed_log_entries = []

# Open the log file and parse its contents
with open('./data/serverlogs.log', 'r') as file:
    for line in file:
        match = re.match(log_pattern, line)
        if match:
            ip_address, timestamp, request_method, url, response_code, response_size, _, user_agent, _, request_successful, request_failed = match.groups()

            # Parse the timestamp into the desired format
            timestamp = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S')

            log_entry = {
                'IP Address': ip_address,
                'Timestamp': timestamp,
                'Request Method': request_method,
                'URL': url,
                'Response Code': response_code,
                'User Agent': user_agent,
                'Request Successful': request_successful,
                'Request Failed': request_failed
            }
            parsed_log_entries.append(log_entry)

# Create a DataFrame from the list of parsed log entries
df = pd.DataFrame(parsed_log_entries)

# Define the output directory
output_directory = './output/'

# Ensure the output directory exists, create it if necessary
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the output CSV file path
output_csv_path = os.path.join(output_directory, 'parsed_serverlogs.csv')

# Write the DataFrame to the CSV file
df.to_csv(output_csv_path, index=False)

# Print the DataFrame
print(df)
