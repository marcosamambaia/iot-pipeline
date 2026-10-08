import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------------------------------------------
# GERADOR DE DADOS IoT — SIMULA 7 DIAS DE LEITURAS DE TEMPERATURA
# -------------------------------------------------------------
# Este script cria um CSV contendo leituras de temperatura de 3 sensores IoT.
# Cada dia possui 144 leituras (intervalos de 10 minutos).
# As temperaturas variam dentro de uma faixa diferente por dia,
# permitindo que a view de máximas e mínimas mostre variações reais.
# -------------------------------------------------------------

# Lista que armazenará todas as linhas (leituras simuladas)
rows = []

# Data e hora inicial da simulação (primeiro dia)
start = datetime(2024, 1, 1, 0, 0, 0)

# -------------------------------------------------------------
# Loop principal: gera dados para 7 dias consecutivos
# -------------------------------------------------------------
for d in range(7):
    # Calcula o início do dia atual (dia 0 = 01/01, dia 1 = 02/01, etc.)
    day_start = start + timedelta(days=d)

    # Para cada dia, definimos uma faixa de temperatura diferente.
    # Isso garante que a view temp_max_min_por_dia tenha valores variados.
    base_min = random.uniform(15, 22)   # temperatura mínima do dia
    base_max = random.uniform(28, 35)   # temperatura máxima do dia

    # -------------------------------------------------------------
    # Loop de 144 intervalos de 10 minutos (24 horas)
    # -------------------------------------------------------------
    for i in range(144):
        # Timestamp exato da leitura (incremento de 10 minutos)
        timestamp = day_start + timedelta(minutes=i * 10)

        # -------------------------------------------------------------
        # Três sensores IoT simulados
        # -------------------------------------------------------------
        for sensor in ["sensor-01", "sensor-02", "sensor-03"]:
            # Gera uma temperatura aleatória dentro da faixa do dia
            temperature = round(random.uniform(base_min, base_max), 2)

            # Adiciona a leitura à lista de dados
            rows.append([sensor, temperature, timestamp])

# -------------------------------------------------------------
# Criação do DataFrame com as colunas esperadas pelo pipeline
# -------------------------------------------------------------
df = pd.DataFrame(rows, columns=["device_id", "temperature", "timestamp"])

# -------------------------------------------------------------
# Exporta o CSV para a pasta /data
# -------------------------------------------------------------
df.to_csv("data/temperature.csv", index=False)

print("CSV gerado com sucesso: 7 dias de leituras simuladas (10 min de intervalo).")
