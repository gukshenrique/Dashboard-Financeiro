import psycopg2
import csv
import re
import pandas as pd
import tkinter as tk
from tkinter import simpledialog

def criar_tabela(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dados (
        Competencia DATE, 
        Data DATE,
        Lancamento VARCHAR(255),
        Categoria VARCHAR(255),
        Tipo VARCHAR(50),
        Valor NUMERIC,
        TipoConta VARCHAR(50)
    )
    """)

def dados_existem(cursor, data, lancamento, categoria, tipo, valor):
    cursor.execute("""
        SELECT COUNT(*) FROM Dados
        WHERE Data = %s AND Lancamento = %s AND Categoria = %s AND Tipo = %s AND Valor = %s
    """, (data, lancamento, categoria, tipo, valor))
    return cursor.fetchone()[0] > 0

def inserir_dados(cursor, csv_file_path, competencia, tipo_conta):
    dados_duplicados = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            valor_str = row['Valor']
            if valor_str.strip() and valor_str.strip() != 'nan':
                valor = re.sub(r'[^\d,-]', '', valor_str).replace(',', '.')
            else:
                valor = None 

            data_str = row['Data']
            try:
                data = pd.to_datetime(data_str, format='%d/%m/%Y').date()
            except ValueError:
                data = None
            
            if data is None:
                try:
                    data = pd.to_datetime(data_str).date()
                except ValueError:
                    pass
            
            if not dados_existem(cursor, data, row['Lançamento'], row['Categoria'], row['Tipo'], valor):
                cursor.execute(
                    "INSERT INTO Dados (Competencia, Data, Lancamento, Categoria, Tipo, Valor, TipoConta) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (competencia, data, row['Lançamento'], row['Categoria'], row['Tipo'], valor, tipo_conta)
                )
            else:
                dados_duplicados.append((data, row['Lançamento'], row['Categoria'], row['Tipo'], valor))

    if dados_duplicados:
        print("As seguintes informações duplicadas foram encontradas e não foram inseridas:")
        for dados in dados_duplicados:
            print("Data:", dados[0], "Lançamento:", dados[1], "Categoria:", dados[2], "Tipo:", dados[3], "Valor:", dados[4])

def obter_competencia():
    root = tk.Tk()
    root.withdraw()
    competencia = simpledialog.askstring("Competência dos Dados", "Qual a competência dos dados?")
    return competencia

def obter_tipo_conta():
    root = tk.Tk()
    root.withdraw()
    tipo_conta = simpledialog.askstring("Tipo de Conta", "Os dados são de conta corrente ou cartão de crédito?")
    return tipo_conta

conn = psycopg2.connect(
    dbname="Dados",
    user="Gustavo",
    password="20ju22li",
    host="localhost"
)

cur = conn.cursor()

criar_tabela(cur)

csv_file_path = 'Dados.csv'

competencia = obter_competencia()
tipo_conta = obter_tipo_conta()

inserir_dados(cur, csv_file_path, competencia, tipo_conta)

conn.commit()

cur.close()
conn.close()