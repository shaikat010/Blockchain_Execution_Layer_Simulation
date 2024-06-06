from ecdsa import SigningKey, NIST384p, VerifyingKey
import hashlib
import json


def create_keys():
    # private key are created here
    private_key = SigningKey.generate(curve=NIST384p)
    print(private_key)

    # creating the public key from the private key
    public_key = private_key.get_verifying_key()
    print(public_key)

    return private_key, public_key


# Storing the public and the private keys
def store_keys(private_key, public_key):
    with open('sk.pem', 'wb') as file:
        file.write(private_key.to_pem())

    with open('vk.pem', 'wb') as file:
        file.write(public_key.to_pem())


def get_public_verifying_key():
    with open("vk.pem") as f:
        vk = VerifyingKey.from_pem(f.read())
        return vk


def get_private_signing_key():
    with open("sk.pem") as f:
        sk = SigningKey.from_pem(f.read())
        return sk


def make_signature(data):
    node_private_key = get_private_signing_key()
    txn_signature = node_private_key.sign(f"{data}".encode('utf-8'))
    return txn_signature


def verify_signature(Signature, data):
    node_public_key = get_public_verifying_key()
    try:
        Status = node_public_key.verify(Signature, f"{data}".encode('utf-8'))

    except:
        Status = False

    return Status

