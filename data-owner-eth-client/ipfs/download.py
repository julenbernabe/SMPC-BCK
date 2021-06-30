import ipfshttpclient

def main(location, _hash, gateway):

    # Note on downloading. When downloading items from IPFS, we can download two kinds of items:
        # --> FILES: Only a file is downloaded in the desired location.
        # --> FOLDERS: The entire folder is downloaded, i.e., the folder and all the files inside.
    # The following function does both functionalities, since for downloading an entire folder, we
    # only need that folder's hash.

    client = ipfshttpclient.connect('/ip4/'+gateway+'/tcp/5001/http')
    client.get(_hash, location)
    print('File located in ', location)