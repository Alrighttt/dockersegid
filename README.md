After creating a staking chain, it is vital to distribute staking coins across all 64 segids. If there is not at least one UTXO staking in each segid, this may give someone the ability to 51% attack the chain. This can be done easily using this repo.

 

## Dependencies/Prerequisites :
Docker/Docker CE installed https://docs.docker.com/install/linux/docker-ce/ubuntu/

python3 installed `sudo apt-get python3`

python3 requests installed `pip install requests`

Komodod installed and running. This tutorial assumes you have already created a Proof of Stake chain, and you have a node running on the computer you're using. Please see [this tutorial](https://komodo-platform.readthedocs.io/en/latest/komodo/create-Komodo-Assetchain.html) if you have not already.

## Tutorial

The first step is to create the docker image. Run 
```shell
git clone https://github.com/alrighttt/dockersegid
cd dockersegid
sudo docker build -t komodod .
``` 

Edit the `config.py` file to the appropriate RPC settings for the node you will be generating the addresses from. You will also be funding all 64 segid addresses from this node, so it must have a balance. The RPC settings can be found in `~/.komodod/<CHAINNAME>/<CHAINNAME>.conf`. The IP should not be changed unless you are running the node from a separate computer. If you are running the node on a separate computer, ensure that the RPC port is open. 

Edit the `dockerstart.sh` file. Set PASSWD to a long string of random characters. Set SEEDIP to the IP of the node the docker nodes will connect to. The node the docker nodes will connect to must have its p2p port open. Edit the `ac_parameters` to match the parameters of your chain. Make sure you have every `ac_parameter` you would use to start a typical node on your chain. For example the default setting for this repo is for this chain `./komodod -ac_name=STAKETEST -ac_supply=10000000 -ac_reward=1000000000 -ac_staked=90`

Edit the `kmdcli` script. Change `-rpcpassword` value to the same value as `PASSWD` set in `dockerstart.sh`.

Stop your node's daemon. 
```shell
cd ~/komodo/src
./komodo-cli -ac_name=<CHAINNAME> stop
```
Rename the `wallet.dat` found in the `~/.komodo/<CHAINNAME>/` directory. Running the `./generateaddresses` script will generate up to a couple hundred addresses and should not be done on a wallet.dat you plan to continually use. Restart the node and ensure that it is running with a newly created wallet.dat. 

Run 
```shell
cd ~/dockersegid
./generateaddresses.py > list.py
```
Check that it generated the file `list.py` properly. This file is the basis for the scripts, and it's vital that it is the correct format. This file is an array including an address with corresponding pubkey/privkey for each segid in the format `[segid, pubkey, privkey, address]` . 
**THIS FILE CONTAINS THE PRIVATE KEYS FOR EACH ADDRESS. KEEP IT SAFE.**

Run `./launchcontainers` Wait for each to launch.

Run `./importprivkey` This will import the private key to each docker container's node.

Run `./sendmany64 100`. This will send 100 coins to each docker node's komodod. Change `100` to how ever many coins you would like each docker container to stake. 

You can check that each node received these coins by running `./kmdcliall "getbalance"`. This `kmdall` script can be used to send any komodod-cli commands to all 64 nodes at once. To send a command to a specific node, use the `./kmdcli`. For example to send a getbalance command to the segid40 node, you would use `./kmdcli 40 "getbalance"` 

Once you have confirmed that each node has received coins, run `./kmdall "setgenerate true 1"`

As soon as the coins are eligible to stake all 64 nodes will begin to stake.
