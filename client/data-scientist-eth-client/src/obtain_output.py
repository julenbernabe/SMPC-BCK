#!/usr/bin/env python3
from utils import ledger, returns
from config import config
import os, shutil

def load_data(key, w3, Contract, index):
    if returns.elected(w3, Contract, index) == 1:
        #Open files
        fp1 = open(config.mpc_data_loc + 'hosts', 'w')
        fp2 = open(config.mpc_data_loc + 'other_info.txt', 'w')
        #Write CA information
        fp2.write(returns.return_CA(w3, Contract, index)+'\n')
        #Number of players
        n = returns.return_n_players(w3, Contract, index)
        #Write prog info location
        fp2.write(returns.return_prog_info(w3, Contract, index)+'\n')
        #Write progs location and preprocessing prog location
        l = returns.return_locs(w3, Contract, index)
        fp2.write(l[0]+'\n')
        fp2.write(l[1]+'\n')
        fp2.write(l[2]+'\n')
        #Write players information
        d = dict()
        indexes = []
        for i in range (n):
            l = returns.return_PlayerData(w3, Contract, index, i)
            if l[5] == 1:
                my_n = len(indexes)
                config.my_n = my_n
                shutil.copy2(config.key_file_loc, config.mpc_data_loc + 'Player-Data/P' + str(my_n) + '.key')
                shutil.copy2(config.input_file_loc, config.mpc_data_loc + 'Player-Data/Input-P' + str(my_n) + '-0')
            d[l[0]] = l
            indexes.append(l[0])
        for i in range (len(indexes)):
            fp1.write(str(d[indexes[i]][1] + ':' + '500' + str(i) +'\n'))
            fp2.write(d[indexes[i]][4]+'\n')
        fp1.close()
        fp2.close()
        os.system('c_rehash ' + config.mpc_data_loc + 'Player-Data')
        tx = Contract.functions.playerReady(index).build_transaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
        })
        ledger.sign_transaction(w3, tx, key)
        return my_n
    elif returns.elected(w3, Contract, index) == 2:
        print('\nYou already have downloaded all the files, so you are ready to start the SMPC.\n')
        return config.my_n
    else:
        print('\nOops! You were not selected for the SMPC.')
        return config.my_n


def finished(key, w3, Contract, index, success, n):
    # The variable below must be changed according to the success of the SMPC. If it ended successfully, the variable will output
    # a 1. If not, the variable will output a 0.
    if success == 0:
        shutil.copy2(config.mpc_data_loc + 'Player-Data/Output-P' + str(n) + '-0', config.output_file_loc)
        suc = 1
    else:
        suc = 0
    tx = Contract.functions.finished(index, suc).build_transaction({
        'chainId': 1, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
    })
    ledger.sign_transaction(w3, tx, key)