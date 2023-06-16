#!/usr/bin/env python3
from utils import ledger, returns, wallet

def find_ended_progs(w3, contract):
    n = 1
    print('\nThis is the list of finished programs:\n\n')
    last = contract.functions.last().call({'from': w3.eth.defaultAccount})
    l2 = []
    while n <= last:
        if returns.return_state(w3, contract, n)[0] == 5:
            l2.append(n)
            print("\nIn program",n,":\n")
            doc_loc = returns.return_prog_info_update(w3, contract, n)
            print("\t --> Documentation in: ", doc_loc, "\n")
            mpc_loc = returns.return_mpcPath(w3, contract, n)
            print("\t --> MPC program location: ", mpc_loc, "\n")
        n += 1
    if len(l2) == 0:
        print('\nOops! There are no finished programs right now.\n')
    return l2

def my_progs(w3, Contract):
    last = Contract.functions.last().call({'from': w3.eth.defaultAccount})
    index = 1
    d = {}
    while index <= last:
        Im_subscribed = Contract.functions.repeated(index).call({'from': w3.eth.defaultAccount})
        if Im_subscribed == 0:
            ContractState = returns.return_state(w3, Contract, index)
            d[index] = ContractState[0]
            if ContractState[0] == 1:
                print('\nIn program ', index, '. ', ContractState[1],'.', ContractState[2], ContractState[3])
            elif ContractState[0] == 2:
                print('\nIn program ', index, '. ', ContractState[1],'.', ContractState[2], ContractState[3])
            elif ContractState[0] == 3:
                print('\nIn program ', index, '. ', ContractState[1],'.', ContractState[2], ContractState[3])
            elif ContractState[0] == 4: 
                print('\nIn program ', index, '. ', ContractState[1])
            else:
                print('\nProgram ', index, ' is finished.')
        index = index + 1
    return d