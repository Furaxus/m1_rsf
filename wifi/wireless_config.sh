#! /bin/sh

address="192.168.1.69"
wlan="RPISIAME"
chan=4
port=5000
file_name="exec.sh"

if [ $# -gt 5 ]
then
	echo "Usage : $0 <local_address> <ssid> <port> <channel>"
	exit 0
fi
if [ $# -eq 5 ]
then
	chan = $4
fi
if [ $# -ge 4 ]
then
	port = $1
fi
if [ $# -ge 3 ]
then
	ssid = $1
fi
if [ $# -ge 2 ]
then
	address = $1
fi

sudo iwconfig wlan0 channel $chan essid $wlan mode ad-hoc
sudo ifconfig wlan0 $address netmask 255.255.255.0

echo "IP $address" > config.conf
echo "SSID $wlan" >> config.conf
echo "CHANNEL $chan" >> config.conf
echo "PORT $port" >> config.conf
echo "FILENAME_CLT $file_name" >> config.conf
echo "FILENAME_SRV src_$file_name" >> config.conf


echo "Connected to $wlan (channel $chan) as $address"
