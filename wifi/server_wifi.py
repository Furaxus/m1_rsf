#!/usr/bin/env python

import sys                      # Import sys module
import socket                   # Import socket module
import time

def main():
    s = socket.socket()             # Create a socket object
    host = ""                       # Get local machine name
    port = -1                       # Port to listen
    filename = ""                   # Filename to execute
    
    # Get configuration from config file
    config_file = open("config.conf")
    for line in config_file:
        param = line.split(' ')
        if param[0] == "IP":
            host = param[1]
        elif param[0] == "PORT":
            port = int(param[1])
        elif param[0] == "FILENAME_CLT":
            filename = param[1]
    config_file.close()
    

    s.bind((host, port))            # Bind to the port
    s.listen(port)                  # Now wait for client connection.


    print ('Server listening....')
    conn, addr = s.accept()         # Establish connection with client.
    print ('Got connection from ' + str(addr))

    f = open(filename,'rb')         # Open exec file
    # Read data and send data
    l = f.read(1024)
    while (l):
        conn.send(l)
        #print('Sent ',repr(l))
        l = f.read(1024)
    f.close()                       # Close file

    print('Done sending')
    time.sleep(3)                   # Waiting time for synchro
    conn.send('END'.encode())
    conn.send('EXEC'.encode())      # Sending execution order
    conn.close()                    # Closing connection
        
    

if __name__ == "__main__":  
    main()
