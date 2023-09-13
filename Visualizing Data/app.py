import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

# Sample data: Replace this with your actual data
data = [
    {'date': '2023-09-01', 'count': 5},
    {'date': '2023-09-02', 'count': 7},
    {'date': '2023-09-03', 'count': 10},
    # Add more data points as needed
]

# Convert date strings to datetime objects
for entry in data:
    entry['date'] = datetime.strptime(entry['date'], '%Y-%m-%d')

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Sort DataFrame by date
df = df.sort_values(by='date')

# Create a line chart to visualize the trend
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['count'], marker='o', linestyle='-')
plt.title('Positive News Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Positive News Count')
plt.grid(True)

# Format date labels on the x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
