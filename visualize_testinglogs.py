import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data as a DataFrame
data = pd.read_csv('output/parsed_testinglogs.csv')

# Convert the 'UTC Timestamp' column to datetime
data['UTC Timestamp'] = pd.to_datetime(data['UTC Timestamp'])

# Create a line plot to visualize the 'Data Payload (Decimal)' column over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='UTC Timestamp', y='Data Payload (Decimal)', hue='Message ID (Decimal)')
plt.title('Data Payload (Decimal) over Time')
plt.xlabel('Timestamp')
plt.ylabel('Data Payload (Decimal)')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the line plot
plt.show()
