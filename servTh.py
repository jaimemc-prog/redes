import socket
import threading
import os
from datetime import datetime

print_lock = threading.Lock()

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print_lock.release()
            break
        option = data.decode()
        if option == '1':
            current_time = datetime.now()
            current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            conn.send(current_time.encode())
        elif option == '2':
            sentence = conn.recv(1024).decode()
            count_s = sentence.count('S') + sentence.count('s')
            conn.send(str(count_s).encode())
        elif option == '3':
            current_dir = os.path.abspath(os.path.dirname(__file__))
            conn.send(current_dir.encode())
        else:
            conn.send("Ingrese una opcion valida.".encode())
    conn.close()

def main():
    host = "192.168.127.207"
    port = 12000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Escuchando en {host}:{port}")
    while True:
        conn, addr = sock.accept()
        print(f"se conecto a {addr[0]}:{addr[1]}")
        print_lock.acquire()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    main()
