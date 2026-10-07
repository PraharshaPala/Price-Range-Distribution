import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset .csv", encoding="latin1")

# Count restaurants in each price range
price_range_counts = df['Price range'].value_counts().sort_index()

# Calculate percentages
price_range_percentages = (
    df['Price range'].value_counts(normalize=True).sort_index() * 100
)

print("Percentage of restaurants in each price range:")
print(price_range_percentages.round(2))

# Create bar chart
plt.figure(figsize=(8, 5))
price_range_counts.plot(kind='bar')

plt.title('Distribution of Restaurants by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()