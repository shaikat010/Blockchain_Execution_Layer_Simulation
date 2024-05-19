### Blockchain Execution Layer Simulator

### Tasks ToDo:
1. Implement add_block_from_peers method
2. The above implementation should be calling the is_chain_valid() and a is_block_valid() method in the blockchain main class
3. Implement Leader choosing algorithm/ mechanism
4. Implement peer_id setting mechanism for every peer that joins using generate_peer_id
5. Make a transaction class that uses the __repr__ method for building the transactions


### About: Memory Pool
The transaction will be stored here initially. The transaction validity will be checked here as well.
Only the transactions that are valid will be sent to the blockchain structure. 
The memory pool will also check some other features as well, like the timestamp of the transaction etc.
Structure for keeping the transactions.
This is for the formatting of the transactions.
Store the data from the memory pool into the data file or any other file if necessary! --> txn_data.
We need an index for the transaction.
Also, we need a status for the transactions that have been mined already.

### Additional Notes and Concerns
1. Refer to the alternative_files directory for the additional codes not included in the main project
2. The consensus mechanism used here is a naive RAFT consensus mechanism (Leader based consensus mechanism)
3. If the Leader is sending a block then there is no need to do validation for the block, just directly add it to the chain
4. However, there will be a complete chain validation after each block is added
5. Recent addition, 