#!/usr/bin/env python3
from eth_account import Account
import json
import os
import errno

keystore = 'keystore/eth/'

def createKeystore(keypath):
    if not os.path.exists(os.path.dirname(keypath)):
        try:
            os.makedirs(os.path.dirname(keypath))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def createAccount():
    name, mnemonic = getData()
    keypath = keystore + name
    createKeystore(keypath)

    acct = Account.create(mnemonic)
    print('\tYour account is: "' + acct.address + '"')

    encrypted = acct.encrypt(mnemonic)
    print('\tYour KeyFile is:', encrypted)
    with open(keypath, 'w+') as keyfile:
        keyfile.write(json.dumps(encrypted))

    print('Do not lose your mnemonic! They are essential to recover the account.')

def readAccount():
    name, mnemonic = getData()
    keypath = keystore + name
    with open(keypath, 'r') as encrypted:
        acct = json.load(encrypted)
        key = Account.decrypt(acct, mnemonic)
        #print('\tYour private key successfully readed:', acct.hex())
        return name, acct, key

def getData():
    name = input('\nPlease, introduce a name for your ETH account: ')
    mnemonic = name # input('Please, introduce a mnemonic for your ETH account: ')
    return name, mnemonic