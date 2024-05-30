import os
import requests

from dotenv import load_dotenv


load_dotenv()

account_id = os.getenv("IBKR_USER_ID")

url = f"https://api.ibkr.com/api/v1/iserver/account/{account_id}/summary/balances"

response = requests.get(url)
print(response.content)
