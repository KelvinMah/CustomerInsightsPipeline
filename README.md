
# Customer Insights Data Pipeline

Complete end-to-end ETL pipeline integrating Shopify and Google Ads using Airflow, PostgreSQL, and Power BI.

## Stack
- Python, Pandas, Requests, Dotenv
- Airflow DAGs
- PostgreSQL
- Power BI Dashboard
- AWS Terraform Infra (EC2 + RDS)

## Run
1. `pip install -r requirements.txt`
2. Set up `.env` from `.env.example`
3. Run unit tests: `python test_etl_pipeline.py`

## Deployment
Use Terraform in `/terraform` to provision EC2 + RDS on AWS.
