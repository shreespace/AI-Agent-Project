import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/clustered_users.csv")

sns.barplot(x="wallet_address", y="trading_volume", data=df)
plt.xticks(rotation=90)
plt.title("Trading Volume of Raydium Users")
plt.show()
