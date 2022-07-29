# 라즈베리 파이에서 eth0의 아이피 주소

import socket, sys, os
import netifaces as ni

hostname = socket.gethostname()
hostAddr = socket.gethostbyname(hostname)
print("Hostname = ", hostname)
print("HostAddr = ", hostAddr)

net_interfaces = ni.interfaces()
print("net_interfaces = ", net_interfaces)

ipAddr_eth0 = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
print("ipAddr_eth0 = ", ipAddr_eth0)
