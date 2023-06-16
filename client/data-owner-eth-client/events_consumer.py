from kafka import KafkaConsumer
from src import obtain_output, signup
from utils import returns
from config import config
import json
import os

consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
cname, acct, key, w3, Contract, index = signup.main()
if index != 0:
    print('\n\n################################')
    print('')
    print('LISTENING TO EVENTS FOR CAMPAIGN: ', index)
    print('')
    print('################################')
    for message in consumer:
        if message.value['details']['name'] == 'scientist_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index and returns.elected(w3, Contract, index) == 1:
                print('\n\n################################')
                print('')
                print('OBTAINING EXECUTION DATA FOR CAMPAIGN', index,'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'])
                print('')
                print('################################\n\n')
                my_n=obtain_output.load_data(key, w3, Contract, index)
                print('\n\n')
        
        if message.value['details']['name'] == 'execution_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index and returns.elected(w3, Contract, index) == 2:
                # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                print('\n\n################################')
                print('')
                print('NETWORK READY FOR EXECUTION IN CAMPAIGN', message.value['details']['nonIndexedParameters'][0]['value'], 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'])
                print('')
                print('################################')
                success = os.system('cd ' + config.mpc_data_loc + '; ./mascot-party.x ' + str(my_n)+' -ip ./hosts -OF Player-Data/Output current')
                print('Success', success)
                print('\n')
                print('Finishing the program:\n')
                obtain_output.finished(key, w3, Contract, index, success, my_n)
        
        if message.value['details']['name'] == 'execution_successful':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                if returns.elected(w3, Contract, index) == 4:
                    # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                    print('\n\n################################')
                    print('')
                    print('EXECUTION FOR CAMPAIGN', message.value['details']['nonIndexedParameters'][0]['value'], 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'], 'ENDED SUCCESSFULLY')
                    print('')
                    print('Check result in: "', config.output_file_loc, '". Its current content is: ')
                    os.system('cat ' + config.output_file_loc)
                    print('################################')
                    break
        
        if message.value['details']['name'] == 'execution_failed':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                if returns.elected(w3, Contract, index) == 4:
                    # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
                    print('\n\n################################')
                    print('')
                    print('EXECUTION FOR CAMPAIGN', message.value['details']['nonIndexedParameters'][0]['value'], 'AND BIN', message.value['details']['nonIndexedParameters'][1]['value'], 'FAILED')
                    print('')
                    print('################################')
                    break