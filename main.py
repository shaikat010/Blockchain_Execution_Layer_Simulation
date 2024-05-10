import fastapi as _fastapi
import blockchain as _blockchain
from mempool import current_txn_index_to_mine, store_transaction_in_pool, check_txn_integrity, format_txn, get_current_index_to_mine, load_requesting_transactions, get_the_Txn_to_mine
from create_keys_signatures import get_private_signing_key, get_public_verifying_key, make_signature
from starlette.responses import FileResponse
from supporting_functions import build_transaction

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()


# endpoint to mine a block
# The data in the mine block has to be according to the memory pool's data only
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    transaction = get_the_Txn_to_mine()

    # Make sure to use the data = data for the next BC 2303 class!
    block = blockchain.mine_block(data=str(transaction))
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
def get_node_private_keys():
    if not get_private_signing_key() and get_public_verifying_key():
        return _fastapi.HTTPException(status_code=400, detail="The private key could not be found!")

    return FileResponse('sk.pem')


# endpoint to get the public key
@app.get("/get_public_key")
def get_node_public_keys():
    if not get_private_signing_key() and get_public_verifying_key():
        return _fastapi.HTTPException(status_code=400, detail="The public key could not be found!")

    return FileResponse('vk.pem')
