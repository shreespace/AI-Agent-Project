import os

print("Fetching Transactions...")
os.system("python scripts/fetch_transactions.py")

print("Initializing Database...")
os.system("python database/init_db.py")

print("Applying ML Model...")
os.system("python ml_models/clustering.py")

print("Generating Visualizations...")
os.system("python visualizations/plots.py")

print("✅ Pipeline Completed.")
