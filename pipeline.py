from scripts.fetch_uniswap_data import fetch_data
import json

def main():
    print("Fetching Uniswap V3 pool data...")
    result = fetch_data()
    
    if result:
        print(json.dumps(result, indent=2))  # Pretty-print the JSON
    else:
        print("No data fetched!")

if __name__ == "__main__":
    main()
