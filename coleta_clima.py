import requests
import pandas as pd
from datetime import datetime
import os

# Localização (ex: São Paulo)
latitude = -23.55
longitude = -46.63

# API Open-Meteo
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode&timezone=America%2FSao_Paulo"

resposta = requests.get(url)
dados = resposta.json()

registro = {
    "data_hora": datetime.now().isoformat(),
    "temperatura": dados["current"]["temperature_2m"],
    "codigo_clima": dados["current"]["weathercode"]
}

df = pd.DataFrame([registro])

# Criar pasta e salvar CSV
os.makedirs("dados", exist_ok=True)
arquivo = f"dados/clima_{datetime.now().date().isoformat()}.csv"
df.to_csv(arquivo, index=False)

print(f"✔️ Arquivo salvo: {arquivo}")
