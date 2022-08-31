import requests
from dotenv import load_dotenv
import os

load_dotenv()
moralis_API_key = os.getenv("MORALIS_API_key")

def get_call(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else", err)

def moralis_headers():
    return {"accept": "application/json","X-API-Key": moralis_API_key}

def searchNFTs(q, filter, chain="Eth", format="decimal", limit=100):
    url = f'https://deep-index.moralis.io/api/v2/nft/search?chain={chain}&format={format}&q={q}&filter={filter}&limit={limit}'
    headers = moralis_headers()
    return get_call(url, headers)

def getNFTs(address, chain="Eth", format="decimal"):
    url = f'https://deep-index.moralis.io/api/v2/{address}/nft?chain={chain}&format={format}'
    headers = moralis_headers()
    return get_call(url, headers)

def getNFTsForContract(address, token_address="", chain="Eth", format="decimal", cursor="", limit=100):
    url = f'https://deep-index.moralis.io/api/v2/{address}/nft/{token_address}chain={chain}&format={format}'
    headers = moralis_headers()
    return get_call(url, headers)

def getNFTTransfers(address, chain="Eth", direction="both", format="decimal", cursor="", limit=100):
    url = f'https://deep-index.moralis.io/api/v2/{address}/nft/transfers?chain={chain}&format={format}'
    headers = moralis_headers()
    return get_call(url, headers)
