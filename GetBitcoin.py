import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df(url):
    # URL Obter o preço atual do Bitcoin em USD

    # Fazer a requisição GET
    response = requests.get(url)
    data = response.json()

    # Extrair o preço do Bitcoin
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_de_coleta = datetime.now()

    # Criar um DataFrame com os dados coletados
    df = pd.DataFrame({
        'preco': [preco],
        'ativo': [ativo],
        'moeda': [moeda],
        'horario_de_coleta': [horario_de_coleta]    
    })
    
    return df

