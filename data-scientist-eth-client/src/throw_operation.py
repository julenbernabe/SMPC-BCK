<<<<<<< HEAD
#!/usr/bin/env python3
=======
#!/usr/bin/env python
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a
from utils import ledger, returns
from ipfs import upload
import os



<<<<<<< HEAD
def main(key, w3, Contract, index, gateway, prog):
    selected_players = returns.return_Playerdata_private(w3,Contract,index)
    
    # FALTA SACAR LAS LENGTHS DE CADA PLAYER, PARA PODER TENERLO EN CUENTA AL EDITAR EL MPC
    
    print('\n\n##############################################################################################################################################################################################################\n\n')
    print('\n\t\t\t\t\t\t\t\t\t\t\tCHANGE YOUR MPC FILE\n\n')
    print('\n\t\t\t\t\t\t\t\tYour file is in: /root/SCALE-MAMBA/Programs/'+prog+'/'+prog+'.mpc')
    print('\n\t\t\t\t\t\t\t\tThe list of players for this bin is:\n')
    count = 0
    addresses = []
    for elem in selected_players:
        count += elem[1]
        addresses.append(elem[0])
        print('\n\t\t\t\t\t\t\t\t --> Account: ', elem[0], '\t\t Dataset size: ', elem[1])
    print('\n\n\t\t\t\t\t\t\t\tTotal number of players: ', len(selected_players))
    print('\n\t\t\t\t\t\t\t\tChange it according to the above list. Do not continue this program until changed.')
    print('\n\n##############################################################################################################################################################################################################')
    cont = int(input('\n\nEnter 0 when you are ready to continue: '))
    if cont == 0:
        prime = int(input('\nChoose the prime that will be used in the operations (among 340282366920938463463374607431768211507 , 170141183460469231731687303715884105727 , 393050634124102232869567034555427371542904833):\n'))
        os.system('cd ..; ./compile.sh Programs/'+prog+' '+str(prime))
        bc_path = '../Programs/'+prog+'/'+prog+'-0.bc'
        sch_path = '../Programs/'+prog+'/'+prog+'.sch'
        bc_hash = upload.upload_file(bc_path, gateway)
        sch_hash = upload.upload_file(sch_path, gateway)
        actual_payment = int(compute_payment(returns.return_payment(w3, Contract, index), count) * 10 ** 18)
        tx = Contract.functions.throw_operation(prime, addresses, bc_hash, sch_hash, index, actual_payment).buildTransaction({
            'chainId': 1, 'gas': 700000, 'gasPrice': 0,
            'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
        })
        ledger.signTransaction(w3, tx, key)
    else:
        'Exiting...'

def compute_payment(total, divisor):
    return total / divisor
=======
def main(key, w3, Contract, index):
    prime = int(input('\nChoose the prime that will be used in the operations (among 340282366920938463463374607431768211507 , 170141183460469231731687303715884105727 , 393050634124102232869567034555427371542904833):\n'))
    bc_path = input('Introduce the path to the .bc file (e.g. ipfs/uploads/test/programs/test.bc): ')
    sch_path = input('Introduce the path to the .sch file (e.g. ipfs/uploads/test/programs/test.sch): ')
    bc_hash = upload.upload_file(bc_path)
    sch_hash = upload.upload_file(sch_path)
    selected_players = returns.return_Playerdata_private(Contract,index)
    tx = Contract.functions.throw_operation(prime, selected_players, bc_hash, sch_hash, index).buildTransaction({
        'chainId': 1, 'gas': 700000, 'gasPrice': 0,
        'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount)
    })
    ledger.signTransaction(w3, tx, key)
>>>>>>> 8e75041ea709eb3c9b268fdd46ec18cd413b0d0a


