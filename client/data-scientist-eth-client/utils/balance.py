#!/usr/bin/env python3
from utils import ledger, wallet, returns

def my_balance():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    l = ledger.getContract(w3)
    Contract = l[0]
    balance = Contract.functions.getBalance().call({'from': w3.eth.defaultAccount})
    return balance / 10 ** 18

def balance_printer():   
    balance = my_balance() 
    print('\n\nYour balance is: ', balance)

def my_reputation():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    l = ledger.getContract(w3)
    Contract = l[0]
    reputation = returns.return_reputation(w3, Contract)
    print('\n\nYour reputation is: ', reputation)

def increase_balance():
    tokens = int(input('\nIntroduce the amount of tokens you want to receive: '))
    increase(tokens)

def increase(tokens):
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    Contract = ledger.getToken(w3)
    amount = tokens * 10 ** 18
    tx = Contract.functions.withdraw(amount).build_transaction({
        'chainId': 5777, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
    })
    ledger.sign_transaction(w3, tx, key)