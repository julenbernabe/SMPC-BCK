#!/usr/bin/env python3
from src import events_consumer
from utils import ledger, returns, grouping
from ipfs import upload
from config import config
import os, sys



def main(key, w3, Contract, index, mpcPath):
    prog = mpcPath.split('/')[-1][:-4]
    selected_players = returns.return_Playerdata_private(w3, Contract, index)
    # Scientist is in selected_players[0]
    scientist = selected_players.pop(0)
    MODL = returns.return_MODL(w3, Contract, index)
    C = int(input('\n\nIntroduce the desired bin capacity considering that the MODL is ' + str(MODL) + ' and your data length is ' + str(scientist[1]) + ': '))
    bins, remaining = grouping.grouping(selected_players, C)
    # The remaining players will not be selected
    while len(bins) == 0:
        selected_players = returns.return_Playerdata_private(w3, Contract, index)
        # Scientist is in selected_players[0]
        selected_players.pop(0)
        C = int(input('You entered an excessively high capacity: ' + str(C) + '. Reduce it to at least ' + str(MODL - scientist[1]) + ': '))
        bins, remaining = grouping.grouping(selected_players, C)
    if len(remaining) != 0:
        bins.pop(remaining[0][1])
    current_bin = 0
    first = True
    data = [0, 0, scientist[2]]
    for bin in bins:
        print('\n\n##############################################################################################################################################################################################################\n\n')
        print('\n\t\t\t\t\t\t\t\t\t\t\tCHANGE YOUR MPC FILE\n\n')
        print('\n\t\t\t\t\t\t\t\tYour file is in: ' + mpcPath)
        print('\n\t\t\t\t\t\t\t\tThe list of players for this bin is:\n')
        count = 0
        i = 0
        indexes = []
        if first and scientist[1] > 0:
            first = False
            bin.append(scientist)
        else:
            bin.append(data)
        for elem in bin:
            count += elem[1]
            i += 1
            indexes.append(elem[0])
            if elem[0] == scientist[0]:
                print('\n\t\t\t\t\t\t\t\t --> Player ', i, ': YOU \t\t Dataset size: ', elem[1])
            else:
                print('\n\t\t\t\t\t\t\t\t --> Player ', i, ': ', elem[0], '\t\t Dataset size: ', elem[1]*C)
        print('\n\n\t\t\t\t\t\t\t\tTotal number of players: ', len(bin))
        print('\n\t\t\t\t\t\t\t\tChange it according to the above list. Do not continue this program until changed.')
        print('\n\n##############################################################################################################################################################################################################')
        cont = int(input('\n\nEnter 1 when you are ready to continue or 0 if you want to skip this bin: '))
        while cont != 0 and cont != 1:
            print('You entered ', cont, ' and that is not a valid value.')
            cont = int(input('\n\nEnter 1 when you are ready to continue or 0 if you want to skip this bin: '))
        if cont == 1:
            success = os.system('cd ' + config.mpc_data_loc + '; ./compile.py /app/client/'+ config.programs_loc[2:] + prog + '/' + prog +'.mpc')
            if success == 0:
                bc_path = config.mpc_data_loc + '/Programs/Bytecode/' + prog + '-0.bc'
                sch_path = config.mpc_data_loc + '/Programs/Schedules/' + prog + '.sch'
                change_sch(sch_path)
                bc_hash = upload.upload_file(bc_path)
                sch_hash = upload.upload_file(sch_path)
                tx = Contract.functions.scientistReady(indexes, bc_hash, sch_hash, index, len(bins), current_bin).build_transaction({
                    'chainId': 1, 'gas': 700000, 'gasPrice': 0,
                    'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
                })
                ledger.sign_transaction(w3, tx, key)
                events_consumer.bin(key, w3, Contract, index, current_bin)
            else:
                print('Compilation failed. Check if the file is in this location: /app/client/'+ config.programs_loc[2:] + prog + '/' + prog +'.mpc')
                sys.exit()
        elif cont == 0:
            print('Skipping this bin...')
        current_bin += 1
    sys.exit()
        


def change_sch(path):
    f = open(path, 'r')
    l = f.readlines()
    index = l[2].find('-0')
    l[2] = 'current' + l[2][index:]
    f.close()
    f2 = open(path, 'w')
    for line in l:
        f2.write(line)
    f2.close()