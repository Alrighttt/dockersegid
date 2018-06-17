#!/usr/bin/env python3
import json
import requests
from config import *

rpcurl = (
    'http://' +
    rpcuser +
    ':' +
    rpcpassword +
    '@' +
    rpcip +
    ':' +
    rpcport)


# define function that posts json data
def post_rpc(url, payload, auth=None):
    try:
        r = requests.post(url, data=json.dumps(payload), auth=auth)
        return(json.loads(r.text))
    except Exception as e:
        raise Exception("Couldn't connect to " + url + ": ", e)


# generate address, validate address, dump private key
def genvaldump():
    # get new address
    payload = {"method": "getnewaddress"}
    getnewaddress_result = post_rpc(rpcurl, payload)
    address = getnewaddress_result['result']
    # validate address
    payload = {
        "method": "validateaddress",
        "params": [address]}
    validateaddress_result = post_rpc(rpcurl, payload)
    segid = validateaddress_result['result']['segid']
    pubkey = validateaddress_result['result']['pubkey']
    address = validateaddress_result['result']['address']
    # dump private key for the address
    payload = {
        "method": "dumpprivkey",
        "params": [address]
    }
    dumpprivkey_result = post_rpc(rpcurl, payload)
    privkey = dumpprivkey_result['result']
    # function output
    output = [segid, pubkey, privkey, address]
    return(output)


# fill a list of sigids with matching segid address data
segids = {}
while len(segids.keys()) < 64:
    genvaldump_result = genvaldump()
    segid = genvaldump_result[0]
    if segid in segids:
        pass
    else:
        segids[segid] = genvaldump_result

# convert dictionary to array
segids_array = []
for position in range(64):
    segids_array.append(segids[position])

# print output
print("segids = " + str(json.dumps(segids_array)))
