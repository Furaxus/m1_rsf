import bluetooth

def main():
    # Create the client socket
    client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 3
    client_socket.connect(("00:12:D2:5A:BD:E4", port))

    client_socket.send("Hello World")

    print("Send")

    client_socket.close()

if __name__ == "__main__":  
    main()
