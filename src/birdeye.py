import requests
from src.config import BIRDEYE_API_KEY, BIRDEYE_BASE_URL

def fetch_token_data(token_address):
    url = f"{BIRDEYE_BASE_URL}/public/token/{token_address}/price"
    headers = {"X-API-KEY": BIRDEYE_API_KEY}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    token_address = "SOL"  # Example: Solana Token
    data = fetch_token_data(token_address)
    print(data)
