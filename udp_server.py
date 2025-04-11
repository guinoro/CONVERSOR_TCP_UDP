
import socket
import random

HOST = 'localhost'
PORT = 5002

def get_conversion_rate(moeda):
    rates = {
        'dolar': round(random.uniform(4.5, 5.5), 2),
        'euro': round(random.uniform(5.0, 6.0), 2),
        'libra': round(random.uniform(6.0, 7.0), 2)
    }
    return rates.get(moeda.lower(), None)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Servidor escutando em {HOST}:{PORT}...")
    
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Conectado por {addr}")
        mensagem = data.decode()
        try:
            valor_str, moeda = mensagem.strip().split()
            valor = float(valor_str)
            taxa = get_conversion_rate(moeda)
            if taxa:
                convertido = round(valor / taxa, 2)
                resposta = f"{valor} BRL = {convertido} {moeda.upper()} (cotação: {taxa})"
            else:
                resposta = "Moeda não suportada. Use: dolar, euro ou libra."
        except Exception:
            resposta = "Erro no formato da mensagem. Use: <valor> <moeda>"

        s.sendto(resposta.encode(), addr)
