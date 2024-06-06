from create_keys_signatures import get_private_signing_key, make_signature, get_public_verifying_key, verify_signature
import time


def build_transaction(data):
    public_key = get_public_verifying_key()
    data.append(time.time())
    data.append(public_key)

    transaction = {
        'from': data[0],
        'to': data[1],
        'balance': data[2],
        'timestamp': data[3],
        'public_key': data[4],
        'signature': make_signature(data[0:5])
    }

    return transaction

