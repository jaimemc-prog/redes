import socket

def main():
    host = "192.168.127.207"
    port = 12000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        print("\nMENU\n1. Hora del servidor\n2. Cuenta las S en una palabra\n3. Directorio \n4. Salir\n")
        option = input("Ingresa tu opcion (1/2/3/4): ")
        sock.send(option.encode())
        if option == '1':
            current_time = sock.recv(1024).decode()
            print(f"Hora actual en servidor: {current_time}")
        elif option == '2':
            sentence = input("Ingresa la palabra: ")
            sock.send(sentence.encode())
            count_s = sock.recv(1024).decode()
            print(f"Numero de 's' en la palabra: {count_s}")
        elif option == '3':
            current_dir = sock.recv(1024).decode()
            print(f"Directorio actual: {current_dir}")
        elif option == '4':
            break
        else:
            print("Ingresa una opcion valida")
    sock.close()

if __name__ == '__main__':
    main()

