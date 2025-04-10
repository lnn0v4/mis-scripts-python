#!/usr/bin/env python3

import time
import sys
import scapy.all as scapy
import signal 
from termcolor import colored
import argparse

def headler(sig,frame):
    print(colored(f"\n\nSaliendo ..\n\n",'blue'))
    sys.exit(1)

signal.signal(signal.SIGINT,headler)

def get_arguments():
    parser = argparse.ArgumentParser(description="SCAN NETWORK")
    parser.add_argument("-t","--target",required=True,dest="target",help="python3 Scan_Network.py -t <IP-target>/24")
    args = parser.parse_args()
    return args.target

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast / arp_packet
    answered , unanswered = scapy.srp(arp_packet , timeout=1 , verbose=False)
    response = answered.summary()
    if response:
        print(response)

def main():
    target = get_arguments()
    scan(target)

if __name__ == '__main__':
    main()
    time.sleep(5)
