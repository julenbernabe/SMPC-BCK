#!/usr/bin/env python
from utils import ledger, finder, wallet, returns
from ipfs import upload
from config import config
import sys

def main():
    print('\n\n################################')
    print('\n           SIGN UP\n')
    print('################################\n\n')
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    Contract = ledger.getContract(w3)
    if returns.return_registered(w3, Contract) == 0:
        x = input('\n\nYou were not registered in the marketplace. Do you want to register? [y/n] ')
        if x == 'y':
            reg = Contract.functions.register().build_transaction({
                'chainId': 1, 'gas': 700000, 'gasPrice': 0,
                'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
            })
            ledger.sign_transaction(w3, reg, key)
        else:
            sys.exit()
    n = finder.choose_prog(w3,Contract)
    if n == 0:
        print('Aborting subscription...\n\n')
        return '', '', '', '', '', n
    else:
        MODL = returns.return_MODL(w3, Contract, n)
        my_data_length = int(input('\nIntroduce your data length (less than the MODL = ' + str(MODL) + '):\n'))
        while my_data_length >= MODL:
            my_data_length = int(input('\nPlease enter a valid size (less than the MODL = ' + str(MODL) + '):\n'))
        rep = returns.return_minimum_reputation(w3, Contract, n)
        my_rep = returns.return_reputation(w3, Contract)
        gambled_rep = int(input('\nThe minimum reputation is ' + str(rep) + ' and your reputation is ' + str(my_rep) + '. Enter the reputation you want to stake for this campaign:\n'))
        while gambled_rep < rep or gambled_rep > my_rep:
            gambled_rep = int(input('\nPlease enter a valid reputation (between ' + str(rep) + ' and ' + str(my_rep) +'):\n'))
        # IP, CRT_name, CN = _docker.getPlayerInfo(cname)
        # For test purpose only
        CRT = upload.upload_file(config.cert_file_loc)
        tx = Contract.functions.subscribe(my_data_length, config.IP, CRT, config.common_name, n, gambled_rep).build_transaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
        })
        ledger.sign_transaction(w3, tx, key)
        print("\nTransaction done!\n\n")
    return cname, acct, key, w3, Contract, n