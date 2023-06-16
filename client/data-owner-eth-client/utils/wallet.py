#!/usr/bin/env python
from eth_account import Account
from config import config
import json
import os
import errno


def createKeystore(keypath):
    try:
        os.makedirs(os.path.dirname(keypath), exist_ok = True)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

def createAccount():
    keypath = config.keystore + config.acc_name
    createKeystore(keypath)
    acct = Account.create(config.acc_name)
    encrypted = acct.encrypt(config.acc_name)
    with open(keypath, 'w+') as keyfile:
        keyfile.write(json.dumps(encrypted))

def readAccount():
    keypath = config.keystore + config.acc_name
    if not os.path.exists(keypath):
        createAccount()
    with open(keypath, 'r') as encrypted:
        acct = json.load(encrypted)
        key = Account.decrypt(acct, config.acc_name)
        return config.acc_name, acct, key