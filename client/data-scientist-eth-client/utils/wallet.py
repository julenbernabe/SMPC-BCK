#!/usr/bin/env python
from eth_account import Account
from config import config
import json
import os
import errno


def createKeystore(keypath):
    if not os.path.exists(os.path.dirname(keypath)):
        try:
            os.makedirs(os.path.dirname(keypath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

def createAccount():
    mnemonic = config.acc_name
    keypath = config.keystore + config.acc_name
    createKeystore(keypath)
    acct = Account.create(mnemonic)
    encrypted = acct.encrypt(mnemonic)
    with open(keypath, 'w+') as keyfile:
        keyfile.write(json.dumps(encrypted))
    

def readAccount():
    mnemonic = config.acc_name
    keypath = config.keystore + config.acc_name
    if not os.path.exists(keypath):
        createAccount()
    with open(keypath, 'r') as encrypted:
        acct = json.load(encrypted)
        key = Account.decrypt(acct, mnemonic)
        return config.acc_name, acct, key