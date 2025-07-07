
import pandas as pd

def transform_data():
    shopify_df = pd.read_csv('/tmp/shopify_data.csv')
    ads_df = pd.read_csv('/tmp/google_ads_data.csv')

    # Data validation
    assert not shopify_df['user_id'].isnull().any(), "Null user_id in Shopify data"
    assert not ads_df['user_id'].isnull().any(), "Null user_id in Google Ads data"
    assert shopify_df.shape[0] > 0, "Shopify data is empty"
    assert ads_df.shape[0] > 0, "Google Ads data is empty"

    merged_df = pd.merge(shopify_df, ads_df, on='user_id', how='outer')
    merged_df.to_csv('/tmp/transformed_data.csv', index=False)
    print("Data transformed with validation.")
