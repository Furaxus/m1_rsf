#! /bin/sh

#address of the device to connect
address = "00:00:00:00:00:00"

if [ $# -gt 2 ] then
    echo "Usage : $0 <bluetooth_adress>"
    exit 1
elif [ $# -eq 1 ] then
    #print the bluetooth config of the device
    hciconfig
    exit 0
elif [ $# -eq 2 ] then
    #init the different variable
    address = $1
fi

#pair with the device at the $address address
pair $address