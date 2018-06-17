#!/usr/bin/env python3
from config import *
from list import segids
import json
import requests
import sys


# accept amount to send as argument
try:
    amount = float(sys.argv[1])
except:
    print("Please, specify an amount to send.")
    quit()

# construct daemon url
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

# iterate addresses list, construct dictionary,
# with amount as value for each address
addresses_dict = {}
for e in segids:
    address = e[-1]
    addresses_dict[address] = amount

# define payload
payload = {
    "jsonrpc": "1.0",
    "id": "python",
    "method": "sendmany",
    "params": ["", addresses_dict]}

#print(json.dumps(payload))

# make rpc call, issue transaction
call_result = post_rpc(rpcurl, payload)
print(json.dumps(call_result))
