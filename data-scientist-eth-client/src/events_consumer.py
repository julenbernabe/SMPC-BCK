from kafka import KafkaConsumer
from src import obtain_output, throw_operation
from utils import finder
import json
import os, sys

def main(key, w3, Contract, gateway, prog):
    consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
    print('\n\n################################')
    print('')
    print('LISTEN TO EVENTS FOR A PROGRAM')
    print('')
    print('################################')
    finder.my_progs(w3, Contract)
    index = int(input('\n\nIntroduce the index of the program you want to follow: '))
    print('\n\n################################')
    print('')
    print('LISTENING TO EVENTS FOR PROGRAM: ', index)
    print('')
    print('################################')
    for message in consumer:
        if message.value['details']['name'] == 'playersFilled':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('MODL REACHED FOR PROGRAM:', index)
                print('')
                print('################################')
                throw_operation.main(key, w3, Contract, index, gateway, prog)
    
        if message.value['details']['name'] == 'operationThrown':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('OBTAINING OUTPUT FOR PROGRAM:', index)
                print('')
                print('################################')
                obtain_output.load_data(key, w3, Contract, index, gateway)

        if message.value['details']['name'] == 'network_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('NETWORK READY FOR PROGRAM:', message.value['details']['nonIndexedParameters'][0]['value'])
                print('')
                print('################################')
                os.system('cd ..; ./Setup.x')
                os.system('cd ..; ./Player.x 0 Programs/current')
                print('\n')
                print('Finishing the program:\n')
                obtain_output.finished(key, w3, Contract, index)
                break

def other(key, w3, Contract, gateway, prog):
    consumer = KafkaConsumer('contract-events', bootstrap_servers='kafka:19092', value_deserializer=lambda m: json.loads(m.decode('ascii')))
    print('\n\n################################')
    print('')
    print('CHOOSE AMONG YOUR REQUESTS')
    print('')
    print('################################')
    d = finder.my_progs(w3, Contract)
    index = int(input('\n\nIntroduce the index of the program you want to follow: '))
    if d[index] == 1:
        print('\n')
    elif d[index] == 2:
        throw_operation.main(key, w3, Contract, index, gateway, prog)
    elif d[index] == 3:
        print('\n\n################################')
        print('')
        print('OBTAINING OUTPUT FOR PROGRAM:', index)
        print('')
        print('################################')
        obtain_output.load_data(key, w3, Contract, index, gateway)
    elif d[index] == 4:
        print('\n\n################################')
        print('')
        print('NETWORK READY FOR PROGRAM:', index)
        print('')
        print('################################')
        os.system('cd ..; ./Setup.x')
        os.system('cd ..; ./Player.x 0 Programs/current')
        print('\n')
        print('Finishing the program:\n')
        obtain_output.finished(key, w3, Contract, index)
        sys.exit()
    print('\n\n################################')
    print('')
    print('LISTENING TO EVENTS FOR PROGRAM: ', index)
    print('')
    print('################################')
    for message in consumer:
        if message.value['details']['name'] == 'playersFilled':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('MODL REACHED FOR PROGRAM:', index)
                print('')
                print('################################')
                throw_operation.main(key, w3, Contract, index, gateway, prog)
    
        if message.value['details']['name'] == 'operationThrown':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('OBTAINING OUTPUT FOR PROGRAM:', index)
                print('')
                print('################################')
                obtain_output.load_data(key, w3, Contract, index, gateway)

        if message.value['details']['name'] == 'network_ready':
            if message.value['details']['nonIndexedParameters'][0]['value'] == index:
                print('\n\n################################')
                print('')
                print('NETWORK READY FOR PROGRAM:', message.value['details']['nonIndexedParameters'][0]['value'])
                print('')
                print('################################')
                os.system('cd ..; ./Setup.x')
                os.system('cd ..; ./Player.x 0 Programs/current')
                print('\n')
                print('Finishing the program:\n')
                obtain_output.finished(key, w3, Contract, index)
                break