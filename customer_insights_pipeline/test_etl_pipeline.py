
import unittest
import pandas as pd
import os

from scripts.extract_shopify import extract_shopify_data
from scripts.extract_google_ads import extract_google_ads_data
from scripts.transform_data import transform_data

class TestETLPipeline(unittest.TestCase):
    def test_shopify(self):
        extract_shopify_data()
        df = pd.read_csv('/tmp/shopify_data.csv')
        self.assertIn('user_id', df.columns)

    def test_google_ads(self):
        extract_google_ads_data()
        df = pd.read_csv('/tmp/google_ads_data.csv')
        self.assertIn('ad_id', df.columns)

    def test_transform(self):
        transform_data()
        df = pd.read_csv('/tmp/transformed_data.csv')
        self.assertIn('user_id', df.columns)

if __name__ == '__main__':
    unittest.main()
