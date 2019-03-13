import bluetooth

def main():
    # Create the client socket
    client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 3
    client_socket.connect(("7C:B0:C2:4F:CC:74", 3))

    client_socket.send("Hello World")


    print("Send")

    client_socket.close()

if __name__ == "__main__":  
    main()
