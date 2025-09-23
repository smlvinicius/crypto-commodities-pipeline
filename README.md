# Crypto & Commodities Pipeline

Este projeto coleta preços de **Bitcoin** e **commodities** e salva em um banco de dados PostgreSQL. (SupaBase)

## 🚀 Estrutura do projeto
- `GetBitcoin.py` → coleta dados do Bitcoin  
- `GetCommodities.py` → coleta dados de commodities  
- `GetPrices_loop_db.py` → integra e salva no banco  

## 🛠️ Como rodar

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows

2. Instale as Dependências:
  
    pip install -r requiriments.txt

3. Configure suas variaveis no arquivo .env

4. Execute o script principal:
    
    python GetPrices_loop_db.py

📦 Requisitos

    Python 3.10+
    Conta no Supabase "https://supabase.com/"

5. Salve (`CTRL+S` ou `CMD+S`).

### 🔹 Depois de criar, rode no terminal:
```bash
git add README.md
git commit -m "Adiciona README inicial"
git push