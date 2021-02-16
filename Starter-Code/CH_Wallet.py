{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "posted-cabin",
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "educational-operations",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'bit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-718d82288edf>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mbit\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mWeb3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mweb3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mWeb3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mdotenv\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mload_dotenv\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mweb3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmiddleware\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mgeth_poa_middleware\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'bit'"
     ]
    }
   ],
   "source": [
    "import bit\n",
    "import Web3\n",
    "from web3 import Web3\n",
    "from dotenv import load_dotenv\n",
    "from web3.middleware import geth_poa_middleware"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bacterial-album",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-8c24b7af0207>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-8c24b7af0207>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    from Users/hatti/GWU_Bootcamp/19-Blockchain-Python/Homework/Instructions import os\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "from Users/hatti/GWU_Bootcamp/19-Blockchain-Python/Homework/Instructions import os\n",
    "import constant "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aquatic-summit",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'w3' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-0bd78e373cf1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mw3\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mWeb3\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mWeb3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mHTTPProvider\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"http://127.0.0.1:8545\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mw3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmiddleware_onion\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minject\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgeth_poa_middleware\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlayer\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'w3' is not defined"
     ]
    }
   ],
   "source": [
    "w3 == Web3(Web3.HTTPProvider(\"http://127.0.0.1:8545\"))\n",
    "w3.middleware_onion.inject(geth_poa_middleware, layer=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "coated-category",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-36d45de40d8d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmnemonic\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetenv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mMNEMONIC\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;34m\"pig chinmey brain stool open sea since increase canoe sand bronze wise\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "mnemonic = os.getenv(MNEMONIC =\"pig chinmey brain stool open sea since increase canoe sand bronze wise\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "velvet-vaccine",
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_wallets(mnemonic):\n",
    "    output_json = dict()\n",
    "    command = './derive -g --mnemonic=\"pig chinmey brain stool open sea since increase canoe sand bronze wise\" --cols=path,address,privkey,pubkey --format=json'\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprodcess.PIPE)\n",
    "    output, err = p.communicate()\n",
    "    stdout, stderr = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    command_out = json.loads(stdout)\n",
    "    \n",
    "    output_json['eth'] = command_out\n",
    "    \n",
    "    command = './derive -g --mnemonic=\"pig chinmey brain stool open sea since increase canoe sand bronze wise\" --cols=path,address,privkey,pubkey --format=json'\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n",
    "    output, err = p.communicate()\n",
    "    stdout, stderr = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    command_out = json.loads(stdout)\n",
    "    \n",
    "    output_json['btc'] = command_out\n",
    "    \n",
    "    command = './derive -g --mnemonic=\"pig chinmey brain stool open sea since increase canoe sand bronze wise\" --cols=path,address,privkey,pubkey --format=json'\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n",
    "    output, err = p.communicate()\n",
    "    stdout, stderr = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    command_out = json.loads(stdout)\n",
    "    \n",
    "    output_json['btc_test'] = command_out\n",
    "    \n",
    "    return output_json\n",
    "\n",
    "def priv_key_to_account(privkey, coin):\n",
    "    if coint == constant.BTCTEST:\n",
    "        return bit.PrivateKeyTestnet(privkey)\n",
    "    \n",
    "    elif coint == contant.ETH:\n",
    "        return web3.eth.accounts.privateKeyToAccount(privkey)\n",
    "    \n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "occasional-ireland",
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_tx(account, recipient, amount):\n",
    "    gasEstimate = w3.eth.estmiateGas(\n",
    "        {\"from\": account.address, \"to\": recipient, \"value\": amount}\n",
    "        )\n",
    "    return {\n",
    "        \"from\": account.address,\n",
    "        \"to\": recipient,\n",
    "        \"value\": amount, \n",
    "        \"gasPrice\": w3.eth.gasPrice, \n",
    "        \"gas\": gasEstimate,\n",
    "        \"nonce\": w3.eth.getTransactionCount(account.address).\n",
    "    }\n",
    "def send_txt(account, recipeint, amount):\n",
    "    tx = create_raw_tx(account, recipient, amount)\n",
    "    signed_tx = account.sign_transaction(tx)\n",
    "    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)\n",
    "    print(result.hex())\n",
    "    return resutl.hex()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "latin-desert",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-ae459d5125a3>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-7-ae459d5125a3>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    if_name_==\"_main_\":\u001b[0m\n\u001b[1;37m                       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    " if_name_==\"_main_\":\n",
    "    coins = derive_wallets(mnemonic)\n",
    "    print(coins)\n",
    "    print(coins['eth'][0]['privkey'])\n",
    "    print(priv_key_to_account('92sByjgSzn5wTF3kZE8X7d61aeeFswuMzVoKqs2nJbkH9Tur9F4', 'eth'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "inside-recorder",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)\n",
    "output, err = p.communicate()\n",
    "p_status = p.wait()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "animal-paraguay",
   "metadata": {},
   "outputs": [
    {
     "ename": "JSONDecodeError",
     "evalue": "Expecting value: line 1 column 1 (char 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-11-988e966a42bd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mkeys\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkeys\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\json\\__init__.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[0;32m    355\u001b[0m             \u001b[0mparse_int\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mparse_float\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    356\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[1;32m--> 357\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    358\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    359\u001b[0m         \u001b[0mcls\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mJSONDecoder\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\json\\decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[1;34m(self, s, _w)\u001b[0m\n\u001b[0;32m    335\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    336\u001b[0m         \"\"\"\n\u001b[1;32m--> 337\u001b[1;33m         \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0midx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    339\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\json\\decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[1;34m(self, s, idx)\u001b[0m\n\u001b[0;32m    353\u001b[0m             \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscan_once\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0midx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    354\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 355\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Expecting value\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    356\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)"
     ]
    }
   ],
   "source": [
    "keys = json.loads(output)\n",
    "print(keys)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "prostate-delta",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:pyvizenv]",
   "language": "python",
   "name": "conda-env-pyvizenv-py"
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
