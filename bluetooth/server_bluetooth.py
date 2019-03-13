import bluetooth


def main():
    server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 3
    server_sock.bind(("",port))

    server_sock.listen(1)

    while True:
        print("Server listening...")

        client_sock,address = server_sock.accept()
        print("Accepted connection from " + str(address))

        data = client_sock.recv(1024)
        print("received [%s]" % data)

        client_sock.close()
    
    server_sock.close()
    
if __name__ == "__main__":  
    main()