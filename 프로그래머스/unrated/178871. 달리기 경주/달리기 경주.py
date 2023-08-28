def solution(players, callings):
    answer = []
    ranks = {k:v for v, k in enumerate(players)}
    
    for call in callings:
        n_temp = ranks[call]
        n_swap = n_temp - 1
        swap_player = players[n_swap]
        # print(f"n_temp: {n_temp}, n_swap: {n_swap}, call: {call}, swap_player: {swap_player}")
        players[n_swap] = call
        players[n_temp] = swap_player
        ranks[call] = n_swap
        ranks[swap_player] = n_temp
    return players