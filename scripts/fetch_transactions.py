from solana.rpc.api import Client
import pandas as pd

# Connect to Solana RPC
solana_client = Client("https://api.mainnet-beta.solana.com")

RAYDIUM_SWAP_PROGRAM_ID = "5quB4MoyZPT3cEpxS5TQK8K3fN8g5GM8tQZ5zv7ZP7w"

def fetch_raydium_transactions():
    signatures = solana_client.get_signatures_for_address(RAYDIUM_SWAP_PROGRAM_ID, limit=20)
    transactions = []
    
    for tx in signatures['result']:
        tx_details = solana_client.get_transaction(tx['signature'])
        if tx_details['result']:
            tx_data = {
                "signature": tx['signature'],
                "block_time": tx_details["result"]["blockTime"],
                "fee": tx_details["result"]["meta"]["fee"]
            }
            transactions.append(tx_data)

    return transactions

df = pd.DataFrame(fetch_raydium_transactions())
df.to_csv("../data/raydium_transactions.csv", index=False)
print("Fetched transactions saved to CSV.")
