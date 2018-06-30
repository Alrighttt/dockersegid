#!/bin/bash

PUBKEY=$1
SEGID=$2

USER=RPCUSER
PASSWD=RPCPASS98fjf9ufj9uj9dj3di3jdi3dgsfouoii2oii2oi2oi
SEEDIP=127.0.0.1

docker run -d --rm --name $SEGID -ti \
  --mount "src=$SEGID,dst=/home/komodo/.komodo" \
  komodod \
  -rpcuser=$USER \
  -rpcpassword=$PASSWD \
  -gen \
  -bind=127.0.0.1 \
  -rpcbind=127.0.0.1 \
  -rpcallowip=0.0.0.0/0 \
  -ac_name=STAKETEST \
  -ac_supply=10000000 \
  -ac_staked=90 \
  -ac_reward=1000000000 \
  -addnode=$SEEDIP
