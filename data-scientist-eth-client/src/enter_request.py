#!/usr/bin/env python3
import socket
from src import events_consumer
from utils import ledger, wallet

def main():
    prog = input('\n\nIntroduce a program name from the above ones: ')
    cname, acct, key = wallet.readAccount()
    gateway='192.168.130.1'
    w3 = ledger.connectBlockchain(acct['address'], gateway)
    l = ledger.getContract(w3)
    Contract = l[0]
    events_consumer.other(key, w3, Contract, gateway, prog)