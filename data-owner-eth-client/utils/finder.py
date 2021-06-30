#!/usr/bin/env python
from utils import ledger, returns, wallet


def find_active_progs(w3, contract, last):
    n = 1
    print('\nList of programs:\n\n')
    if last == 0:
        print('\nOops! There are no programs at subscribing time right now.\n')
    l2 = []
    while n <= last:
        l1 = returns.return_state(w3, contract, n)
        if l1[0] == 1:
            my_rep = returns.return_reputation(w3,contract)
            rep = returns.return_required_reputation(w3, contract, n)
            if my_rep >= rep:
                l2.append(n)
                print("\nIn program",n,": ")
                print("\n\t -->", l1[1]," ",l1[2]," ",l1[3])
                print("\n\t --> Required reputation: ", returns.return_required_reputation(w3, contract, n))
                print("\n\t --> MODL for the request: ", returns.return_MODL(w3, contract, n))
                lower, upper = returns.return_payment(w3, contract, n)
                print("\n\t --> Reward between ", lower, " and", upper, "tokens per data item used.\n")
        n += 1
    return l2
    
def choose_prog(w3, contract):
    last = contract.functions.last().call()
    l = find_active_progs(w3, contract, last)
    if len(l) == 0:
        print('\nOops! There are no programs at subscribing time right now.\n')
        return 0
    else:
        index = int(input('\n\nEnter the program index of the program you want to choose:\n'))
        if index in l:
            return index
        else:
            while index not in l and index != 0:
                index = int(input('\nTry a possible number or enter 0 to exit:\n'))
            return index