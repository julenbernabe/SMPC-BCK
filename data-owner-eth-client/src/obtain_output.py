#!/usr/bin/env python
from utils import ledger, returns, wallet

def load_data(key, w3, Contract, index, gateway):
    if returns.elected(w3, Contract, index) == 1:
        #Open files
        fp1 = open('../Data/NetworkData.txt', 'w')
        fp2 = open('../Data/other_info.txt', 'w')
        #Write CA information
        fp1.write('RootCA.crt\n')
        fp2.write(returns.return_CA(w3,Contract,index, gateway)+'\n')
        #Write number of players
        n = returns.return_n_players(w3, Contract, index)
        fp1.write(str(n)+'\n')
        #Write prog info location
        fp2.write(returns.return_prog_info(w3, Contract, index, gateway)+'\n')
        #Write progs location and preprocessing prog location
        l = returns.return_locs(w3, Contract, index, gateway)
        fp2.write(l[0]+'\n')
        fp2.write(l[1]+'\n')
        fp2.write(l[2]+'\n')
        #Write prime number
        fp2.write(str(returns.return_prime(w3, Contract, index))+'\n')
        #Write players information
        for i in range (n):
            l = returns.return_PlayerData(w3, Contract, index, i, gateway)
            if l[5] == 1:
                my_n = l[0]
            fp1.write(str(l[0]) + ' ' + l[1] + ' ' + l[2] + ' ' + l[3]+'\n')
            fp2.write(l[4]+'\n')
        fp1.write(str(0)+'\n')
        fp1.write(str(0))
        fp1.close()
        fp2.close()
        tx = Contract.functions.Im_ready(index).buildTransaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
        })
        ledger.signTransaction(w3, tx, key)
        return my_n
    else:
        print('\nOops! You were not selected for the MPC.')


def finished(key, w3, Contract, index):
    # The variable below must be changed according to the success of the SMPC. If it ended successfully, the variable will output
    # a 1. If not, the variable will output a 0.
    success = 1       
    tx = Contract.functions.finished(index, success).buildTransaction({
        'chainId': 1, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
    })
    ledger.signTransaction(w3, tx, key)
