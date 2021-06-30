<<<<<<< HEAD
#!/usr/bin/env python3
from utils import ledger, returns

def load_data(key, w3, Contract, index, gateway):
    if returns.elected(w3, Contract, index) == 1:
=======
#!/usr/bin/env python
from utils import ledger, returns

def load_data(key, w3, Contract, index):
    if returns.elected(Contract, index) == 1:
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
        #Open files
        fp1 = open('sm/NetworkData.txt', 'w')
        fp2 = open('sm/other_info.txt', 'w')
        #Write CA information
        fp1.write('RootCA.crt\n')
<<<<<<< HEAD
        fp2.write(returns.return_CA(w3,Contract,index, gateway)+'\n')
=======
        fp2.write(returns.return_CA(Contract,index)+'\n')
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
        #Write number of players
        n = returns.return_n_players(Contract, index)
        fp1.write(str(n)+'\n')
        #Write prog info location
<<<<<<< HEAD
        fp2.write(returns.return_prog_info(w3, Contract, index, gateway)+'\n')
        #Write progs location and preprocessing prog location
        l = returns.return_locs(w3, Contract, index, gateway)
=======
        fp2.write(returns.return_prog_info(Contract, index)+'\n')
        #Write progs location and preprocessing prog location
        l = returns.return_locs(Contract, index)
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
        fp2.write(l[0]+'\n')
        fp2.write(l[1]+'\n')
        fp2.write(l[2]+'\n')
        #Write prime number
        fp2.write(str(returns.return_prime(Contract, index))+'\n')
        #Write players information
        for i in range (n):
<<<<<<< HEAD
            l = returns.return_PlayerData(w3, Contract, index, i, gateway)
=======
            l = returns.return_PlayerData(Contract, index, i)
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
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
    elif returns.elected(w3, Contract, index) == 2:
        print('\nYou already have downloaded all the files, so you are ready to start the SMPC.\n')
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