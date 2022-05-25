import os
from time import sleep

gN = 0
hN = 1

board = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,-1,0,0,0,-1,-1,-1,-1,-1,0],
    [0,-1,-1,0,0,0,0,0,0,-1,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

goal = [2,6]
start = [3,0]

visited = [[3,0]]
added = 1

def abs(a):
    if a > 0:
        return a
    else:
        return a*-1

def calcManhattan():
    global board
    global goal
    for row in range(0,len(board)):
        for col in range(0,len(board[0])):
            if board[row][col] != -1:
                board[row][col] = abs(row-goal[0])+abs(col-goal[1])

def printBoard():
    global board
    print("\n+-------------------------------------------+")
    for row in range(0,len(board)):
        print("|",end="")
        for col in range(0,len(board[0])):
            if board[row][col] == -1: 
                print(f" \033[31mX\033[0m |",end="")
            elif board[row][col] == 0:
                print(f" \033[32m{board[row][col]}\033[0m |",end="")
            else:
                if [row,col] in visited:
                    print(f" \033[36m{board[row][col]}\033[0m |",end="")
                else:
                    print(f" {board[row][col]} |",end="")
        print()
        print("+-------------------------------------------+")

def findMinInd(currBlocks):
    global board
    tempValues = []
    for block in currBlocks:
        tempValues.append(board[block[0]][block[1]])
    
    return [i for i,j in enumerate(tempValues) if j == min(tempValues)]

def bestFirst():
    global visited
    global start
    global goal
    calcManhattan()
    print(f"\n\033[36mStart : [{start[0]}][{start[1]}]\033[0m")
    print(f"\033[32mGoal : [{goal[0]}][{goal[1]}]\033[0m")
    printBoard()
    while(1):
        sleep(1)
        # os.system('clear')

        if goal in visited:
            printBoard()
            print("Path found!!")
            break
        printBoard()
        minIndices = findMinInd(visited[0:added])
        addNeighbours(minIndices)
      
def addNeighbours(minIndices):
    global added 
    global visited
    global board
    added = 0
    temp = []
    for index in minIndices:
        print(f"Minimum choice is {board[visited[index][0]][visited[index][1]]} and its co-ordinates are {visited[index][0]},{visited[index][1]}")
        if visited[index][0]+1 < 5 and [visited[index][0]+1,visited[index][1]] not in visited and board[visited[index][0]+1][visited[index][1]] != -1:
            temp.append([visited[index][0]+1,visited[index][1]])
        if visited[index][0]-1 >= 0 and [visited[index][0]-1,visited[index][1]] not in visited and board[visited[index][0]-1][visited[index][1]] != -1:
            temp.append([visited[index][0]-1,visited[index][1]])
        if visited[index][1]+1 < 11 and [visited[index][0],visited[index][1]+1] not in visited and board[visited[index][0]][visited[index][1]+1] != -1:
            temp.append([visited[index][0],visited[index][1]+1])
        if visited[index][1]-1 >= 0 and [visited[index][0],visited[index][1]-1] not in visited and board[visited[index][0]][visited[index][1]-1] != -1:
            temp.append([visited[index][0],visited[index][1]-1])

    for t in temp:
        visited.insert(0,t)
        added+=1

bestFirst()