#!/usr/bin/python

# state is a tuple (board, players)
# board is a list of ints, each list is one nim stack
# players is a list of two ids
# best not to use 1 and 0 for ids, since 0 is false, and we might end
# up comparing against returned player ID

cache = {}

def play(board, players = ["l", "r"], display =True):
    '''Convenience method for kicking off Nim games. Sorts the board
    to aid the caching. Uses default "l" and "r" players. (note:
    changing these will screw up the caching!). By default, it does
    not return a value - it just displays it. The return value is in
    the cache, if you need it. Setting display=False will trigger
    return value. Define a helper function if you want both display
    and return (function display_result will be useful for this)
    Note: display is bottom to top. Original situation is at the bottom.
    '''
    board = sorted(board)
    result = evaluate((board, players))
    if display:
        display_result(result)
    else:
        return result


def evaluate(state):
    '''Evaluates a state by recursive descent. Stops when it finds a
    move which wins for the current player. This is extremely
    ineffiecient, and is really just a starting point.'''
    global cache
    moves = possible_moves(state)
    cache_hash = "*".join([str (i) for i in state[0]+state[1]])
    if cache.get(cache_hash, None):
        return (cache[cache_hash])
    if empty(state):
        return other_player(state),[state]
    for move in moves:
        winner, history = evaluate(move)
        if  winner == this_player(state):
            cache[cache_hash] = (this_player(state), history + [state])
            return cache[cache_hash]
    cache[cache_hash] = (other_player(state), history + [state])    
    return cache[cache_hash]


def possible_moves(state):
    '''return a generator of all possible states that current player
    could choose to put us into'''
    state = rotate_players(state)
    board, players = state
    for index, stack in enumerate(board):
        for i in range(stack):
            new_board = board[:index]+[i]+board[index+1:]
            new_board = [stack for stack in new_board if stack >0]
            yield (new_board, players)
 

def display_result(result):
    winner, history = result
    print winner
    for item in history:
        print item 

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


players = ['l', 'r']
