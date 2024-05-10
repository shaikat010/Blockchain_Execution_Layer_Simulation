from create_keys_signatures import get_private_signing_key, make_signature, get_public_verifying_key, verify_signature
import time

def build_transaction(data):
    public_key = get_public_verifying_key()
    data.append(time.time())
    data.append(public_key)
    print(f"This is the size of transaction data list --> {len(data)}")
    signature_data = "This is the sample signature data"

    transaction = {
        'from': data[0],
        'to': data[1],
        'balance': data[2],
        'timestamp': data[3],
        'public_key': data[4],
        'signature': make_signature(signature_data)
    }

    return transaction


# built_txn = build_transaction(['Tom', 'sam', 101])
# print("This is the transaction that was built: ")
# print(built_txn)
# print("-----------------------------------------------")
#
# print("This is the length of the transaction that was built: ")
# print(len(built_txn))
# print("---------------------------------------------------")
#
# print("This is the transaction integrity")
# print(check_txn_integrity(built_txn))
# print("-------------------------------------------------")
