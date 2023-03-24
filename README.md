This script is small compilation with choices to check for:
- Latest blocks -> eth_blockNumber
- Current Balance -> eth_getBalance
- Getting transaction count -> eth_getTransactionCount
- Resolving ENS domain name to wallet address -> with web3.py ENS API library

With added features to check on Goerli and Sepolia instead of default in mainnet

How to use:
- Unzip the files (make sure index.py, sepolia.py, and goerli.py are in the same folder)
- run "python index.py"
- Type 1 or 2 when asked for ENS domain name:
    - "1" : Will use the default quicknode.eth ENS domain
    - "2" : you may choose and enter custom domain.eth ENS domain (such as vitalik.eth)
- Type "y" and/or "y" again for the second choice to also check in goerli and/or sepolia
    - Type "y" then "y" : will check on both Sepolia and goerli
    - Type "y" then "n" : will check on goerli only
    - Type "n" then "y" : will check on sepolia only
    - Type "n" then "n" : will check on mainnet only


Note:
- There's obselete warning when running the script for using v5 version of ENS API even though already used the stable version from https://web3py.readthedocs.io/en/latest/ens_overview.html
- This can be safely ignored.
