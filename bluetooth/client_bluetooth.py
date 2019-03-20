import bluetooth

def main():
    # Create the client socket
    client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    #connect to the server on local Raspberry
    client_socket.connect(("7C:B0:C2:4F:CC:74", port))

    #Send data to server 'Hello World'
    client_socket.send("Hello World")


    print("Send")

    #close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
