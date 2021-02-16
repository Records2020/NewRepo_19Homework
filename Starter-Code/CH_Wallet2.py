{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "uniform-service",
   "metadata": {},
   "outputs": [],
   "source": [
    "#In the below code I'm setting up my wallet. I'm establishing all the required criteria to import my data from, plus setting up the web3 connection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "unnecessary-powell",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'web3'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-0446812f25d5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mbit\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mweb3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mweb3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mWeb3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mdotenv\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mload_dotenv\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'web3'"
     ]
    }
   ],
   "source": [
    "import subprocess\n",
    "import json\n",
    "import bit\n",
    "import web3\n",
    "from web3 import Web3\n",
    "from dotenv import load_dotenv\n",
    "from web3.middleware import geth_poa_middleware\n",
    "from eth_account import Account\n",
    "from bit.network import NetworkAPI\n",
    "import os\n",
    "import constants"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "operating-motorcycle",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'load_dotenv' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-de7b5df4e02c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mload_dotenv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'load_dotenv' is not defined"
     ]
    }
   ],
   "source": [
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "technical-greenhouse",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Web3' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-f912641aa3ed>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Establishing the web3 prorvider route.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mw3\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mWeb3\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mWeb3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mHTTPProvider\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'http://127.0.0.1:8545'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mw3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmiddleware_onion\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minject\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgeth_poa_middleware\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlayer\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Web3' is not defined"
     ]
    }
   ],
   "source": [
    "# Establishing the web3 prorvider route. \n",
    "w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))\n",
    "w3.middleware_onion.inject(geth_poa_middleware, layer=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "atomic-cruise",
   "metadata": {},
   "outputs": [],
   "source": [
    "private_key = os.getenv(\"PRIVATE_KEY\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fourth-benefit",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-dbd28e767d6e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Setting up my mnemonic reference to connect with my environment and wallet for transactions.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mmnemonic\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetenv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"MNEMONIC\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"pig chimney brain stool open sea since increase canoe sand bronze wise\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "# Setting up my mnemonic reference to connect with my environment and wallet for transactions. \n",
    "mnemonic = os.getenv(\"MNEMONIC\", \"pig chimney brain stool open sea since increase canoe sand bronze wise\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "unable-formula",
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_wallets(mnemonic):\n",
    "    output_json = dict()\n",
    "    command = [/Users/hatti/GWU_Bootcamp/19-Blockchain-Python/Homework/hd-wallet-derive.php\", \"-g\", \"--mnemonic='\"+mnemonic+\"'\", \"--cols=path,address,privkey,pubkey\", \"--format=json\", \"--coin=eth\", \"--numberive=3\"]\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n",
    "    stdout, stderr = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    command_out = json.loads(stdout)\n",
    "               \n",
    "    output_json['eth'] = command_out\n",
    "               \n",
    "    command = [/Users/hatti/GWU_Bootcamp/19-Blockchain-Python/Homework/hd-wallet-derive.php\", \"-g\", \"--mnemonic='\"+mnemonic+\"'\", \"--cols=path,address,privkey,pubkey\", \"--format=json\", \"--coin=btc\", \"--numberive=3\"]\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n",
    "    stdout, stderr = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    command_out = json.loads(stdout)\n",
    "               \n",
    "    output_json['btc'] = command_out        \n",
    "        \n",
    "    command = [/Users/hatti/GWU_Bootcamp/19-Blockchain-Python/Homework/hd-wallet-derive.php\", \"-g\", \"--mnemonic='\"+mnemonic+\"'\", \"--cols=path,address,privkey,pubkey\", \"--format=json\", \"--coin=btc-test\", \"--numberive=3\"]\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n",
    "    stdout, stderr = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    command_out = json.loads(stdout)\n",
    "               \n",
    "    output_json['btc-test'] = command_out\n",
    "               \n",
    "    return output_json                         "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "retired-effort",
   "metadata": {},
   "outputs": [],
   "source": [
    "def priv_key_to_account(coin, private_key):\n",
    "    if coin == constant.BTCTEST:\n",
    "        return bit.PrivateKeyTestnet(private_key)\n",
    "    \n",
    "    elif coin == constant.ETH:\n",
    "        return Account.from_key(private_key)\n",
    "\n",
    "def create_tx(coin, account, recipient, amount):\n",
    "    \n",
    "    if coin == constant.BTCTEST:\n",
    "        return account.create_transaction([(str(recipient),amount,'btc')])\n",
    "        #gasEstimate = w3.eth.estimateGas({\"from\": account.address, \"to\": recipient, \"value\": amount}\n",
    "    #)\n",
    "    return {\n",
    "        \"from\": account.address,\n",
    "        \"to\": recipient,\n",
    "        \"value\": amount,\n",
    "        \"gasPrice\": w3.eth.gasPrice,\n",
    "        \"gas\": gasEstimate,\n",
    "        \"nonce\": w3.eth.getTransactionCount(account.address),\n",
    "    }\n",
    "def send_tx(coin, account, recipient, amount):\n",
    "    if coin == constant.BTCTEST:\n",
    "        print(\"BTC token\")\n",
    "    elif coin == constant.ETH:\n",
    "        tx = create_tx('eth', account, recipient, amount)\n",
    "        signed_tx = account.sign_transaction(tx)\n",
    "        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)\n",
    "    elif coin == constant.BTC_TEST:\n",
    "        #print(\"BTC_TEST token\")\n",
    "        tx_hash=create_tx('btc-test',account,recipient,amount)\n",
    "        result=NetworkAPI.broadcast_tx_testnet(tx_hash)\n",
    "        return result\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    coins = derive_wallets(mnemonic)\n",
    "\n",
    "    account=priv_key_to_account('btc-test', '.....')\n",
    "    create_tx('btc-test', account, coins['btc-test'][0]['address'], 0.00008)\n",
    "\n",
    "    output = send_tx('btc-test', account, coins['btc-test'][0]['address'], 0.00008)\n",
    "    print(output)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:Anaconda3]",
   "language": "python",
   "name": "conda-env-Anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
