from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("7C:B0:C2:4F:CC:74", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
