import requests
from dotenv import load_dotenv
import os
import asyncio

class MoralisClient:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.headers = {
            'accept': 'application/json','X-API-Key': os.getenv("MORALIS_API_key"),
        }
    
    def handle_request(self, url):
        return requests.get(
            url,
            headers=self.headers
        )

    async def handle_response(self, response):
        try:
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else", err)

    async def searchNFTs(self, q, filter, chain="Eth", format="decimal", limit=100):
        url = f'https://deep-index.moralis.io/api/v2/nft/search?chain={chain}&format={format}&q={q}&filter={filter}&limit={limit}'
        response = self.handle_request(url)
        return await self.handle_response(response)

    async def getNFTs(self, address, chain="Eth", format="decimal"):
        url = f'https://deep-index.moralis.io/api/v2/{address}/nft?chain={chain}&format={format}'
        response = self.handle_request(url)
        return await self.handle_response(response)

    async def getNFTsForContract(self, address, token_address="", chain="Eth", format="decimal", cursor="", limit=100):
        url = f'https://deep-index.moralis.io/api/v2/{address}/nft/{token_address}chain={chain}&format={format}'
        response = self.handle_request(url)
        return await self.handle_response(response)

    async def getNFTTransfers(self, address, chain="Eth", direction="both", format="decimal", cursor="", limit=100):
        url = f'https://deep-index.moralis.io/api/v2/{address}/nft/transfers?chain={chain}&format={format}'
        response = self.handle_request(url)
        return await self.handle_response(response)
