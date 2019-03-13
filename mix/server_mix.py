import bluetooth
import socket

wifi_address = ""                   # Get local machine name
wifi_port = 1                       # Port to listen
filename = ""                       # Filename to execute

def read_config():
    global wifi_address
    global wifi_port
    global filename

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
    wifi_socket = socket.socket()
    wifi_socket.bind((wifi_address, wifi_port))
    wifi_socket.listen(wifi_port)
    print('Server listening....')

    conn, addr = wifi_socket.accept()
    print('Got connection from ' + str(addr))

    f = open(filename,'rb')
    print("Open file")
    l = f.read(1024)
    print(l)
    while (l):
        conn.send(l)
        print('Sent ',repr(l))
        l = f.read(1024)
    f.close()
    print("Close file")

    print('Done sending')
    time.sleep(3)
    conn.send('END'.encode())
    conn.close()
    # END OF WIFI PART



    # BLUETOOTH PART
    bluetooth_port = 1
    bluetooth_address = "7C:B0:C2:4F:CC:74"
    bluetooth_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    bluetooth_socket.connect((bluetooth_address, port))

    bluetooth_socket.send("EXEC")
    print("Send EXEC")

    bluetooth_socket.close()
    # END OF BLUETOOTH PART

    
if __name__ == "__main__":  
    main()