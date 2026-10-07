import pandas as pd
from db import get_engine

engine = get_engine()

df = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

print(f"Ładowanie {len(df):,} rekordów...")

df.to_sql(
    name="orders",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=10_000,
)

print("Tabela orders została załadowana.")