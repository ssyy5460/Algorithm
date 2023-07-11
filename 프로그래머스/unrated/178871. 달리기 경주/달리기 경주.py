def solution(players, callings):
    answer = []
    dict = {} 
    
    for i,val in enumerate(players):
        dict[val] = i
        
    for call in callings:
        pre,post = dict[call] - 1, dict[call]
        dict[players[pre]] = post
        dict[players[post]] = pre
        players[pre], players[post] = players[post],players[pre]
    return players

