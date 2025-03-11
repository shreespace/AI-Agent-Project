import requests
import json

# The Graph API endpoint for Uniswap v3
GRAPH_API_URL = "https://gateway.thegraph.com/api/6a895ba6bb78d81c95c626c20ee6e9bc/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"

# GraphQL query
query = """
{
  pools(
    where: {
      token0: "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
      token1: "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    }
    orderBy: liquidity
    orderDirection: desc
  ) {
    id
    token0Price
    token1Price
    liquidity
  }
}
"""

def fetch_data():
    response = requests.post(GRAPH_API_URL, json={"query": query})
    
    if response.status_code == 200:
        data = response.json()
        
        # Save JSON to a file
        with open("uniswap_data.json", "w") as json_file:
            json.dump(data, json_file, indent=2)

        print("Data saved to uniswap_data.json")
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    result = fetch_data()
    if result:
        print(json.dumps(result, indent=2))  # Pretty-print the JSON
