def solution(players, callings):
    answer = players
    players_dict = {player: idx for idx, player in enumerate(players)}

    for call in callings:
        idx = players_dict[call]
        answer[idx], answer[idx - 1] = answer[idx - 1], answer[idx]
        
        players_dict[players[idx]] = idx
        players_dict[players[idx - 1]] = idx - 1

    return answer
