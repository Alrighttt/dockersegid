#!/bin/bash
touch ~/.komodo/komodo.conf
chown komodo:komodo ~/.komodo/komodo.conf

/komodo/src/komodod "$@" 
