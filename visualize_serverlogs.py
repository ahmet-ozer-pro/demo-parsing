import pandas as pd
import matplotlib.pyplot as plt

server_df = pd.read_csv('output/parsed_serverlogs.csv')

# Visualize the response codes
plt.figure(figsize=(10, 6))
plt.bar(server_df['IP Address'], server_df['Response Code'], color='skyblue')
plt.xlabel('IP Address')
plt.ylabel('Response Code')
plt.title('Response Codes by IP Address')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
