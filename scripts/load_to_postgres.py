
import pandas as pd
import psycopg2

def load_to_postgres():
    df = pd.read_csv('/tmp/transformed_data.csv')
    conn = psycopg2.connect(
        host='localhost',
        database='customer_insights',
        user='postgres',
        password='postgres'
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS insights (
            timestamp TIMESTAMP,
            user_id INT,
            event_type TEXT,
            product_id INT,
            ad_id INT,
            click INT
        )
    """)
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO insights (timestamp, user_id, event_type, product_id, ad_id, click)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row.get('timestamp'), row.get('user_id'), row.get('event_type'),
               row.get('product_id'), row.get('ad_id'), row.get('click')))
    conn.commit()
    cur.close()
    conn.close()
    print("Loaded into PostgreSQL.")
