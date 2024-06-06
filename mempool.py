import time
import datetime
from create_keys_signatures import verify_signature,get_private_signing_key, get_public_verifying_key, make_signature
from supporting_functions import build_transaction

index = 0

# Gives the current index of the transaction that is to be mined
current_txn_index_to_mine = 0

# This is the data structure for the transactions that are currently requested to be stored
transaction_pool = []

# The signature will take all the data and then sign it using the private key to create the signature
sample_transaction = {
    'from': "me",
    'to': "sam",
    "balance": 100,
    'timestamp': 32424234,
    'public_key': "This is a sample public_key",
    'signature': "This is a sample signature"
}


def store_transaction_in_pool(new_transaction):
    global index
    transaction_pool[index] = new_transaction
    index = index + 1


# Functions for checking the integrity of the transactions
def check_txn_integrity(incoming_transaction):
    flag = True

    incoming_transaction_data = list(incoming_transaction.values())

    # timestamp check for the incoming transaction
    if int(incoming_transaction['timestamp']) > int(time.time()):
        print("Transaction is invalid fue to a timestamp fault!")
        flag = False
    else:
        pass

    # format check for the incoming transaction
    if len(incoming_transaction.keys()) < 6:
        print("Transaction is invalid because of length mismatch!")
        flag = False
    else:
        pass

    # Signature Check for the incoming transaction
    if not verify_signature(incoming_transaction['signature'], incoming_transaction_data[0:5]):
        flag = False

    else:
        pass

    return flag


def format_txn(transaction_data):
    formatted_transaction = transaction_data.split(",")
    return formatted_transaction


def get_current_index_to_mine():
    return current_txn_index_to_mine


def load_requesting_transactions():
    current_requesting_transactions = []
    with open('incoming_transactions.txt', 'r') as file:
        for line in file:
            # we are using the strip functionality here because we want to remove the space at the end of each line
            current_requesting_transactions.append(line.strip())

    return current_requesting_transactions


def get_the_Txn_to_mine():
    all_requesting_txns = load_requesting_transactions()
    global current_txn_index_to_mine
    transaction = all_requesting_txns[current_txn_index_to_mine]
    transaction = format_txn(transaction)
    transaction = build_transaction(transaction)

    try:
        check_txn_integrity(transaction)

    except:

        print("Transaction integrity has not been preserved!")
        return False

    current_txn_index_to_mine = current_txn_index_to_mine + 1
    return transaction

