#!/usr/bin/env python

import socket                   # Import socket module
import time
import subprocess
import sys
import os

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)             # Create a socket object

    host = ""                   # Ip address that the TCPServer  is there
    port = -1                   # Reserve a port for your service every new transfer wants a new port or you must wait.
    filename = ""


    config_file = open("config.conf")
    #get configuration from config file
    for line in config_file:
        param = line.split(' ')
        if param[0] == "IP":
            host = param[1]
        elif param[0] == "PORT":
            port = int(param[1])
        elif param[0] == "FILENAME_CLT":
            l = param[1].split('\n')
            filename = l[0]

    config_file.close()

    #connect to the server
    s.connect((host, port))
    with open(filename, 'wb') as f:
        print ('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            if data.decode()=='END':
                print('Receive END')
                break
            # write data to a file
            f.write(data)
    #close file
    f.close()
    print('Successfully get the file')
    commande=s.recv(1024).decode()
    print('Receive command : '+ commande)
    print('Execution...')
    #change right of the file exec
    os.system('chmod u+x ' + filename)
    if commande == "EXEC":
        #execute commande from file
        os.system('./' + filename)
    print('End of execution')
    #close connection
    s.close()
    print('Connection closed')



if __name__ == "__main__":
    main()
