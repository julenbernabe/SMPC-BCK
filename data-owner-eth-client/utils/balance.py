#!/usr/bin/env python3
from utils import ledger, wallet

def my_balance():
    cname, acct, key = wallet.readAccount()
    gateway='192.168.130.1'
    w3 = ledger.connectBlockchain(acct['address'], gateway)
    Contract = ledger.getContract(w3)
    balance = Contract.functions.balance().call()
    print('\n\nYour balance is: ', balance / 10 ** 18)