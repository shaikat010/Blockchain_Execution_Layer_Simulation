# The transaction will be stored here initially,
# The transaction validity will be checked here as well
# Only the transactions that are valid will be sent to the blockchain structure
# The memory pool will also check some other features as well like the timestamp of the transaction etc

import time
import datetime
from create_keys_signatures import get_private_signing_key,get_public_verifying_key,make_signature,verify_signature

# Structure for keeping the transactions
# This is for the formatting of the transactions
# Store the data from the memory pool into the data file or any other file if necessary! --> txn_data
# We need an index for the transaction
# also we need a status for the transactions that have been mined already

index = 0

# The genesis block will be the first index to be mined
current_txn_index_to_mine = 0

transaction_pool = []


# The signature will take all the data and then sign it using the private key to create the signature
sample_transaction = {
    'from':"me",
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
    print("##########################################################")
    print(incoming_transaction_data)
    print(type(incoming_transaction_data))


    # timestamp check
    if int(incoming_transaction['timestamp']) > int(time.time()):
        print("Transaction is invalid fue to a timestamp fault!")
        flag = False
    else:
        pass

    # format check
    if len(incoming_transaction.keys()) < 6:
        print("Transaction is invalid because of length mismatch!")
        flag = False
    else:
        pass

    # Signature Check
    if not verify_signature(incoming_transaction['signature'], incoming_transaction_data[0:5]):
        flag = False

    else:
        pass

    return flag



def format_txn(transaction_data):
    formatted_transaction = transaction_data.split(",")
    return formatted_transaction
    # also convert transaction into a dictionary here


def get_current_index_to_mine():
    return current_txn_index_to_mine

