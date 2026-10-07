import pandas as pd

from db import get_engine

engine = get_engine()

tables = {
    "customers": "data/raw/olist_customers_dataset.csv",
    "geolocation": "data/raw/olist_geolocation_dataset.csv",
    "order_items": "data/raw/olist_order_items_dataset.csv",
    "order_payments": "data/raw/olist_order_payments_dataset.csv",
    "order_reviews": "data/raw/olist_order_reviews_dataset.csv",
    "orders": "data/raw/olist_orders_dataset.csv",
    "products": "data/raw/olist_products_dataset.csv",
    "sellers": "data/raw/olist_sellers_dataset.csv",
    "category_translation": "data/raw/product_category_name_translation.csv",
}

date_columns = {
    "orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ],
    "order_items": [
        "shipping_limit_date",
    ],
    "order_reviews": [
        "review_creation_date",
        "review_answer_timestamp",
    ],
}

for table_name, file_path in tables.items():
    print(f"Loading {table_name}")
    df = pd.read_csv(file_path)

    if table_name in date_columns:
        for column in date_columns[table_name]:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    df.to_sql(table_name,
              con=engine,
              if_exists="replace",
              index=False,
              chunksize=10_000,
    )

    print(
        f"{table_name}: "
        f"{len(df)} rows loaded."
    )

print("\nAll tables loaded.")