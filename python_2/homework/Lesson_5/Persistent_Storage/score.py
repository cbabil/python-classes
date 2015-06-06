import shelve
    
def high_score(player, score):

    '''
    This function takes two arguments a string player name
    and an integer score.
    It returns the player's current high score
    '''

    shelf = shelve.open('playerscore.shlf')

    if player not in shelf:
        shelf[player] = score
        highestscore = score
    elif shelf[player] < score:
        shelf[player] = score
        highestscore = score
    else:
        highestscore = shelf[player]
        
    shelf.close()

    return highestscore