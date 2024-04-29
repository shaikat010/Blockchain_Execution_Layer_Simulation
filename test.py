from create_keys_signatures import *
data = "erverververvtrv"
node_private_key = get_private_signing_key()
print(node_private_key)
print("***************************************************")
signature = make_signature(data,node_private_key)
print("***********This is the signature ***************")
print(signature)