# This is important because this file can read the keys and also read the data and be able to verify the signatures as well.
import hashlib
from ecdsa import SigningKey, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der

with open("../vk.pem") as f:
    vk = VerifyingKey.from_pem(f.read())

with open("data", "rb") as f:
    data = f.read()

# # I am currently here at the moment!
# # The issue here is that the signature cannot be converted to bytes format and stored in the file
# # but that is okay, i will not store it in the file for the time being and use it in dynamic memory
# with open("data.sig", "rb") as f:
#     signature = f.read()
#
# assert vk.verify(signature, data, hashlib.sha256, sigdecode=sigdecode_der)
#
# with open("sk.pem") as f:
#     sk = SigningKey.from_pem(f.read(), hashlib.sha256)
#
# new_signature = sk.sign_deterministic(data, sigencode=sigencode_der)
#
#
# # with open("data.sig2", "wb") as f:
# #    f.write(new_signature)
#
# # openssl dgst -sha256 -verify vk.pem -signature data.sig2 data

# I need the vk and the sk from here for the signature and the verification!
def get_verifying_key():
    with open("../vk.pem") as f:
        vk = VerifyingKey.from_pem(f.read())
        return vk


def get_signing_key():
   with open("../sk.pem") as f:
      sk = SigningKey.from_pem(f.read(), hashlib.sha256)
      return sk

# ___________________________________________________________________________


vk = get_verifying_key()
sk = get_signing_key()

print(vk)
print(sk)

# Making the Signature for any data:
print("This is the signature _________________________________________________")
signature = sk.sign(b"This is a sample data")
print(signature)


# print("This is the verification status_____________________________________________")
# print(vk.verify(signature,b"This is a sample data"))


print((vk))