#!/usr/bin/env python
from utils import ledger
from ipfs import download
import os

def return_CA(w3, contract, index, gateway):
    CA = contract.functions.return_CA(index).call()
    download.main('../Cert-Store',CA, gateway)
    return change_filename('Cert-Store', CA, 'RootCA.crt')

def return_registered(w3, contract):
    return contract.functions.return_registered().call()

def return_payment(w3, contract, index):
    x = contract.functions.return_payment(index).call()
    payment_per_item = x[0] / x[1]
    tokens_per_item = payment_per_item / 10 ** 18
    return tokens_per_item / 2, tokens_per_item

def return_required_reputation(w3, contract, index):
    return contract.functions.return_required_reputation(index).call()

def return_MODL(w3, contract, index):
    return contract.functions.return_MODL(index).call()

def return_reputation(w3, contract):
    return contract.functions.return_reputation().call()

def return_balance(w3, contract):
    balance = contract.functions.balance().call()
    return balance / 10 ** 18

def return_n_players(w3, contract, index):
    n = contract.functions.return_n_players(index).call()
    return n

def return_prog_info(w3, contract, index, gateway):
    info_file = contract.functions.return_info(index).call()
    download.main('../Programs/current',info_file, gateway)
    return change_filename('Programs/current', info_file, 'current.txt')

def return_locs(w3, contract, index, gateway):
    locs_list = contract.functions.return_locs(index).call()
    download.main('../Programs/current',locs_list[0], gateway)
    bc_path = change_filename('Programs/current', locs_list[0], 'current.bc')
    download.main('../Programs/current',locs_list[1], gateway)
    sch_path = change_filename('Programs/current', locs_list[1], 'current.sch')
    download.main('../Programs/current', locs_list[2], gateway)
    prep_path = change_filename('Programs/current', locs_list[2], 'current.py')
    return bc_path, sch_path, prep_path

def return_prime(w3, contract, index):
    p = contract.functions.return_prime(index).call()
    return p

def return_PlayerData(w3, contract, index, n, gateway):
    info_list = contract.functions.return_PlayerData(n, index).call()
    download.main('../Cert-Store',info_list[2], gateway)
    new_name = 'player' + str(n) + '.crt'
    path = change_filename('Cert-Store', info_list[2], new_name)
    return info_list[0], info_list[1], new_name, info_list[3], path, info_list[4]

def return_state(w3, contract, index):
    state = contract.functions.return_state(index).call()
    return state

def return_last(w3, contract):
    last = contract.functions.last().call()
    return last

def elected(w3,contract,index):
    return contract.functions._elected(index).call()

def change_filename(file_path, old_name, new_name):
    old_path = '/root/SCALE-MAMBA' + '/' + file_path + '/' + old_name
    new_path = '/root/SCALE-MAMBA' + '/' + file_path + '/' + new_name
    os.rename(old_path,new_path)
    return new_path