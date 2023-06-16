import ipfshttpclient
from config import config

def upload_file(location):
    client = ipfshttpclient.connect(config.ipfs_gateway)
    result = client.add(location)
    _hash = result['Hash']
    #print('The resulting hash of your file is: ', _hash, '\n')
    return(_hash)