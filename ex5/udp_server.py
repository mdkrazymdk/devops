import socket


UDP_IP = "127.0.0.1"
UDP_PORT = 8125

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"📡 UDP сервер слухає на {UDP_IP}:{UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(1024) 
    print(f"📥 Отримано метрику: {data.decode('utf-8')}")
