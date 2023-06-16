#!/usr/bin/env python
from utils import ledger
from ipfs import download
import os
from config import config

def return_CA(w3, contract, index):
    CA = contract.functions.getCA(index).call({'from': w3.eth.defaultAccount})
    download.main(config.mpc_data_loc + 'Player-Data', CA)
    return change_filename('Player-Data', CA, 'RootCA.crt')

def return_registered(w3, contract):
    return contract.functions.getRegistered().call({'from': w3.eth.defaultAccount})

def return_payment_prediction(w3, contract, index):
    x = contract.functions.getPaymentPrediction(index).call({'from': w3.eth.defaultAccount})
    payment_per_item = x[0] / x[1]
    tokens_per_item = payment_per_item / 10 ** 18
    return tokens_per_item / 2, tokens_per_item

def return_minimum_reputation(w3, contract, index):
    return contract.functions.getMinimumReputation(index).call({'from': w3.eth.defaultAccount})

def return_MODL(w3, contract, index):
    return contract.functions.getMODL(index).call({'from': w3.eth.defaultAccount})

def return_reputation(w3, contract):
    return contract.functions.getReputation().call({'from': w3.eth.defaultAccount})

def return_balance(w3, contract):
    balance = contract.functions.balance().call({'from': w3.eth.defaultAccount})
    return balance / 10 ** 18

def return_n_players(w3, contract, index):
    n = contract.functions.getTotalPlayers(index).call({'from': w3.eth.defaultAccount})
    return n

def return_prog_info(w3, contract, index):
    info_file = contract.functions.getInfoFileLocation(index).call({'from': w3.eth.defaultAccount})
    download.main(config.mpc_data_loc + 'Programs/current', info_file)
    return change_filename('Programs/current', info_file, 'current.txt')

def return_locs(w3, contract, index):
    locs_list = contract.functions.getExecutionFilesLocation(index).call({'from': w3.eth.defaultAccount})
    download.main(config.mpc_data_loc + 'Programs/Bytecode', locs_list[0])
    bc_path = change_filename('Programs/Bytecode', locs_list[0], 'current-0.bc')
    download.main(config.mpc_data_loc + 'Programs/Schedules', locs_list[1])
    sch_path = change_filename('Programs/Schedules', locs_list[1], 'current.sch')
    download.main(config.mpc_data_loc + 'Programs/Source', locs_list[2])
    prep_path = change_filename('Programs/Source', locs_list[2], 'current.py')
    return bc_path, sch_path, prep_path

def return_prime(w3, contract, index):
    p = contract.functions.return_prime(index).call({'from': w3.eth.defaultAccount})
    return p

def return_PlayerData(w3, contract, index, n):
    info_list = contract.functions.getPlayerData(n, index).call({'from': w3.eth.defaultAccount})
    download.main(config.mpc_data_loc + 'Player-Data', info_list[2])
    new_name = 'P' + str(n) + '.pem'
    path = change_filename('Player-Data', info_list[2], new_name)
    return info_list[0], info_list[1], new_name, info_list[3], path, info_list[4]

def return_state(w3, contract, index):
    state = contract.functions.getCampaignState(index).call({'from': w3.eth.defaultAccount})
    return state

def return_last(w3, contract):
    last = contract.functions.last().call({'from': w3.eth.defaultAccount})
    return last

def elected(w3, contract,index):
    return contract.functions.getElected(index).call({'from': w3.eth.defaultAccount})

def change_filename(file_path, old_name, new_name):
    old_path = config.mpc_data_loc + '/' + file_path + '/' + old_name
    new_path = config.mpc_data_loc + '/' + file_path + '/' + new_name
    os.rename(old_path,new_path)
    return new_path