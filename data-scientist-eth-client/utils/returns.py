<<<<<<< HEAD
#!/usr/bin/env python3

from ipfs import download
import os

def return_CA(w3, contract, index, gateway):
=======
#!/usr/bin/env python
from ipfs import download
import os

def return_CA(contract, index):
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
    CA = contract.functions.return_CA(index).call()
    download.main('../Cert-Store',CA, gateway)
    return change_filename('Cert-Store', CA, 'RootCA.crt')

def return_registered(w3, contract):
    return contract.functions.return_registered().call()

def return_payment(w3, contract, index):
    return contract.functions.return_payment(index).call()[0] / 10 ** 18
    
def return_required_reputation(w3, contract, index):
    return contract.functions.return_required_reputation(index).call()

def return_MODL(w3, contract, index):
    return contract.functions.return_MODL(index).call()

def return_reputation(w3, contract):
    return contract.functions.return_reputation().call()

def return_balance(w3, contract):
    balance = contract.functions.balance().call()
    return balance / 10 ** 18

def return_n_players(contract, index):
    n = contract.functions.return_n_players(index).call()
    return n

def return_subscribed_players(contract, index):
    n = contract.functions.return_subscribed_n(index).call()
    return n

<<<<<<< HEAD
def return_prog_info(w3, contract, index, gateway):
=======
def return_prog_info(contract, index):
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
    info_file = contract.functions.return_info(index).call()
    download.main('../Programs/current',info_file, gateway)
    return change_filename('Programs/current', info_file, 'current.txt')

def return_prog_info_update(w3, contract, index, gateway):
    info_file = contract.functions.return_info(index).call()
    download.update('../Programs/finished',info_file, gateway)
    return change_filename('Programs/finished', info_file, 'prog_' + str(index) + '.txt')

<<<<<<< HEAD
def return_locs(w3, contract, index, gateway):
=======
def return_locs(contract, index):
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
    locs_list = contract.functions.return_locs(index).call()
    download.main('../Programs/current',locs_list[0], gateway)
    bc_path = change_filename('Programs/current', locs_list[0], 'current.bc')
    download.main('../Programs/current',locs_list[1], gateway)
    sch_path = change_filename('Programs/current', locs_list[1], 'current.sch')
    download.main('../Programs/current', locs_list[2], gateway)
    prep_path = change_filename('Programs/current', locs_list[2], 'current.py')
    return bc_path, sch_path, prep_path

def return_prime(contract, index):
    p = contract.functions.return_prime(index).call()
    return p

<<<<<<< HEAD
def return_PlayerData(w3, contract, index, n, gateway):
=======
def return_PlayerData(contract, index, n):
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
    info_list = contract.functions.return_PlayerData(n, index).call()
    download.main('../Cert-Store',info_list[2], gateway)
    new_name = 'player' + str(n) + '.crt'
    path = change_filename('Cert-Store', info_list[2], new_name)
    return info_list[0], info_list[1], new_name, info_list[3], path, info_list[4]

def return_state(contract, index):
    state = contract.functions.return_state(index).call()
    return state

def return_last(contract):
    last = contract.functions.last().call()
    return last

def elected(contract,index):
    return contract.functions._elected(index).call()
<<<<<<< HEAD

# This function receives players' addresses and dataset sizes as input, and outputs a list of the addresses ordered from larger to 
# shorter dataset length.
def return_Playerdata_private(w3, contract, index):
    subscribed_players = return_subscribed_players(w3, contract, index)
=======
def return_Playerdata_private(contract, index):
    subscribed_players = return_subscribed_players(contract, index)
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
    M = list()
    i = 1
    while i < subscribed_players:
        row = list()
        row.append(contract.functions.return_PlayerData_private(i, index).call()[0])
        row.append(contract.functions.return_PlayerData_private(i, index).call()[1])
        M.append(row)
        i += 1
    M.sort(key = takeSecond, reverse=True)
    return M

def takeSecond(l):
    return l[1]

def change_filename(file_path, old_name, new_name):
    old_path = '/root/SCALE-MAMBA' + '/' + file_path + '/' + old_name
    new_path = '/root/SCALE-MAMBA' + '/' + file_path + '/' + new_name
    os.rename(old_path,new_path)
    return new_path