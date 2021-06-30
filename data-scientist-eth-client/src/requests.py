#!/usr/bin/env python3
import socket
from src import events_consumer
from utils import ledger, wallet, finder, returns
from ipfs import upload
<<<<<<< HEAD
import sys
=======
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a

def new():
    prog = input('\n\nIntroduce a program name from the above ones: ')
    cname, acct, key = wallet.readAccount()
    gateway='192.168.130.1'
    w3 = ledger.connectBlockchain(acct['address'], gateway)
    l = ledger.getContract(w3)
    Token = ledger.getToken(w3)
    Contract = l[0]
    contractAddress = l[1]
    if returns.return_registered(w3, Contract) == 0:
        x = input('\n\nYou were not registered in the marketplace. Do you want to register? [y/n]')
        if x == 'y':
            reg = Contract.functions.register().buildTransaction({
                'chainId': 1, 'gas': 700000, 'gasPrice': 0,
                'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
            })
            ledger.signTransaction(w3, reg, key)
        else:
            sys.exit()
    MODL = int(input('\nWhat is the required MODL (Minimum Overall Data Length)?\n'))
    data_length = int(input('\nWhat is your data length?\n'))
    my_rep = returns.return_reputation(w3, Contract)
    print('\nYour reputation is: ', my_rep, '\n')
    min_rep = int(input('\nWhat is the required minimum reputation to participate (necessarily lower than ' + str(my_rep) + ')?\n'))
    while min_rep > my_rep:
        min_rep = int(input('\nIntroduce a valid reputation(necessarily lower than ' + str(my_rep) + '):\n'))
    balance = returns.return_balance(w3, Contract)
    if balance <= 0:
        print('\nYou have not enough tokens to make a request. Please get tokens before making a request.')
        sys.exit()
    tokens = int(input('\nWhat is the amount of tokens you will pay (necessarily lower than ' + str(balance) + ')?\n'))
    payment = tokens * 10 ** 18
    CA_path = input('\nIntroduce the path where the CA certificate is located (e.g. ../Cert-Store/RootCA.crt)\n')
    CA = upload.upload_file(CA_path, gateway)

    IP, CRT_name, CN = _docker.getPlayerInfo(cname)
    # For test purpose only
    print('\nUploading the following files to IPFS:\n')
    print('\t - Your certificate file.\n')
    print('\t - The preprocessing program.\n')
    print('\t - The information document.\n')
    CRT_path = '../Cert-Store/' + CRT_name
    CRT = upload.upload_file(CRT_path, gateway)
    PREP_path = '../Programs/'+prog+'/'+prog+'.py'
    PREP = upload.upload_file(PREP_path, gateway)
    INFO_path = '../Programs/'+prog+'/'+prog+'.txt'
    INFO = upload.upload_file(INFO_path, gateway)
    print('\nFiles successfully uploaded!\n')

    str_items = [CA, IP, CRT, CN, PREP, INFO]
    print('\nApproving the staking of your tokens:\n\n')
    approve = Token.functions.approve(contractAddress, payment).buildTransaction({
        'chainId': 1, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
    })
    ledger.signTransaction(w3, approve, key)
    print('\n\nPutting your tokens in stake:\n\n')
    tx = Contract.functions.new_request(str_items, data_length, MODL, min_rep, payment).buildTransaction({
        'chainId': 1, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
    })
    ledger.signTransaction(w3, tx, key)

    events_consumer.main(key, w3, Contract, gateway, prog)

def update():
    prog = input('\n\nIntroduce a program name from the above ones: ')
    cname, acct, key = wallet.readAccount()
