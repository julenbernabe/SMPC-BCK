import ipfshttpclient

def upload_file(location, gateway):
    client = ipfshttpclient.connect('/ip4/'+gateway+'/tcp/5001/http')
    result = client.add(location)
    _hash = result['Hash']
    #print('The resulting hash of your file is: ', _hash, '\n')
    return(_hash)