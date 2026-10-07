import pandas as pd

df = pd.read_csv("data/raw/olist_orders_dataset.csv")

print("Pierwsze 5 wierszy:")
print(df.head())

print("\nRozmiar danych:")
print(df.shape)

print("\nKolumny:")
print(df.columns.tolist())

print("\nInformacje o danych:")
df.info()

print("\nLiczba brakujących wartości:")
print(df.isnull().sum())

print("\nLiczba duplikatów:")
print(df.duplicated().sum())

print("\nStatusy samówień:")
print(df["order_status"].value_counts())

print("\nZakres dat:")
print(df["order_purchase_timestamp"].min())
print(df["order_purchase_timestamp"].max())

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

print("\nTypy danych po konwersji:")
print(df.dtypes)

print("\nLiczba rekordów:")
print(len(df))

print("\nUnikalne order_id:")
print(df["order_id"].nunique())

missing_delivery = (
    df[df["order_delivered_customer_date"].isna()]
    ["order_status"]
    .value_counts()
)

print("\nStatusy zamówień bez dostawy:")
print(missing_delivery)

delivered_without_date = df[
    (df["order_status"] == "delivered")
    &
    (df["order_delivered_customer_date"].isna())
]

print("\nDelivered bez daty dostawy:")
print(len(delivered_without_date))

non_delivered_with_date = df[
    (df["order_status"] != "delivered")
    &
    (df["order_delivered_customer_date"].notna())
]

print("\nNiedelivered z datą dostawy:")
print(len(non_delivered_with_date))

print("\nStatusy:")
print(
    non_delivered_with_date[
        "order_status"
    ].value_counts()
)