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
