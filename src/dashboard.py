# Importa o Streamlit para criar o dashboard web
import streamlit as st

# Importa o Pandas para manipulação de dados
import pandas as pd

# Importa o Plotly Express para gerar gráficos interativos
import plotly.express as px

# Importa o SQLAlchemy para conectar ao PostgreSQL
from sqlalchemy import create_engine

# Cria a conexão com o banco PostgreSQL usando o driver psycopg2
engine = create_engine("postgresql+psycopg2://postgres:senha123@localhost:5432/iotdb")

# Função auxiliar para carregar dados de qualquer view SQL
def load(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

# Título principal do dashboard
st.title("Dashboard IoT - Temperaturas")

# -----------------------------
# GRÁFICO 1: Média por dispositivo
# -----------------------------
st.header("Média por dispositivo")

# Carrega a view que calcula a média de temperatura por sensor
df1 = load("avg_temp_por_dispositivo")

# Exibe gráfico de barras com as médias
st.plotly_chart(px.bar(df1, x="device_id", y="avg_temp"))

# -----------------------------
# GRÁFICO 2: Leituras por hora
# -----------------------------
st.header("Leituras por hora")

# Carrega a view que conta quantas leituras existem por hora do dia
df2 = load("leituras_por_hora")

# Exibe gráfico de linha com a contagem por hora
st.plotly_chart(px.line(df2, x="hora", y="contagem"))

# -----------------------------
# GRÁFICO 3: Máximas e mínimas por dia
# -----------------------------
st.header("Máximas e mínimas por dia")

# Carrega a view que calcula temperatura máxima e mínima por dia
df3 = load("temp_max_min_por_dia")

# Exibe gráfico de linha com máximas e mínimas
st.plotly_chart(px.line(df3, x="data", y=["temp_max", "temp_min"]))

# -----------------------------
# GRÁFICO 4: Temperatura ao longo do tempo (último dia)
# -----------------------------
st.header("Temperatura ao longo do tempo")

# Consulta apenas o último dia de registros usando date_trunc
df_all = pd.read_sql("""
    SELECT * 
    FROM temperature_readings
    WHERE timestamp >= (
        SELECT date_trunc('day', MAX(timestamp)) 
        FROM temperature_readings
    )
    ORDER BY timestamp
""", engine)

# Cria gráfico de linha com escala fixa no eixo Y (estética)
fig = px.line(
    df_all,
    x="timestamp",
    y="temperature",
    color="device_id",
    range_y=[10, 40]  # escala visual fixa entre 10°C e 40°C
)

# Exibe o gráfico no dashboard
st.plotly_chart(fig)
