import ipfshttpclient
from config import config

def main(location, _hash):

    # Note on downloading. When downloading items from IPFS, we can download two kinds of items:
        # --> FILES: Only a file is downloaded in the desired location.
        # --> FOLDERS: The entire folder is downloaded, i.e., the folder and all the files inside.
    # The following function does both functionalities, since for downloading an entire folder, we
    # only need that folder's hash.

    client = ipfshttpclient.connect(config.ipfs_gateway)
    client.get(_hash, location)