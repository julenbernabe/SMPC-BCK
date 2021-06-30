#!/usr/bin/env python

from web3 import Web3
import json

contractAddress = '0x3Ff035c4d94Bf59FdDeB779e7cC7deFB71f9F639'

### Web3 functions
def connectBlockchain(sender, gateway):
    # w3 keeps the blockchain information from the config.py file (it is currently entering in the local endpoint)
    w3 = Web3(Web3.HTTPProvider('http://'+gateway+':9545'))
    # Here we check if the blockchain connection es working
    print('Checking blockchain connection...', w3.isConnected())
    # Set my account as default account
    w3.eth.defaultAccount = w3.toChecksumAddress(sender)
    # Once we finish this setup process, this function returns all the blockchain information
    return w3

def getContract(w3):
    # For this function, we'll need the blockchain information (this is important for the moment when we write the client script)

    # We now open the json file from the build directory. This file contains all the info about the contract (in this case the subscribe contract)
    # and the functions defined in it
    with open('config/subscribe.json') as json_file:
        # In data we load the json file in json format for python to be readable
        data = json.load(json_file)
        # In the variable abi we save the ABI code
        abi = data['abi']
        # The previous instructions will be useful for us in order to load the contract and return it in the following commands
        Contract = w3.eth.contract(abi=abi, address=w3.toChecksumAddress(contractAddress))       # Note that we have called config to
                                                                                                        # obtain the contract address
    return Contract

def signTransaction(w3, tx, key):
    # This function will sign the transactions we want to do in the future. For this purpose, it will need the transaction hash (a string) 
    # and the blockchain information again.
    print("tx:", tx)
    # We now sign the transaction with the following command. Recall that we are using both of the inputs given to this function, and the private key
    signed_tx = w3.eth.account.signTransaction(tx, private_key=key)
    print("signed_tx:", signed_tx)
    w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    # We finally compute the transaction receipt from the signed transaction's hash.
    tx_receipt = w3.eth.waitForTransactionReceipt(signed_tx.hash)
    print("\ntx_receipt:", tx_receipt)
    return tx_receipt
