#GetPrices_loop_save.py
# A cada 60s: coleta os dados e salva em CSV

import os
import time
import pandas as pd
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df   

Sleep_Seconds = 60
CSV_Path = 'cotacoes.csv'

if __name__ == '__main__':

  #Se o arquivo CSV não existir, cria com os cabeçalhos
  if not os.path.exists(CSV_Path):
    # Criar DataFrame vazio com os cabeçalhos e salvar em CSV
    cols = ['ativo', 'preco', 'moeda', 'horario_de_coleta']
    pd.DataFrame(columns=cols).to_csv(CSV_Path, index=False)

  while True:
    #Coleta os dados
    df_btc = get_bitcoin_df()
    df_comm = get_commodities_df()

    #Concatena os dados
    df = pd.concat([df_btc, df_comm], ignore_index=True)

    #Salva os dados no CSV (append) sem os cabeçalhos
    df.to_csv(CSV_Path, mode='a', header=False, index=False)

    #Espera o tempo definido antes de coletar os dados novamente
    time.sleep(Sleep_Seconds) 