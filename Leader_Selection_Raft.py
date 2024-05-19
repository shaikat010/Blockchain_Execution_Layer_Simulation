import random
import blockchain as _blockchain

Leader = None


def select_block_leader(peers_list):
    peers_id_list = []

    for i in peers_list:
        peers_id_list.append(i.peer_id)

    selected_peer_id = random.choice(peers_id_list)

    global Leader
    Leader = selected_peer_id

    return selected_peer_id
