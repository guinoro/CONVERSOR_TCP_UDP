
import socket

HOST = 'localhost'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    valor = input("Digite o valor em R$ e a moeda (dolar, euro ou libra): ")
    s.send(valor.encode())
    resposta = s.recv(1024).decode()
    print("[TCP] Resposta do servidor:", resposta)