<<<<<<< HEAD
    gateway='192.168.130.1'
    w3 = ledger.connectBlockchain(acct['address'], gateway)
    l = ledger.getContract(w3)
    Token = ledger.getToken(w3)
    Contract = l[0]
    contractAddress = l[1]
    if returns.return_registered(w3, Contract) == 0:
        x = input('\n\nYou were not registered in the marketplace. Do you want to register? [y/n]')
        if x == 'y':
            reg = Contract.functions.register().buildTransaction({
                'chainId': 1, 'gas': 700000, 'gasPrice': 0,
                'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
            })
            ledger.signTransaction(w3, reg, key)
        else:
            sys.exit()
    last = returns.return_last(w3, Contract)
    l = finder.find_ended_progs(w3,Contract,last,gateway)
    index = int(input("\nChoose the request you want to update from the above ones (enter the index):\n"))
=======
    w3 = ledger.connectBlockchain(acct['address'])
    Contract = ledger.getContract(w3)
    last = returns.return_last(Contract)
    l = finder.find_ended_progs(w3,Contract,last)
    index = int(input("\nChoose the operation you want to update from the above ones (enter the index):\n"))
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
    while index not in l and index != 0:
        index = int(input("Choose a valid option or enter 0 to exit:\n"))
    if index == 0:
        print('CANCELLING UPDATE')
    else:
        MODL = int(input('\nWhat is the required MODL (Minimum Overall Data Length)?\n'))
        data_length = int(input('\nWhat is your data length?\n'))
<<<<<<< HEAD
        my_rep = returns.return_reputation(w3, Contract)
        print('\nYour reputation is: ', my_rep, '\n')
        min_rep = int(input('\nWhat is the required minimum reputation to participate (necessarily lower than ' + str(my_rep) + ')?\n'))
        while min_rep > my_rep:
            min_rep = int(input('\nIntroduce a valid reputation(necessarily lower than ' + str(my_rep) + '):\n'))
        balance = returns.return_balance(w3, Contract)
        if balance <= 0:
            print('\nYou have not enough tokens to make a request. Please get tokens before making a request.')
            sys.exit()
        tokens = int(input('\nWhat is the amount of tokens you will pay (necessarily lower than ' + str(balance) + ')?\n'))
        payment = tokens * 10 ** 18
        CA_path = input('\nIntroduce the path where the CA certificate is located (e.g. ../Cert-Store/RootCA.crt)\n')
        CA = upload.upload_file(CA_path, gateway)
        IP, CRT_name, CN = getPlayerInfo(cname)
=======
        MODL = int(input('What is the required MODL (Minimum Overall Data Length)?\n'))
        CA_path = input('Introduce the path where the CA certificate is located (e.g. ipfs/uploads/test/certs/player0/RootCA.crt)\n')
        CA = upload.upload_file(CA_path)
        IP, CRT_name, CN = _docker.getPlayerInfo(cname)
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
        # For test purpose only
        CRT_path = '../Cert-Store/' + CRT_name
        CRT = upload.upload_file(CRT_path, gateway)

        # At this moment we would register those programs on IPFS and keep the hashes in the following list:

        str_items = [CA, IP, CRT, CN]
        print('\nApproving the staking of your tokens:\n\n')
        approve = Token.functions.approve(contractAddress, payment).buildTransaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
        })
        ledger.signTransaction(w3, approve, key)
        print('\n\nPutting your tokens in stake:\n\n')
        tx = Contract.functions.update_request(index, str_items, data_length, MODL, min_rep, payment).buildTransaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
        })
        ledger.signTransaction(w3, tx, key)
        events_consumer.main(key, w3, Contract, gateway, prog)

<<<<<<< HEAD
def getPlayerInfo(cname):
    # Here we'll have to call another program that will open the crt file and upload its information to the blockchain
    if input('Do you want to configure your player info manually? \n\t1-True\n\t0-False\n') == "1":
        print('\nNow introduce the paths of the following as above:\n')
        IP = input('\n--> IP address: ')
        CRT = input('\n--> Your certificate file name (.crt): ')
        CN = input('\n--> Your Common Name: ')
    else:
        IP = socket.gethostbyname(socket.gethostname())
        CRT = cname + '.crt'
        CN = cname + '@example.com'
    print('Your data is:\n\tIP: ' + IP + '\n\tCRT: ' + CRT + '\n\tCN: ' + CN)
    return IP, CRT, CN
=======
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
