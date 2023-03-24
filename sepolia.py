from web3 import Web3
from ens import ENS

# Connect to a Sepolia Ethereum node
sepolia_endpoints = "https://proud-small-county.ethereum-sepolia.quiknode.pro/f68390f3a1c7694aedf1eb72fa5a04ddf892be16/"
w3 = Web3(Web3.HTTPProvider(sepolia_endpoints))

# Create an ENS instance from the Web3 connection
ns = ENS.fromWeb3(w3)


def get_sepolia_balance_and_tx_count(address):
    try:
        if address == 'quicknode.eth':
            eth_address = '0xD10E24685c7CDD3cd3BaAA86b09C92Be28c834B6'
            print(f'Used {eth_address} instead of quicknode.eth because the ENS domain cant got resolved in Sepolia')
        else:
            # Look up the hex representation of the address for the name
            eth_address = ns.address(address)
    except Exception as e:
        return f"Error: {e}"

    # Get the latest block number
    latest_block_number = w3.eth.block_number

    try:
        # Get the balance of the address at the latest block number
        balance_wei = w3.eth.get_balance(eth_address, block_identifier=latest_block_number)
        # Convert it to ether denom.
        balance_eth = w3.fromWei(balance_wei, 'ether')

        # Get the transaction count of the address at the latest block number
        tx_count = w3.eth.get_transaction_count(eth_address, block_identifier=latest_block_number)

        return eth_address, balance_eth, tx_count, sepolia_endpoints
    except Exception as e:
        return f"Error: {e}"
