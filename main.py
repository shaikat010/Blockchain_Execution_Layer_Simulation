import fastapi as _fastapi
import blockchain as _blockchain
from mempool import current_txn_index_to_mine, store_transaction_in_pool, check_txn_integrity, format_txn, \
    get_current_index_to_mine, load_requesting_transactions, get_the_Txn_to_mine
from create_keys_signatures import get_private_signing_key, get_public_verifying_key, make_signature
from starlette.responses import FileResponse
from supporting_functions import build_transaction
from Leader_Selection_Raft import select_block_leader

personal_access_token = 323232

# We will be running multiple blockchains here in the next version
blockchain = _blockchain.Blockchain()
B1 = _blockchain.Blockchain()
B2 = _blockchain.Blockchain()
B3 = _blockchain.Blockchain()
B4 = _blockchain.Blockchain()

peers = [blockchain, B1, B2, B3, B4]

app = _fastapi.FastAPI()


# endpoint to mine a block
# The data in the mine block has to be according to the memory pool's data only
@app.post("/mine_block/")
def mine_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    transaction = get_the_Txn_to_mine()

    selected_peer_id = select_block_leader([blockchain, B1, B2, B3, B4])

    block = None
    # Make sure to use the data = data for the next BC 2303 class!
    for i in peers:
        if i.peer_id == selected_peer_id:
            block = i.mine_block(data=str(transaction))

    # Implement a mechanism here for checking the length of the largest blockchain and then
    # make sure to add the last or the leaf block in that blockchain to all the other chains

    # CODE IS UNSTABLE --> DO NOT USE THIS PART OF THE CODE
    # CODE IS NOW STABLE DUE TO MAKING SURE THAT ALL THE TIMESTAMP FOR ALL THE CHAINS IN THE GENESIS BLOCK IS SAME
    largest = 0
    largest_peer_id = None
    longest_chain = None
    for i in peers:
        if len(i.chain) > largest:
            largest = len(i.chain)
            longest_chain = i

    for i in peers:
        if i == longest_chain:
            pass
        else:
            i.add_block_from_leader(longest_chain.get_previous_block())

    final_status = None
    chain_validity_status = None
    # CODE UNSTABLE TILL HERE, DO NOT USE THIS PART OF THE CODE!

    if len(blockchain.chain) == len(B1.chain) == len(B2.chain) == len(B3.chain) == len(B4.chain):
        final_status = "The chains are valid and are of the same length!" + "Chain length is " + str(len(blockchain.chain))
        if blockchain.is_chain_valid() and B1.is_chain_valid() and B2.is_chain_valid() and B3.is_chain_valid() and B4.is_chain_valid():
            chain_validity_status = True

    print("This is the final status:")
    print(final_status)
    print("This is the chain validity status:")
    print(chain_validity_status)
    return block


# We can make a new api here that only sends the request for the transaction and not mine directly.
# The mining will be done automatically in the backend after every n amount of time or when the mine block functionality is called
# Every transaction will have 6 things, to,from, balance, timestamp public key and the signature
# This will return a 1 if the transaction was sent to the memory pool!
# So we are taking only the data of the to, from and the balance here!

@app.post("/request_incoming_txn")
def request_txn(data: str):
    # This transaction is a list!
    with open('incoming_transactions.txt', 'a') as file:
        file.write(str(data))
        file.write('\n')

    return data


# endpoint to return the blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    chain = blockchain.chain
    return chain


# endpoint to see if the chain is valid
@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()


# endpoint to return the last block
@app.get("/blockchain/last/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.get_previous_block()


# endpoint to get the private key
@app.get("/get_private_key")
def get_node_private_keys(data:int):
    if not get_private_signing_key() and get_public_verifying_key() and data != personal_access_token:
        return _fastapi.HTTPException(status_code=400, detail="The private key could not be found!")

    if data != personal_access_token:
        return _fastapi.HTTPException(status_code=401, detail="Incorrect personal access token has been given!")

    return FileResponse('sk.pem')


# endpoint to get the public key
@app.get("/get_public_key")
def get_node_public_keys():
    if not get_private_signing_key() and get_public_verifying_key():
        return _fastapi.HTTPException(status_code=400, detail="The public key could not be found!")

    return FileResponse('vk.pem')
