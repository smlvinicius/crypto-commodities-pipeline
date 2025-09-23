Crypto & Commodities Pipeline

Este projeto coleta preços de Bitcoin e Commodities e salva em um banco de dados PostgreSQL (SupaBase).

 🚀 Estrutura do projeto
- `GetBitcoin.py` → coleta dados do Bitcoin  
- `GetCommodities.py` → coleta dados de commodities  
- `GetPrices_loop_db.py` → integra e salva no banco  

 🛠️ Como rodar

1. Clone o repositório

   git clone https://github.com/smlvinicius/crypto-commodities-pipeline.git

   cd crypto-commodities-pipeline

3. Crie um ambiente virtual:
 
   - python -m venv .venv
   - source .venv/bin/activate   
   - .venv\Scripts\activate      

4. Instale as Dependências:
  
    pip install -r requiriments.txt

5. Configure suas variaveis no arquivo .env
   Preencha os valores reais no arquivo .env.
   Exemplo:
   
   - DB_USER=meu_usuario
   - DB_PASSWORD=minha_senha
   - DB_HOST=localhost
   - DB_PORT=5432
   - DB_NAME=meu_banco
 

6. Execute o script principal:
    
    python GetPrices_loop_db.py

📦 Requisitos:

   - Python 3.10+
   - Conta no Supabase "https://supabase.com/"
