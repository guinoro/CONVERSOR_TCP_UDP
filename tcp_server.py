
import socket
import random

HOST = 'localhost'
PORT = 5001

def get_conversion_rate(moeda):
    rates = {
        'dolar': round(random.uniform(4.5, 5.5), 2),
        'euro': round(random.uniform(5.0, 6.0), 2),
        'libra': round(random.uniform(6.0, 7.0), 2)
    }
    return rates.get(moeda.lower(), None)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor escutando em {HOST}:{PORT}...")
    
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Conectado por {addr}")
            data = conn.recv(1024).decode()
            if not data:
                break
            try:
                valor_str, moeda = data.strip().split()
                valor = float(valor_str)
                taxa = get_conversion_rate(moeda)
                if taxa:
                    convertido = round(valor / taxa, 2)
                    resposta = f"{valor} BRL = {convertido} {moeda.upper()} (cotação: {taxa})"
                else:
                    resposta = "Moeda não suportada. Use: dolar, euro ou libra."
            except Exception as e:
                resposta = f"Erro no formato da mensagem. Use: <valor> <moeda>"

            conn.send(resposta.encode())
