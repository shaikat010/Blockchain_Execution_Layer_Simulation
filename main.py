import fastapi as _fastapi
import blockchain as _blockchain
from mempool import current_txn_index_to_mine, get_the_Txn_to_mine, get_current_index_to_mine, get_public_verifying_key, \
    get_private_signing_key
from create_keys_signatures import get_private_signing_key, get_public_verifying_key, make_signature
from starlette.responses import FileResponse
from supporting_functions import build_transaction
from Leader_Selection_Raft import select_block_leader
import uvicorn

personal_access_token = 323232

blockchain = _blockchain.Blockchain()
B1 = _blockchain.Blockchain()
B2 = _blockchain.Blockchain()
B3 = _blockchain.Blockchain()
B4 = _blockchain.Blockchain()

peers = [blockchain, B1, B2, B3, B4]

# This line makes a fastapi app
app = _fastapi.FastAPI()


@app.post("/mine_block/")
def mine_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid!")

    transaction = get_the_Txn_to_mine()

    selected_peer_id = select_block_leader([blockchain, B1, B2, B3, B4])

    block = None

    for i in peers:
        if i.peer_id == selected_peer_id:
            block = i.mine_block(data=str(transaction))

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

    if len(blockchain.chain) == len(B1.chain) == len(B2.chain) == len(B3.chain) == len(B4.chain):
        final_status = True
        final_status = f'THe chains are of the same size and size is {len(blockchain.chain)}'
        if blockchain.is_chain_valid() and B1.is_chain_valid() and B2.is_chain_valid() and B3.is_chain_valid() and B4.is_chain_valid():
            chain_validity_status = True

    print("This is the final chain status: ")
    print(final_status)
    print("This is the chain validity status:")
    print(chain_validity_status)

    return block


@app.post("/request_incoming_txn")
def request_txn(data: str):
    with open("incoming_transactions.txt", 'a') as file:
        file.write(str(data))
        file.write("\n")

    return data


@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="This blockchain is invalid!")

    chain = blockchain.chain

    return chain


@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="This blockchain is invalid!")

    return blockchain.is_chain_valid()


@app.get("/blockchain/last")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="This blockchain is invalid!")

    return blockchain.get_previous_block()


@app.get("/get_public_key")
def get_node_public_key():
    if not get_public_verifying_key() and get_private_signing_key():
        return _fastapi.HTTPException(status_code=400, detail="The public key could not be found!")

    return FileResponse('vk.pem')


@app.get("/get_private_key/{data}")
def get_node_private_key(data: int):
    if not get_public_verifying_key() and get_private_signing_key() and data != personal_access_token:
        return _fastapi.HTTPException(status_code=400, detail="The public key could not be found!")

    if data != personal_access_token:
        return _fastapi.HTTPException(status_code=401, detail="The token provided is incorrect!")

    return FileResponse("sk.pem")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)