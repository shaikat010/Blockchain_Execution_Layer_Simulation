from ecdsa import SigningKey, NIST384p, VerifyingKey
import hashlib
import json


# =========================================================================================================
# This part is very very important! Comment this out later on!
# private_key = SigningKey.generate(curve=NIST384p)  # uses NIST192p
#
# # The verifying key is like the public key in terms of public key cryptography
# public_key = private_key.get_verifying_key()
# =========================================================================================================

# signature = private_key.sign(b"Sample Digital Signature!")

# print(signature)
# print("This is the type of the signature -------------------------------------")
# print(type(signature))
# print("This is the type of the signature -------------------------------------")
#
# # This is not working, so no need to store the signatures in files
# with open('data.sig', 'wb') as file:
#     file.write(signature)
#
# print("This is the verification status: ")
# print(public_key.verify(signature, b"Sample Digital Signature!"))
#
# print("This is the public key or the verifying key: ")
# print(public_key)
# print(type(public_key))
#
# print("This is the private key: ")
# print(private_key)
# print(type(private_key))


# =========================================================================================================
# This part is also very very important! Make sure to comment this out as well!
# Storing the keys in the respective files
# with open('sk.pem', 'wb') as file:
#     file.write(private_key.to_pem())
#
# with open('vk.pem', 'wb') as file:
#     file.write(public_key.to_pem())
# ===========================================================================================================



def get_public_verifying_key():
    with open("vk.pem") as f:
        vk = VerifyingKey.from_pem(f.read())
        return vk


def get_private_signing_key():
    with open("sk.pem") as f:
        sk = SigningKey.from_pem(f.read(), hashlib.sha256)
        return sk


def make_signature(data, node_private_key):
    data = (data.encode('utf-8'))
    txn_signature = node_private_key.sign(data)
    return txn_signature


def verify_signature(signature, data):
    print("abra ka dabra !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(signature)
    print(type(signature))
    data = str(data)
    print(data)
    print(type(data))
    # Serialize the list to JSON
    json_data = json.dumps(data)

    # Encode the JSON string to bytes
    bytes_data = json_data.encode('utf-8')

    public_key = get_public_verifying_key()
    status = public_key.verify(signature, bytes_data)
    return status


# if public_key == get_public_verifying_key():
#     print("True, it is the same!")
#
# if private_key == get_private_signing_key():
#     print("True, it is the same!")


# signature = make_signature("This is a sample data",private_key)
# print(f'THis is the signature {signature}')

print(get_public_verifying_key())
