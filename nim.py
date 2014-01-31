#!/usr/bin/python

# state is a tuple (board, players)
# board is a list of ints, each list is one nim stack
# players is a list of two ids
# best not to use 1 and 0 for ids, since 0 is false, and we might end
# up comparing against returned player ID

def evaluate(state):
    moves = possible_moves(state)
    if empty(state):
        return other_player(state),[state]
    for move in moves:
        winner, history = evaluate(move)
        if len (history) % 100 == 21:
            print ".",
        if  winner == this_player(state):
            return this_player(state), history + [state]
    return other_player(state), history+ [state] 

def possible_moves(state):
    '''return a generator of all possible states that current player
    could choose to put us into'''
    state = rotate_players(state)
    board, players = state
    for index, stack in enumerate(board):
        for i in range(1, stack+1):
            yield (board[:index]+[stack-i]+board[index+1:], players)

def empty(state):
    return sum(state[0]) == 0

def this_player(state):
    '''return the player whose turn it is'''
    return state[1][0]

def other_player(state):
    '''return the player whose move it isn't'''
    return state[1][1]
 
def rotate_players(state):
    '''Return state with players exchanged, nondestructively'''
    board, players = state
    return (board, [players[1], players[0]])
