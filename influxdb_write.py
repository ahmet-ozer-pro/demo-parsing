from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import csv

# InfluxDB 2.0 connection information
url = "http://localhost:8086"  # Replace with your InfluxDB 2.0 URL
token = "hCyIm9XIU4Prm32DGravJA_aZLdxtjGej-9m1xPI9R7oLnRKssMZ7hNQRw7p-HFsODhRyiVP0Nkxq2HTG6ZHXw=="           # Replace with your authentication token
org = "aozer"               # Replace with your organization name
bucket = "aozer"         # Replace with your bucket name

# Create an InfluxDB 2.0 client
client = InfluxDBClient(url=url, token=token, org=org)

# Create a write API
write_api = client.write_api(write_options=SYNCHRONOUS)

# Read and write data from the CSV file
with open('./output/parsed_serverlogs.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        point = Point("your_measurement_name") \
            .tag("ip_address", row["IP Address"]) \
            .time(row["Timestamp"], WritePrecision.S) \
            .field("request_method", row["Request Method"]) \
            .field("url", row["URL"]) \
            .field("response_code", int(row["Response Code"])) \
            .field("user_agent", row["User Agent"]) \
            .field("request_successful", row["Request Successful"]) \
            .field("request_failed", int(row["Request Failed"]))
        write_api.write(bucket=bucket, record=point)

# Close the InfluxDB 2.0 client
client.close()
