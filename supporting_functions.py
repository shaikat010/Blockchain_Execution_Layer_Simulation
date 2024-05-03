# from create_keys_signatures import *
#
# data = "This is a sample data!"
#
# node_private_key = get_private_signing_key()
#
# print(node_private_key)
#
# print("***************************************************")
#
# signature = make_signature(data,node_private_key)
#
# print("***********This is the signature ***************")
#
# print(signature)


from create_keys_signatures import get_private_signing_key, make_signature, get_public_verifying_key,verify_signature
import time
from mempool import check_txn_integrity

def build_transaction(data):
    private_key = get_private_signing_key()
    public_key = get_public_verifying_key()
    data.append(time.time())
    data.append(public_key)
    print(f"This is the size of transaction data list --> {len(data)}")
    signature_data = str(data[0:5])
    print('This is the signature data -----> ')
    print(signature_data)
    print('This is the signature data: ')
    print(signature_data)

    transaction = {
        'from': data[0],
        'to': data[1],
        'balance': data[2],
        'timestamp': data[3],
        'public_key': data[4],
        'signature': make_signature(signature_data, private_key)
    }

    return transaction


built_txn = build_transaction(['Tom', 'sam',101])
print(built_txn)
print(len(built_txn))


print(check_txn_integrity(built_txn))