import bluetooth


def main():
    channel = 1                                                     # Bluetooth channel
    server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)         # Socket creation
    server_sock.bind(("",channel))                                  # Socket binding

    server_sock.listen(channel)                                     # Channel listening

    print("Server listening...")

    client_sock,address = server_sock.accept()                      # Receive connection
    print("Accepted connection from " + str(address))

    data = client_sock.recv(1024)                                   # Receive data
    print("received [%s]" % data)

    client_sock.close()                                             # Close client connection
    
    server_sock.close()                                             # Close server socket
    
if __name__ == "__main__":  
    main()