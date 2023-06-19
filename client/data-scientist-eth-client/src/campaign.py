#!/usr/bin/env python3
import socket
from src import events_consumer
from utils import ledger, wallet, finder, returns, balance
from ipfs import upload
from config import config
import sys, os

def new():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    l = ledger.getContract(w3)
    Token = ledger.getToken(w3)
    Contract = l[0]
    contractAddress = l[1]
    if returns.return_registered(w3, Contract) == 0:
        x = input('\n\nYou were not registered in the marketplace. Do you want to register? [y/n]')
        if x == 'y':
            reg = Contract.functions.register().build_transaction({
                'chainId': 1, 'gas': 700000, 'gasPrice': 0,
                'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
            })
            ledger.sign_transaction(w3, reg, key)
        else:
            sys.exit()
    programs = os.listdir(config.programs_loc)
    print('\n')
    i = 0
    while i < len(programs):
        if programs[i].find('-0') != -1:
            print('Please rename program: ', programs[i])
            programs.pop(i)
        else:
            i += 1
    print('\n\n###################################\n\nPOSIBLE PROGRAMS TO RUN:\n')
    for program in programs:
        print('\t--> ' + program)
    print('\n\n###################################\n\n')
    prog = input('Introduce a program from the above ones: ')
    while prog not in programs:
        prog = input('\nProgram "' + prog + '" is not in the list of programs above. Please enter a valid program: ')
    mpcPath = config.programs_loc + prog + '/' + prog + '.mpc'
    MODL = int(input('\nWhat is the required MODL (Minimum Overall Data Length)?\n'))
    data_length = int(input('\nWhat is your data length?\n'))
    my_rep = returns.return_reputation(w3, Contract)
    print('\nYour reputation is: ', my_rep, '\n')
    min_rep = int(input('\nWhat is the required minimum reputation to participate? (necessarily lower than ' + str(my_rep) + ')\n'))
    while min_rep > my_rep:
        min_rep = int(input('\nIntroduce a valid reputation (necessarily lower than ' + str(my_rep) + '):\n'))
    if returns.return_balance(w3, Contract) <= 0:
        print('\nYou have not enough tokens to make a request. Withdrawing tokens...')
        balance.increase(50)
        print('\nYou now have tokens...')
    tokens = int(input('\nWhat is the amount of tokens you will pay? (necessarily lower than ' + str(returns.return_balance(w3, Contract)) + ')\n'))
    payment = tokens * 10 ** 18
    CA = upload.upload_file(config.CA_file_loc)

    # For test purpose only
    print('\nUploading the following files to IPFS:\n')
    print('\t - Your certificate file.\n')
    print('\t - The preprocessing program.\n')
    print('\t - The information document.\n')
    CRT = upload.upload_file(config.cert_file_loc)
    PREP = upload.upload_file(config.programs_loc + prog + '/' + prog + '.py')
    INFO = upload.upload_file(config.programs_loc + prog + '/' + prog + '.txt')
    print('\nFiles successfully uploaded!\n')

    str_items = [CA, config.IP, CRT, config.common_name, PREP, INFO, mpcPath]
    print('\nApproving the staking of your tokens:\n\n')
    approve = Token.functions.approve(contractAddress, payment).build_transaction({
        'chainId': 5777, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
    })
    ledger.sign_transaction(w3, approve, key)
    print('\n\nCreating campaign:\n\n')
    tx = Contract.functions.newCampaign(str_items, data_length, MODL, min_rep, payment).build_transaction({
        'chainId': 5777, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
    })
    ledger.sign_transaction(w3, tx, key)
    last = returns.return_last(w3, Contract)
    events_consumer.main(key, w3, Contract, last)

