
from google.ads.googleads.client import GoogleAdsClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def extract_google_ads_data():
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    ga_service = client.get_service("GoogleAdsService")

    query = '''
        SELECT
            campaign.id,
            ad_group.id,
            ad_group_criterion.criterion_id,
            segments.date,
            metrics.clicks,
            metrics.impressions
        FROM ad_group_criterion
        WHERE segments.date DURING LAST_7_DAYS
    '''

    response = ga_service.search_stream(customer_id=os.getenv("GOOGLE_ADS_CUSTOMER_ID"), query=query)

    rows = []
    for batch in response:
        for row in batch.results:
            rows.append({
                "campaign_id": row.campaign.id,
                "ad_group_id": row.ad_group.id,
                "criterion_id": row.ad_group_criterion.criterion_id,
                "date": row.segments.date.value,
                "clicks": row.metrics.clicks,
                "impressions": row.metrics.impressions
            })

    pd.DataFrame(rows).to_csv("/tmp/google_ads_data.csv", index=False)
    print("Google Ads data extracted.")
