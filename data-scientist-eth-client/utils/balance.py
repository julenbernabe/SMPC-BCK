#!/usr/bin/env python3
from utils import ledger, wallet

def my_balance():
    cname, acct, key = wallet.readAccount()
    gateway='192.168.130.1'
    w3 = ledger.connectBlockchain(acct['address'], gateway)
    l = ledger.getContract(w3)
    Contract = l[0]
    balance = Contract.functions.balance().call()
    print('\n\nYour balance is: ', balance / 10 ** 18)

def increase():
    cname, acct, key = wallet.readAccount()
    gateway='192.168.130.1'
    w3 = ledger.connectBlockchain(acct['address'], gateway)
    l = ledger.getContract(w3)
    Contract = l[0]
    tokens = int(input('\nIntroduce the amount of tokens you want to receive: '))
    amount = tokens * 10 ** 18
    tx = Contract.functions.withdraw(amount).buildTransaction({
        'chainId': 1, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
    })
    ledger.signTransaction(w3, tx, key)