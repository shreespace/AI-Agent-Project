from src.birdeye import fetch_token_data

if __name__ == "__main__":
    token_address = "SOL"  # Replace with required token
    data = fetch_token_data(token_address)
    print("Token Data:", data)
