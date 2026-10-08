import pandas as pd
from sqlalchemy import create_engine

# Conexão com PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:senha123@localhost:5432/iotdb")


# Carregar CSV
df = pd.read_csv("data/temperature.csv")

# Inserir no banco
df.to_sql("temperature_readings", engine, if_exists="append", index=False)

print("Dados inseridos com sucesso!")
