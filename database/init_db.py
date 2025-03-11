import psycopg2

conn = psycopg2.connect(database="raydium_db", user="your_user", password="your_password", host="localhost", port="5432")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS raydium_transactions (
    wallet_address TEXT,
    transaction_signature TEXT PRIMARY KEY,
    timestamp TIMESTAMP,
    swap_amount FLOAT,
    liquidity_provided FLOAT,
    trading_volume FLOAT,
    token_in TEXT,
    token_out TEXT,
    fee FLOAT
);
""")

conn.commit()
cursor.close()
conn.close()
print("Database initialized.")
