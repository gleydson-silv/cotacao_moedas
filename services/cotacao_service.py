import requests
from datetime import datetime
from config.db_config import conectar

def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-BRL,EUR-BRL"
    resposta = requests.get(url)
    return resposta.json()

def salvar_cotacoes(dados):
    con = conectar()
    cursor = con.cursor()

    for moeda in dados.values():
        codigo = f"{moeda['code']}-{moeda['codein']}"
        valor = float(moeda['bid'])
        data_hora = datetime.now()

        cursor.execute("""
            INSERT INTO cotacoes (moeda, valor, data_hora)
            VALUES (%s, %s, %s)
        """, (codigo, valor, data_hora))

    con.commit()
    cursor.close()
    con.close()
