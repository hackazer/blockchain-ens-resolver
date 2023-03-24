from web3 import Web3
from ens import ENS
from goerli import get_goerli_balance_and_tx_count
from sepolia import get_sepolia_balance_and_tx_count

# Connect to an Ethereum node
#mainnet_w3 = Web3(Web3.HTTPProvider('https://fittest-skilled-gas.quiknode.pro/b191b6da5d88e90be808a517ad1e9472af783806/'))
#goerli_w3 = Web3(Web3.HTTPProvider('https://broken-hidden-night.ethereum-goerli.quiknode.pro/3caf9d93c922ab578f13d57d2885b602fb915f61/'))
#sepolia_w3 = Web3(Web3.HTTPProvider('https://proud-small-county.ethereum-sepolia.quiknode.pro/f68390f3a1c7694aedf1eb72fa5a04ddf892be16/'))
w3 = Web3(Web3.HTTPProvider('https://fittest-skilled-gas.quiknode.pro/b191b6da5d88e90be808a517ad1e9472af783806/'))

# Create an ENS instance from the Web3 connection
ns = ENS.fromWeb3(w3)

# Option to choose to input their own ENS name or use a hardcoded name
print("Welcome!", "Please choose an option below:")
print("1. Use default hardcoded ENS domain name (quicknode.eth)")
print("2. Input your own ENS domain name")
option = input("Option: ")

# Set default ENS name to use if user chooses option 1
default_ens_name = 'quicknode.eth'

if option == '1':
    ens_name = default_ens_name
elif option == '2':
    ens_name = input("Please enter the ENS domain name: ")
else:
    print("Invalid option. Using default ENS domain name (quicknode.eth).")
    ens_name = default_ens_name

# Look up the hex representation of the address for the name
# Check for balance and transaction count on mainnet
try:
    eth_address = ns.address(ens_name)
    print(f'The Ethereum address for {ens_name} is {eth_address}')

    print(f'Getting data for {ens_name} in mainnet...')
    latest_block = w3.eth.block_number
    mainnet_balance = w3.eth.getBalance(eth_address, block_identifier=latest_block)
    mainnet_tx_count = w3.eth.getTransactionCount(eth_address, block_identifier=latest_block)
    mainnet_balance_eth = Web3.fromWei(mainnet_balance, 'ether')
    print(f'Mainnet blocks number: {latest_block}' )
    print(f'Mainnet balance for {eth_address}: {mainnet_balance_eth} ETH at blocks {latest_block}' )
    print(f'Mainnet transaction count for {eth_address}: {mainnet_tx_count}')
    print('―' * 20) # print horizontal line
    # Ask user if want to check for Goerli chain
    check_goerli = input("Do you want to check Goerli chain? (y/n): ").lower() == 'y'

    # Ask user if want to check for Sepolia chain
    check_sepolia = input("Do you want to check Sepolia chain? (y/n): ").lower() == 'y'

    print('―' * 20) # print horizontal line

    # Check for balances and transaction counts in goerli and sepolia
    if check_goerli:
        print(f'Getting data for {ens_name} in goerli...')
        result = get_goerli_balance_and_tx_count(ens_name)
        if isinstance(result, str):
            # an error occurred, print the error message
            if result == "Error: Could not transact with/call contract function, is contract deployed correctly and chain synced?":
                # print(result)
                print(f'Address is somehow available, but it returns None / 0x in the Goerli blockchain')
            print(f'It seems {ens_name} is not available at Ethereum Goerli blockchain')
            print(result)
            print('―' * 20)  # print horizontal line

        else:
            # if no errors, print result
            goerli_address, goerli_balance, goerli_tx_count, goerli_endpoint = result
            print(f'Goerli Endpoint: {goerli_endpoint}')
            print(f'Goerli chain balance for {goerli_address}: {goerli_balance} ETH')
            print(f'Goerli chain transaction count for {goerli_address}: {goerli_tx_count}')
            print('―' * 20)  # print horizontal line

    if check_sepolia:
        print(f'Getting data for {ens_name} in sepolia...')
        result = get_sepolia_balance_and_tx_count(ens_name)
        if isinstance(result, str):
            # an error occurred, print the error message
            if result == "Error: Could not transact with/call contract function, is contract deployed correctly and chain synced?":
                # print(result)
                print(f'Address is somehow available, but it returns None / 0x in the Sepolia blockchain')
            print(f'It seems {ens_name} is not available at Ethereum Sepolia blockchain')
            print('―' * 20)  # print horizontal line

        else:
            # no errors, unpack the tuple
            sepolia_address, sepolia_balance, sepolia_tx_count, sepolia_endpoint = result
            print(f'Sepolia Endpoint: {sepolia_endpoint}')
            print(f'Sepolia chain balance for {sepolia_address}: {sepolia_balance} ETH')
            print(f'Sepolia chain transaction count for {sepolia_address}: {sepolia_tx_count}')
            print('―' * 20)  # print horizontal line

    if not check_goerli and not check_sepolia:
        # Check for balance and transaction count on mainnet
        print(f'Getting data for {ens_name} in mainnet again...')
        latest_block = w3.eth.block_number
        mainnet_balance = w3.eth.getBalance(eth_address, block_identifier=latest_block)
        mainnet_tx_count = w3.eth.getTransactionCount(eth_address, block_identifier=latest_block)
        mainnet_balance_eth = Web3.fromWei(mainnet_balance, 'ether')
        print(f'Mainnet blocks number: {latest_block}')
        print(f'Mainnet balance for {eth_address}: {mainnet_balance_eth} ETH')
        print(f'Mainnet transaction count for {eth_address}: {mainnet_tx_count}')
        print('―' * 20)  # print horizontal line

except Exception as e:
    print(f'Error: {e}')