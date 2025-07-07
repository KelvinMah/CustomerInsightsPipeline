
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

SHOP_NAME = os.getenv("SHOP_NAME")
ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")

def extract_shopify_data():
    headers = {
        "X-Shopify-Access-Token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    url = f"https://{SHOP_NAME}.myshopify.com/admin/api/2023-10/orders.json?status=any"

    response = requests.get(url, headers=headers)
    orders = response.json().get("orders", [])

    df = pd.json_normalize(orders)
    df.to_csv("/tmp/shopify_data.csv", index=False)
    print("Shopify data extracted.")
