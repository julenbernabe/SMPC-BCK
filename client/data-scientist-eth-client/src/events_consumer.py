from kafka import KafkaConsumer
from src import obtain_output, prepare_execution
from utils import finder, returns
from config import config
import json
import os, sys

def main(key, w3, Contract, index):
    consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
    print('\n\n################################')
    print('')
    print('LISTEN TO EVENTS FOR A CAMPAIGN')
    print('')
    print('################################')
    mpcPath = returns.return_mpcPath(w3, Contract, index)
    print('\n\n################################')
    print('')
    print('LISTENING TO EVENTS FOR CAMPAIGN: ', index)
    print('')
    print('################################')
    for message in consumer:
        if message.value['details']['name'] == 'players_filled':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('MODL REACHED FOR CAMPAIGN:', index)
                print('')
                print('################################')
                prepare_execution.main(key, w3, Contract, index, mpcPath)
                break
    print('Break main')

def bin(key, w3, Contract, campaignIndex, binIndex):
    consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
    print('\n\n################################')
    print('')
    print('LISTENING TO EVENTS FOR CAMPAIGN',  campaignIndex, 'AND BIN', binIndex)
    print('')
    print('################################')
    for message in consumer:
        if message.value['details']['name'] == 'scientist_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == campaignIndex and message.value['details']['status'] == 'UNCONFIRMED':
                print('\n\n################################')
                print('')
                print('OBTAINING EXECUTION DATA FOR CAMPAIGN', campaignIndex, 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'])
                print('')
                print('################################')
                my_n=obtain_output.load_data(key, w3, Contract, campaignIndex)

        if message.value['details']['name'] == 'execution_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == campaignIndex and message.value['details']['status'] == 'UNCONFIRMED':
                print('\n\n################################')
                print('')
                print('NETWORK READY FOR EXECUTION IN CAMPAIGN', message.value['details']['nonIndexedParameters'][0]['value'], 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'])
                print('')
                print('################################')
                success = os.system('cd ' + config.mpc_data_loc + '; ./mascot-party.x ' + str(my_n) + ' -ip ./hosts -OF Player-Data/Output current')
                print('\n')
                print('Finishing the program:\n')
                obtain_output.finished(key, w3, Contract, campaignIndex, success, my_n)
        
        if message.value['details']['name'] == 'execution_successful':
            if message.value['details']['nonIndexedParameters'][0]['value'] == campaignIndex and message.value['details']['status'] == 'UNCONFIRMED':
                # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                print('\n\n################################')
                print('')
                print('EXECUTION FOR CAMPAIGN', message.value['details']['nonIndexedParameters'][0]['value'], 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'], 'ENDED SUCCESSFULLY')
                print('')
                print('################################')
                print('Check result in: "', config.output_file_loc, '". Its current content is: ')
                os.system('cat ' + config.output_file_loc)
                return
        
        if message.value['details']['name'] == 'execution_failed':
            if message.value['details']['nonIndexedParameters'][0]['value'] == campaignIndex and message.value['details']['status'] == 'UNCONFIRMED':
                # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                print('\n\n################################')
                print('')
                print('EXECUTION FOR CAMPAIGN', message.value['details']['nonIndexedParameters'][0]['value'], 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'], 'FAILED')
                print('')
                print('################################')
                return
    print('Break bin')

def other(key, w3, Contract):
    consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
    print('\n\n################################')
    print('')
    print('CHOOSE AMONG EXISTING CAMPAIGNS')
    print('')
    print('################################')
    d = finder.my_progs(w3, Contract)
    index = int(input('\n\nIntroduce the index of the campaign you want to enter: '))
    if d[index] == 1:
        print('\n')
    elif d[index] == 2:
        mpcPath = returns.return_mpcPath(w3, Contract, index)
        prepare_execution.main(key, w3, Contract, index, mpcPath)
    elif d[index] == 3:
        print('\n\n################################')
        print('')
        print('OBTAINING EXECUTION DATA FOR CAMPAIGN:', index)
        print('')
        print('################################')
        my_n = obtain_output.load_data(key, w3, Contract, index)
    elif d[index] == 4:
        print('\n\n################################')
        print('')
        print('NETWORK READY FOR EXECUTION:', index)
        print('')
        print('################################')
        my_n = obtain_output.load_data(key, w3, Contract, index)
        success = os.system('cd ' + config.mpc_data_loc + '; ./mascot-party.x ' + str(my_n) + ' -ip ./hosts -OF Player-Data/Output current')
        print('\n')
        print('Finishing the program:\n')
        obtain_output.finished(key, w3, Contract, index, success, my_n)
    print('\n\n################################')
    print('')
    print('LISTENING TO EVENTS FOR CAMPAIGN: ', index)
    print('')
    print('################################')
    for message in consumer:
        if message.value['details']['name'] == 'players_filled':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('MODL REACHED FOR CAMPAIGN:', index)
                print('')
                print('################################')
                mpcPath = returns.return_mpcPath(w3, Contract, index)
                prepare_execution.main(key, w3, Contract, index, mpcPath)
    
        if message.value['details']['name'] == 'scientist_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('OBTAINING EXECUTION DATA FOR CAMPAIGN:', index)
                print('')
                print('################################')
                my_n = obtain_output.load_data(key, w3, Contract, index)

        if message.value['details']['name'] == 'execution_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('NETWORK READY FOR EXECUTION:', message.value['details']['nonIndexedParameters'][0]['value'])
                print('')
                print('################################')
                success = os.system('cd ' + config.mpc_data_loc + '; ./mascot-party.x '+ str(my_n) + ' -ip ./hosts -OF Player-Data/Output current')
                print('\n')
                print('Finishing the program:\n')
                obtain_output.finished(key, w3, Contract, index, success, my_n)
        
        if message.value['details']['name'] == 'execution_successful':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                print('\n\n################################')
                print('')
                print('CAMPAIGN ', message.value['details']['nonIndexedParameters'][0]['value'], ' ENDED SUCCESSFULLY')
                print('')
                print('################################')
                print('Check result in: "', config.output_file_loc, '". Its current content is: ')
                os.system('cat ' + config.output_file_loc)
                break
        
        if message.value['details']['name'] == 'execution_failed':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                print('\n\n################################')
                print('')
                print('CAMPAIGN ', message.value['details']['nonIndexedParameters'][0]['value'], ' FAILED')
                print('')
                print('################################')
                break
    print('Break other')