import os
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

diretorio = 'Cartao'

mapeamento_colunas = {
    "Data": "date",
    "Lançamento": "title",
    "Categoria": "category",
    "Tipo": "type",
    "Valor": "amount"
}

def converter_valor_monetario(valor):
    if isinstance(valor, str): 
        try:
            # Remove caracteres indesejados
            valor = valor.replace('R$', '').replace('Â', '').strip()
            valor = locale.atof(valor)  # Converter para tipo numérico
            return valor
        except ValueError:
            return None
    else:
        return valor

dataframes = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.csv'):

        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_csv(caminho_arquivo)

        df = df.rename(columns=mapeamento_colunas)

        if 'amount' in df.columns:
            df['amount'] = df['amount'].apply(converter_valor_monetario)
            # Substituir pontos por vírgulas na coluna "Valor"
            df['amount'] = df['amount'].apply(lambda x: str(x).replace('.', ','))
            
        dataframes.append(df)

df_final = pd.concat(dataframes, ignore_index=True)

df_final = df_final[["date", "title", "category", "type", "amount"]]

df_final.columns = ["Data", "Lançamento", "Categoria", "Tipo", "Valor"]

df_final.to_csv('Dados.csv', index=False)

print("Arquivo CSV criado com sucesso!")
