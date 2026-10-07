from sqlalchemy import text

from db import get_engine


engine = get_engine()

with engine.connect() as connection:
    database = connection.execute(
        text("SELECT current_database();")
    ).scalar()

    version = connection.execute(
        text("SELECT version();")
    ).scalar()

print("Połączenie działa!")
print(f"Baza: {database}")
print(f"Wersja: {version}")