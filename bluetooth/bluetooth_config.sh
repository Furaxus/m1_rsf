#! /bin/sh

if [ $# -gt 3 || ($# -eq 3 && $1 != "client") ] then
    echo "Usage : $0 [ client <bluetooth_adress_to connect> | server | config ]"
    exit 1
elif [ $# -eq 2 && $1 == "config"] then
    #print the bluetooth config of the device
    hciconfig
    exit 0
fi


bluetoothctl
power on
agent on
if [ $1 == "server" ] then
    #make device visible
    discoverable on
    scan on
else
    scan on
    #pair with the device at the $address address
    pair $2
fi