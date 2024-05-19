from random import randint


def generate_new_peer_id(lower_bound=7859578, upper_bound=7596856798679):
    generated_peer_id = randint(lower_bound, upper_bound)
    with open('available_peers.txt', 'a') as file:
        file.write(str(generated_peer_id) + '\n')
    return generated_peer_id


