============================================================
README - Pipeline de Dados IoT com Docker, PostgreSQL e Streamlit
============================================================

SOBRE O PROJETO

Este projeto implementa um pipeline completo de dados IoT, capaz de:

Simular leituras de temperatura de sensores IoT

Processar e armazenar os dados em um banco PostgreSQL dentro de um container Docker

Criar views SQL para análise

Exibir gráficos interativos em um dashboard Streamlit

O objetivo é demonstrar uma arquitetura moderna de ingestão, armazenamento e visualização de dados IoT.

ARQUITETURA DO PIPELINE

Fluxo geral:

Gerador de dados -> CSV -> Pipeline Python -> PostgreSQL -> Views SQL -> Dashboard Streamlit

Tecnologias utilizadas:

Python

Docker

PostgreSQL

SQLAlchemy

Streamlit

Plotly

ESTRUTURA DO PROJETO
``` 
iot-pipeline/
    data/
        temperature.csv
    src/
        generate_data.py
        pipeline.py
        dashboard.py
    docs/
        trabalho.pdf (opcional)
    README.md
``` 
CONFIGURAÇÃO DO DOCKER + POSTGRESQL

Criar container:

``` 
docker run --name postgres-iot -e POSTGRES_PASSWORD=senha123 -p 5432:5432 -d postgres
``` 
Acessar o banco:

``` 
docker exec -it postgres-iot psql -U postgres
``` 
Criar banco e tabela:

```  
CREATE DATABASE iotdb;
 
\c iotdb;

CREATE TABLE temperature_readings (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50),
    temperature FLOAT,
    timestamp TIMESTAMP
);

``` 
GERADOR DE DADOS IOT (7 DIAS)

Arquivo: src/generate_data.py

``` 
python src/generate_data.py
``` 
PIPELINE DE INSERÇÃO NO POSTGRESQL

Arquivo: src/pipeline.py

Executar:

```  
python src/pipeline.py

``` 
Mensagem esperada:
``` 
Dados inseridos com sucesso!
VIEWS SQL CRIADAS
``` 

Média por dispositivo:



``` 
CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;
Leituras por hora:
``` 
``` 
CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora,
       COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;
``` 

Máximas e mínimas por dia:


``` 
CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) AS data,
       MAX(temperature) AS temp_max,
       MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY data;

``` 
DASHBOARD STREAMLIT

Arquivo: src/dashboard.py

Executar:

``` 
streamlit run src/dashboard.py
``` 
Graficos exibidos:

Média por dispositivo

Leituras por hora

Máximas e mínimas por dia

Temperatura ao longo do último dia

CAPTURAS DE TELA

Inclua no GitHub:

Gráficos do dashboard

Pipeline funcionando

Banco populado

Views SQL

INSIGHTS OBTIDOS

Sensores apresentam comportamento estável entre 15 C e 35 C

Picos de leitura ocorrem em horários específicos

Máximas e mínimas variam por dia devido à simulação realista

Pipeline suporta expansão para mais sensores e mais dias

COMO EXECUTAR O PROJETO

Clone o repositório

Crie o ambiente virtual

Instale dependências:

``` 
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
``` 
Suba o Docker PostgreSQL

Gere os dados

Execute o pipeline

Rode o dashboard

COMANDOS GIT UTILIZADOS

``` 
git init
git add .
git commit -m "Pipeline IoT completo"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/iot-pipeline.git
git push -u origin main
``` 


============================================================
FIM DO README 
============================================================