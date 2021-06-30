#!/usr/bin/env python3
from utils import ledger, returns, wallet

def find_ended_progs(w3, contract, last, gateway):
    n = 1
    print('\nThis is the list of finished programs:\n\n')
    if last == 0:
        print('\nOops! There are no finished programs right now.\n')
    l2 = []
    while n <= last:
<<<<<<< HEAD
        if returns.return_state(w3, contract, n)[0] == 5:
=======
        if returns.return_state(contract, n)[0] == 4:
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
            l2.append(n)
            print("\nIn program",n,":\n")
            doc_loc = returns.return_prog_info_update(w3, contract, n, gateway)
            print("\t --> Documentation in: ", doc_loc, "\n")
        n += 1
    return l2

def my_progs(w3, Contract):
    last = Contract.functions.last().call()
    index = 1
    d = {}
    while index <= last:
        Im_subscribed = Contract.functions.account_repeated(index).call()
        if Im_subscribed == 0:
<<<<<<< HEAD
            ContractState = returns.return_state(w3, Contract, index)
            d[index] = ContractState[0]
            if ContractState[0] == 1:
                print('\nIn program ', index, '. ', ContractState[1],'.', ContractState[2], ContractState[3])
            elif ContractState[0] == 2:
                print('\nIn program ', index, '. ', ContractState[1],'.', ContractState[2], ContractState[3])
            elif ContractState[0] == 3:
                print('\nIn program ', index, '. ', ContractState[1],'.', ContractState[2], ContractState[3])
            elif ContractState[0] == 4: 
=======
            ContractState = returns.return_state(Contract, index)
            if ContractState[0] == 3:
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
                print('\nIn program ', index, '. ', ContractState[1])
            else:
                print('\nProgram ', index, ' is finished.')
        index = index + 1
    return d