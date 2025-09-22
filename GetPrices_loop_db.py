import time
import pandas as pd
from sqlalchemy import create_engine
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df 

from dotenv import load_dotenv
import os

#Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

#Configurações do banco de dados (Substituir com dados reais)
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
URL = os.getenv('URL')  

#Criar conexão com o banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)  

Sleep_Seconds = 3600 #1hora

if __name__ == '__main__':
  while True:
    #Coleta os dados
    df_btc = get_bitcoin_df(URL)
    df_comm = get_commodities_df()

    #Junta os dados
    df = pd.concat([df_btc, df_comm], ignore_index=True)

    #Salva os dados no banco (append) sem os cabeçalhos
    df.to_sql('cotacoes', engine, if_exists='append', index=False)

    print('Dados inseridos no banco com sucesso!')

    #Espera o tempo definido antes de coletar os dados novamente
    time.sleep(Sleep_Seconds)

