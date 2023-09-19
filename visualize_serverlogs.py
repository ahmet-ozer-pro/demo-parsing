import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('output/parsed_serverlogs.csv')

# Create a count plot of Request Methods
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Request Method")
plt.title("Request Methods Count")
plt.xticks(rotation=45)
plt.xlabel("Request Method")
plt.ylabel("Count")
plt.show()




# Convert the "Timestamp" column to a datetime data type
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set the "Timestamp" column as the index of the DataFrame
df.set_index('Timestamp', inplace=True)

# Resample the data to a frequency of seconds and count the number of requests per second
requests_per_second = df.resample('S').size()

# Plot the time series data
plt.figure(figsize=(12, 6))
requests_per_second.plot()
plt.title("Requests Per Second Over Time")
plt.xlabel("Time")
plt.ylabel("Requests Count")
plt.grid(True)
plt.show()
