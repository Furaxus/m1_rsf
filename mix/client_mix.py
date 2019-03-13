import bluetooth
import socket
import sys

wifi_address = ""
wifi_port = 1
filename = ""

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
    wifi_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    wifi_socket.connect((wifi_address,wifi_port))

    f = open(filename, 'wb')
    print ("Open file")
    while True:
        print("Receiving data...")
        data = s.recv(1024)
        if data.decode()=='END':
            print("End of data")
            break
        # write data to a file
        f.write(data)
    f.close()
    print("Close file")

    wifi_socket.close()
    # END OF WIFI PART


    # BLUETOOTH PART
    bluetooth_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    bluetooth_port = 1
    bluetooth_sock.bind(("",bluetooth_port))

    bluetooth_sock.listen(bluetooth_port)

    print("Waiting for command...")

    server_sock,address = bluetooth_sock.accept()
    print("Got connection from " + str(address))

    command = server_sock.recv(1024)
    print("Receive [%s]" % command)

    if (command == "EXEC")
        print("Execution of " + filename)
        os.system('chmod u+x ' + filename)
        os.system('./' + filename)

    server_sock.close()
    bluetooth_sock.close()
    # END OF BLUETOOTH PART


if __name__ == "__main__":  
    main()
