from kafka import KafkaConsumer
from src import obtain_output, signup
import json
import os

gateway='192.168.130.1'
consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
cname, acct, key, w3, Contract, index = signup.main(gateway)
print('\n\n################################')
print('')
print('LISTENING TO EVENTS FOR PROGRAM: ', index)
print('')
print('################################')
for message in consumer:
    if message.value['details']['name'] == 'operationThrown':
        if message.value['details']['nonIndexedParameters'][0]['value'] == index:
            print('\n\n################################')
            print('\nOBTAINING OUTPUT FOR PROGRAM:', index,'\n')
            print('################################\n\n')
            my_n=obtain_output.load_data(key, w3, Contract, index, gateway)
            print('\n\n')
        
    if message.value['details']['name'] == 'network_ready':
        if message.value['details']['nonIndexedParameters'][0]['value'] == index:
            # if returns.return_state(w3, contract, message.value['details']['nonIndexedParameters'][0]['value'])[0] == 3: TODO: Update
            print('################################')
            print('')
            print('NETWORK READY FOR PROGRAM:', message.value['details']['nonIndexedParameters'][0]['value'])
            print('')
            print('################################')
            os.system('cd ..; ./Setup.x')
            os.system('cd ..; ./Player.x '+str(my_n)+' Programs/current')
            print('\n')
            print('Finishing the program:\n')
            obtain_output.finished(key, w3, Contract, index)
            break