import bluetooth
import socket

wifi_address = ""                   # Get local machine name
wifi_port = 1                       # Port to listen
filename = ""                       # Filename to execute

def read_config():
    global wifi_address
    global wifi_port
    global filename

    # Get configuration from config file
    config_file = open("wifi_config.conf")
    for line in config_file:
        param = line.split(' ')
        if param[0] == "IP":
            wifi_address = param[1]
        elif param[0] == "PORT":
            wifi_port = int(param[1])
        elif param[0] == "FILENAME_CLT":
            filename = param[1]
    config_file.close()

def main():
    global wifi_address
    global wifi_port
    global filename

    # WIFI PART
    wifi_socket = socket.socket()                   # Create wifi socket
    wifi_socket.bind((wifi_address, wifi_port))     # Bind to the port
    wifi_socket.listen(wifi_port)                   # Now wait for client connection.
    print('Server listening....')

    conn, addr = wifi_socket.accept()               # Receive connection
    print('Got connection from ' + str(addr))

    f = open(filename,'rb')                         # Open exec file
    print("Open file")
    # Read and send data
    l = f.read(1024)
    while (l):
        conn.send(l)
        l = f.read(1024)
    f.close()                                       # Close file
    print("Close file")

    print('Done sending')
    time.sleep(3)                                   # Waiting time for synchro
    conn.send('END'.encode())
    conn.close()                                    # Closing connection
    # END OF WIFI PART



    # BLUETOOTH PART
    bluetooth_port = 1                                              # Bluetooth port
    bluetooth_address = "7C:B0:C2:4F:CC:74"                         # Target bluetooth device
    bluetooth_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  # Bluetooth socket creation
    bluetooth_socket.connect((bluetooth_address, port))             # Connection

    bluetooth_socket.send("EXEC")                   # Sending execution order
    print("Send EXEC")

    bluetooth_socket.close()                        # Close connection
    # END OF BLUETOOTH PART

    
if __name__ == "__main__":  
    main()