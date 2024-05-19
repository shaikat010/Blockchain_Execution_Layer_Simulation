from ecdsa import SigningKey, NIST384p, VerifyingKey
import hashlib
import json

# This part is very very important! Comment this out later on!
private_key = SigningKey.generate(curve=NIST384p)  # uses NIST192p
print(private_key)
#
# # The verifying key is like the public key in terms of public key cryptography
public_key = private_key.get_verifying_key()
print(public_key)


signature = private_key.sign(b"Sample Digital Signature!")

print("This is the verification status: ")
print(public_key.verify(signature, b"Sample Digital Signature!"))


# =========================================================================================================
# This part is also very very important! Make sure to comment this out as well!
# Storing the keys in the respective files
# with open('sk.pem', 'wb') as file:
#     file.write(private_key.to_pem())
#
# with open('vk.pem', 'wb') as file:
#     file.write(public_key.to_pem())
# ===========================================================================================================


# if public_key == get_public_verifying_key():
#     print("True, it is the same!")
#
# if private_key == get_private_signing_key():
#     print("True, it is the same!")


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



# This is taken form the supporting function file
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