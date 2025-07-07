
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../scripts')

from extract_shopify import extract_shopify_data
from extract_google_ads import extract_google_ads_data
from transform_data import transform_data
from load_to_postgres import load_to_postgres

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'customer_insights_etl',
    default_args=default_args,
    description='ETL pipeline for customer insights',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 7, 1),
    catchup=False,
)

task_extract_shopify = PythonOperator(
    task_id='extract_shopify',
    python_callable=extract_shopify_data,
    dag=dag,
)

task_extract_google_ads = PythonOperator(
    task_id='extract_google_ads',
    python_callable=extract_google_ads_data,
    dag=dag,
)

task_transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

task_load = PythonOperator(
    task_id='load_to_postgres',
    python_callable=load_to_postgres,
    dag=dag,
)

[task_extract_shopify, task_extract_google_ads] >> task_transform >> task_load