def reuse():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    l = ledger.getContract(w3)
    Token = ledger.getToken(w3)
    Contract = l[0]
    contractAddress = l[1]
    if returns.return_registered(w3, Contract) == 0:
        x = input('\n\nYou were not registered in the marketplace. Do you want to register? [y/n]')
        if x == 'y':
            reg = Contract.functions.register().build_transaction({
                'chainId': 1, 'gas': 700000, 'gasPrice': 0,
                'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
            })
            ledger.sign_transaction(w3, reg, key)
        else:
            sys.exit()
    l = finder.find_ended_progs(w3, Contract)
    if len(l) == 0:
        print('\nOops! There are no finished programs right now.\n')
        sys.exit()
    index = int(input("\nChoose the request you want to reuse from the above ones (enter the index):\n"))
    while index not in l and index != 0:
        index = int(input("Choose a valid option or enter 0 to exit:\n"))
    if index == 0:
        print('CANCELLING')
    else:
        print('You will reuse the campaign where the executed program is in:', returns.return_mpcPath(w3, Contract, index))
        MODL = returns.return_MODL(w3, Contract, index)
        data_length = returns.return_dataLength(w3, Contract, index, 0)
        min_rep = returns.return_minimum_reputation(w3, Contract, index)
        payment = int(returns.return_payment(w3, Contract, index))
        updatePayment = True
        updateReputation = True
        print('\nCampaign', index, 'was executed with:')
        print('\t--> MODL:', MODL)
        print('\t--> Your data length:', data_length)
        if payment < returns.return_balance(w3, Contract):
            print('\t--> Payment:', payment)
            updatePayment = False
        if min_rep < returns.return_reputation(w3, Contract):
            print('\t--> Minimum reputation:', min_rep)
            updateReputation = False
        x = input('\nDo you want to reuse the values above? [y/n]')
        if x == 'y' and updatePayment:
            if returns.return_balance(w3, Contract) <= 0:
                print('\nYou have not enough tokens to make a request. Withdrawing tokens...')
                balance.increase(50)
                print('\nYou now have tokens...')
            payment = int(input('\nWhat is the amount of tokens you will pay? (necessarily lower than ' + str(returns.return_balance(w3, Contract)) + ')\n'))
            while payment > returns.return_balance(w3, Contract):
                payment = int(input('\nIntroduce a valid payment (necessarily lower than ' + str(returns.return_balance(w3, Contract)) + '):\n'))
        elif x == 'y' and updateReputation:
            min_rep = int(input('\nWhat is the required minimum reputation to participate? (necessarily lower than ' + str(returns.return_reputation(w3, Contract)) + ')\n'))
            while min_rep > returns.return_reputation(w3, Contract):
                min_rep = int(input('\nIntroduce a valid reputation (necessarily lower than ' + str(returns.return_reputation(w3, Contract)) + '):\n'))
        elif x == 'n':
            MODL = int(input('\nWhat is the required MODL (Minimum Overall Data Length)?\n'))
            data_length = int(input('\nWhat is your data length?\n'))
            my_rep = returns.return_reputation(w3, Contract)
            print('\nYour reputation is: ', my_rep, '\n')
            min_rep = int(input('\nWhat is the required minimum reputation to participate? (necessarily lower than ' + str(my_rep) + ')\n'))
            while min_rep > my_rep:
                min_rep = int(input('\nIntroduce a valid reputation (necessarily lower than ' + str(my_rep) + '):\n'))
            balance = returns.return_balance(w3, Contract)
            if returns.return_balance(w3, Contract) <= 0:
                print('\nYou have not enough tokens to make a request. Withdrawing tokens...')
                balance.increase(50)
                print('\nYou now have tokens...')
            payment = int(input('\nWhat is the amount of tokens you will pay (necessarily lower than ' + str(balance) + ')?\n'))
            while payment > returns.return_balance(w3, Contract):
                payment = int(input('\nIntroduce a valid payment (necessarily lower than ' + str(returns.return_balance(w3, Contract)) + '):\n'))
        

        payment = payment * 10 ** 18
        
        CA = upload.upload_file(config.CA_file_loc)
        CRT = upload.upload_file(config.cert_file_loc)

        # At this moment we would register those programs on IPFS and keep the hashes in the following list:

        str_items = [CA, config.IP, CRT, config.common_name]
        print('\nApproving the staking of your tokens:\n\n')
        approve = Token.functions.approve(contractAddress, payment).build_transaction({
            'chainId': 5777, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
        })
        ledger.sign_transaction(w3, approve, key)
        print('Payment', payment)
        print('\n\nPutting your tokens in stake:\n\n')
        tx = Contract.functions.updateCampaign(index, str_items, data_length, MODL, min_rep, payment).build_transaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount)
        })
        ledger.sign_transaction(w3, tx, key)
        events_consumer.main(key, w3, Contract, index)

def working():
    cname, acct, key = wallet.readAccount()
    w3 = ledger.connectBlockchain(acct['address'])
    l = ledger.getContract(w3)
    Contract = l[0]
    events_consumer.other(key, w3, Contract)

# def getPlayerInfo(cname):
#     # Here we'll have to call another program that will open the crt file and upload its information to the blockchain
#     if input('Do you want to configure your player info manually? \n\t1-True\n\t0-False\n') == "1":
#         print('\nNow introduce the paths of the following as above:\n')
#         IP = input('\n--> IP address: ')
#         CRT = input('\n--> Your certificate file name (.crt): ')
#         CN = input('\n--> Your Common Name: ')
#     else:
#         IP = socket.gethostbyname(socket.gethostname())
#         CRT = cname + '.crt'
#         CN = cname + '@example.com'
#     print('Your data is:\n\tIP: ' + IP + '\n\tCRT: ' + CRT + '\n\tCN: ' + CN)
#     return IP, CRT, CN
