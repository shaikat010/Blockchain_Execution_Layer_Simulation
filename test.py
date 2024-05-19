import blockchain as _blockchain
from mempool import get_the_Txn_to_mine
from Leader_Selection_Raft import select_block_leader

# We will be running multiple blockchains here in the next version
blockchain = _blockchain.Blockchain()
B1 = _blockchain.Blockchain()
B2 = _blockchain.Blockchain()
B3 = _blockchain.Blockchain()
B4 = _blockchain.Blockchain()

peers = [blockchain, B1, B2, B3, B4]


def mine_block():

    transaction = get_the_Txn_to_mine()

    selected_peer_id = select_block_leader(peers)

    block = None
    # Make sure to use the data = data for the next BC 2303 class!
    for i in peers:
        if i.peer_id == selected_peer_id:
            block = i.mine_block(data=str(transaction))

    # Implement a mechanism here for checking the length of the largest blockchain and then
    # make sure to add the last or the leaf block in that blockchain to all the other chains

    # CODE IS UNSTABLE --> DO NOT USE THIS PART OF THE CODE
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
        final_status = "The chains are valid and are of the same length!" + "chain length is " + str(
            len(blockchain.chain))
    if blockchain.is_chain_valid() and B1.is_chain_valid() and B2.is_chain_valid() and B3.is_chain_valid() and B4.is_chain_valid():
        chain_validity_status = True

    print("This is the final status:")
    print(final_status)
    print("This is the chain validity status:")
    print(chain_validity_status)

    return block


for i in range(12):
    mine_block()