import copy

class State():
    gN = None
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
    ["2","5"," "],
    ["3","6","4"]
]
ini_space = [1,2]

open = []
closed = []

def printState(state):
    matrix = state.board
    print("\n\t\t+-----------+")
    for i in range(3):
        print("\t\t| ",end="")
        for j in range(3):
            print(f"{matrix[i][j]} | ",end="")
        print("\n",end="")
        print("\t\t+-----------+")
    print(f"\t\tf(n) = {state.gN} + {state.hN} = {state.gN+state.hN}")

def gethN(board):
    val = 0
    for i in range(3):
        for j in range(3):
            if goal_board[i][j] == board[i][j]:
                val+=1
    return val

def open_insert(curr_state):
    if len(open) > 0:
        for i,state in enumerate(open):
            if(state.gN+state.hN < curr_state.gN+curr_state.hN):
                open.insert(i,curr_state)
                return
    open.append(curr_state)

def Solution(final_state):
    soln = []
    curr_state = final_state
    while(curr_state!=None):
        soln.insert(0,curr_state)
        curr_state = curr_state.parent
    return soln

def getSucessors(curr_state):
    
    succ = []
    if(curr_state.space[1]+1 <= 2):
            state = copy.deepcopy(curr_state)
            temp = state.board[state.space[0]][state.space[1]]
            state.board[state.space[0]][state.space[1]] = state.board[state.space[0]][state.space[1]+1]
            state.board[state.space[0]][state.space[1]+1] = temp
            state.space[1] += 1
            
            state.parent = curr_state
            state.gN = curr_state.gN + 1
            state.hN = gethN(state.board)
            succ.append(state)
        
    if(curr_state.space[1]-1 >= 0):
            state = copy.deepcopy(curr_state)
            temp = state.board[state.space[0]][state.space[1]]
            state.board[state.space[0]][state.space[1]] = state.board[state.space[0]][state.space[1]-1]
            state.board[state.space[0]][state.space[1]-1] = temp
            
            state.space[1] -= 1
            
            state.parent = curr_state
            state.gN = curr_state.gN + 1
            state.hN = gethN(state.board)
            succ.append(state)

    if(curr_state.space[0]+1 <= 2):
            state = copy.deepcopy(curr_state)
            temp = state.board[state.space[0]][state.space[1]]
            state.board[state.space[0]][state.space[1]] = state.board[state.space[0]+1][state.space[1]]
            state.board[state.space[0]+1][state.space[1]] = temp
            state.space[0] += 1
            
            state.parent = curr_state
            state.gN = curr_state.gN + 1
            state.hN = gethN(state.board)
            succ.append(state)

    if(curr_state.space[0]-1 >= 0):
            state = copy.deepcopy(curr_state)
            temp = state.board[state.space[0]][state.space[1]]
            state.board[state.space[0]][state.space[1]] = state.board[state.space[0]-1][state.space[1]]
            state.board[state.space[0]-1][state.space[1]] = temp
            
            state.space[0] -= 1
            
            state.parent = curr_state
            state.gN = curr_state.gN + 1
            state.hN = gethN(state.board)
            succ.append(state)
    
    return succ

def getIndexOpen(curr_state):
    for i,state in enumerate(open):
        if state.board == curr_state.board:
            return i
    return False

def getIndexClosed(curr_state):
    for i,state in enumerate(closed):
        if state.board == curr_state.board:
            return i
    return False

def Astar():
    start = State()
    start.gN = 0
    start.hN = gethN(ini_board)
    start.board = ini_board
    start.space = ini_space
    start.parent = None

    open.append(start)

    while len(open) != 0:
        print("OPEN : ")
        for a in open:
            printState(a)
        curr_node = open.pop(0)
        curr_board = curr_node.board
        print("CURRENT NODE : ")
        printState(curr_node)

        if curr_board == goal_board:
            return Solution(curr_node)

        closed.append(curr_node)
        succesors = getSucessors(curr_node)

        for sucessor in succesors:
            newgN = curr_node.gN
            if getIndexOpen(sucessor):
                old_node = open[getIndexOpen(sucessor)]
                if(old_node.gN > newgN):
                    old_node.gN = newgN
                    old_node.parent = curr_node
                    old_node = open.pop(getIndexOpen(sucessor))
                    open_insert(old_node)
            elif getIndexClosed(sucessor):
                old_node = closed[getIndexClosed(sucessor)]
                if(old_node.gN > newgN):
                    old_node.gN = newgN
                    old_node.parent = curr_node
                    old_node = closed.pop(getIndexClosed(sucessor))
                    open_insert(old_node)
            else:
                new_node = State()
                new_node.gN = curr_node.gN + 1
                new_node.hN = gethN(sucessor.board)
                new_node.board = sucessor.board
                new_node.space = sucessor.space
                new_node.parent = curr_node
                open_insert(new_node)

ans = Astar()
print(f"SOLUTION : ")
for a in ans:
    printState(a)