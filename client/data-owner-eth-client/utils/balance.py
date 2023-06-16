#!/usr/bin/env python3
from utils import ledger, wallet, returns

def my_balance():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    Contract = ledger.getContract(w3)
    balance = Contract.functions.getBalance().call({'from': w3.eth.defaultAccount})
    print('\n\nYour balance is: ', balance / 10 ** 18)

def my_reputation():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    Contract = ledger.getContract(w3)
    reputation = returns.return_reputation(w3, Contract)
    print('\n\nYour reputation is: ', reputation)