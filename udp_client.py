
import socket

HOST = 'localhost'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    valor = input("Digite o valor em R$ e a moeda (dolar, euro ou libra): ")
    s.sendto(valor.encode(), (HOST, PORT))
    resposta, _ = s.recvfrom(1024)
    print("[UDP] Resposta do servidor:", resposta.decode())
