After creating a staking chain, it is vital to distribute staking coins across all 64 segids. If there is not at least one UTXO staking in each segid, this may give someone the ability to 51% attack the chain. This can be done easily using this repo{LINK TO DOCKER REPO}. 

 

Prequisites:
Docker/Docker CE installed https://docs.docker.com/install/linux/docker-ce/ubuntu/

This tutorial assumes you have already created a Proof of Stake chain, and you have a node running on the computer you're using. PLease see {LINK TO ASSET CHAIN TUT} if you have not. 

The script used to generate the addresses will require the use of `komodo-cli` command. If you haven't already created a symblink to `/usr/local/bin/`
`sudo ln -sf /home/$USER/komodo/src/komodo-cli /usr/local/bin/komodo-cli`
`sudo ln -sf /home/$USER/komodo/src/komodod /usr/local/bin/komodod`


Clone the repo `https://github.com/alrighttt/dockersegid

`sudo ln -sf /home/$USER/komodo/src/komodo-cli /usr/local/bin/komodo-cli`
`sudo ln -sf /home/$USER/komodo/src/komodod /usr/local/bin/komodod`

If you currently have a wallet.dat file in `~/.komodo/<CHAINNAME>` change the name of it to something for now and restart the daemon. Running the `./generateaddresses` script will generate up to a couple hundred addresses, and should not be done on a wallet.dat you plan to continually use. 

Ensure that your node is running with a wallet.dat with no important addresses imported to it. Edit the `generateaddresses.sh` script's config zone to reflect the values found in `~/.komodo/<CHAINNAME>/<CHAINNAME>.conf`. It's recommended to run this script on the same computer as the node is running. If for some reason you would like to do it from a different computer, ensure that the RPC port is open on the node's computer and set the `rpcip` value in the script to node's IP. 

Run the `./generateaddresses.sh` script. Check that it generated the file `list.py` properly. This file is the basis for most of the scripts, and it's vital that it is the correct format. This file is an array including an address with corresponding pubkey/privkey for each segid in the format `[segid, pubkey, privkey, address]` . THIS FILE CONTAINS THE PRIVATE KEYS FOR EACH ADDRESS. KEEP IT SAFE. 

double check that it generated `addresslist` properly. This will be a file with 64 addresses, one for each segid. 

edit `startdocker` script. 
Change the RPCUSER, RPCPASS and seednode values along with the ac_params for the chain. RPCUSER can be anything. RPCPASS should be a long random password. The seednode value should be the IP of a node you would like the docker containers to connect to.

Edit the `kmdcli` script to reflect the same rpcuser and rpcpass values in `startdocker` script

Run `sudo ./launchcontainers` Wait for each to launch 

Run `sudo ./importprivkey` This will import the private key for each corresponding pubkey.

On the node you will fund the staking daemons from, run the `./fund64 script

You can check that each node received these coins by running `sudo ./kmdall "getbalance"

Once you have confirmed that each node has received coins, do `sudo ./kmdall "setgenerate true 1"

As soon as the coins are eligible to stake all 64 nodes will begin to stake.
