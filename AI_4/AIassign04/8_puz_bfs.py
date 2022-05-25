import copy

open = []
closed = []

class State():
    hN = None
    board = None
    space = None
    parent = None

goal_board = [
    ["1","8","7"],
    ["2"," ","6"],
    ["3","4","5"]
]

ini_board = [
    ["1","8","7"],
    ["2"," ","5"],
    ["3","6","4"]
]
ini_space = [1,1]

def gethN(board):
    val = 0
    for i in range(3):
        for j in range(3):
            if goal_board[i][j] == board[i][j]:
                val+=1
    return val

start = State()
start.hN = gethN(ini_board)
start.board = ini_board
start.space = ini_space
start.parent = None

open.append(start)

def printState(matrix):
    print("\n\t\t+-----------+")
    for i in range(3):
        print("\t\t| ",end="")
        for j in range(3):
            print(f"{matrix[i][j]} | ",end="")
        print("\n",end="")
        print("\t\t+-----------+")
    print(f"\t\th(n) = {gethN(matrix)}")

def open_insert(curr_state):
    if len(open) > 0:
        for i,state in enumerate(open):
            if(state.hN < curr_state.hN):
                open.insert(i,curr_state)
                return
    open.append(curr_state)

def empty_open():
    global open
    open = []

def successors(curr_state):
    if(curr_state.space[1]+1 <= 2):
        state = copy.deepcopy(curr_state)
        temp = state.board[state.space[0]][state.space[1]]
        state.board[state.space[0]][state.space[1]] = state.board[state.space[0]][state.space[1]+1]
        state.board[state.space[0]][state.space[1]+1] = temp
        state.space[1] += 1
        state.hN = gethN(state.board)
        state.parent = curr_state
        if state.board not in closed:
            open_insert(state)
    
    if(curr_state.space[1]-1 >= 0):
        state = copy.deepcopy(curr_state)
        temp = state.board[state.space[0]][state.space[1]]
        state.board[state.space[0]][state.space[1]] = state.board[state.space[0]][state.space[1]-1]
        state.board[state.space[0]][state.space[1]-1] = temp
        state.space[1] -= 1
        state.hN = gethN(state.board)
        state.parent = curr_state
        if state.board not in closed:
            open_insert(state)

    if(curr_state.space[0]+1 <= 2):
        state = copy.deepcopy(curr_state)
        temp = state.board[state.space[0]][state.space[1]]
        state.board[state.space[0]][state.space[1]] = state.board[state.space[0]+1][state.space[1]]
        state.board[state.space[0]+1][state.space[1]] = temp
        state.space[0] += 1
        state.hN = gethN(state.board)
        state.parent = curr_state
        if state.board not in closed:
            open_insert(state)

    if(curr_state.space[0]-1 >= 0):
        state = copy.deepcopy(curr_state)
        temp = state.board[state.space[0]][state.space[1]]
        state.board[state.space[0]][state.space[1]] = state.board[state.space[0]-1][state.space[1]]
        state.board[state.space[0]-1][state.space[1]] = temp
        state.space[0] -= 1
        state.hN = gethN(state.board)
        state.parent = curr_state
        if state.board not in closed:
            open_insert(state)

def Solution(final_state):
    soln = []
    curr_state = final_state
    while(curr_state!=None):
        soln.insert(0,curr_state)
        curr_state = curr_state.parent
    return soln

def bfs():
    while len(open) != 0:
        print("OPEN : ")
        for a in open:
            printState(a.board)
        curr_node = open.pop(0)
        closed.append(curr_node.board)
        print("SELECTED : ")
        printState(curr_node.board)
        if curr_node.board == goal_board:
            return Solution(curr_node)
        empty_open()
        successors(curr_node)

ans = bfs()
print("SOLUTION : ")
for a in ans:
    printState(a.board)