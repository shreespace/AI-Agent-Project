import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raydium_transactions.csv")

X = df[["swap_amount", "liquidity_provided", "trading_volume"]].dropna()
kmeans = KMeans(n_clusters=3, random_state=42)
df["user_group"] = kmeans.fit_predict(X)

df.to_csv("../data/clustered_users.csv", index=False)

plt.scatter(X["swap_amount"], X["trading_volume"], c=df["user_group"], cmap="viridis", alpha=0.5)
plt.xlabel("Swap Amount")
plt.ylabel("Trading Volume")
plt.title("Raydium User Clusters")
plt.show()
