import socket

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