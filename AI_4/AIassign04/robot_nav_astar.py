import os
from time import sleep

gN = 0
hN = 1

board = [
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[-1,-1],[0,0],[0,0],[0,0],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[0,0]],
    [[0,0],[-1,-1],[-1,-1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[-1,-1],[0,0]],
    [[0,0],[0,0],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
]

goal = [2,6]
start = [3,0]

closed = []
open = [[3,0]]

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
            if board[row][col][1] != -1:
                board[row][col][1] = abs(row-goal[0])+abs(col-goal[1])

def printBoard():
    global board
    print("\n+-----------------------------------------------------------------+")
    for row in range(0,len(board)):
        print("|",end="")
        for col in range(0,len(board[0])):
            if board[row][col][hN] == -1: 
                print(f" \033[31m X \033[0m |",end="")
            elif board[row][col][hN] == 0:
                print(f" \033[32m {board[row][col][hN]} \033[0m |",end="")
            else:
                if [row,col] in closed:
                    print(f" \033[36m{board[row][col][gN]}+{board[row][col][hN]}\033[0m |",end="")
                else:
                    print(f" {board[row][col][gN]}+{board[row][col][hN]} |",end="")
        print()
        print("+-----------------------------------------------------------------+")

def findMinInd(open):
    global board
    tempValues = []
    for block in open:
        tempValues.append(board[block[0]][block[1]][gN]+board[block[0]][block[1]][hN])
    
    return [open[i] for i,j in enumerate(tempValues) if j == min(tempValues)]

def addNeighbours(minIndices): 
    global closed
    global board
    temp = []
    for cord in minIndices:
        open.remove(cord)
        closed.append(cord)
    for cord in minIndices:
        print(f"Minimum choice is {board[cord[0]][cord[1]][gN]}+{board[cord[0]][cord[1]][hN]} and its co-ordinates are {cord[0]},{cord[1]}")
        if cord[0]+1 < 5 and [cord[0]+1,cord[1]] not in open and board[cord[0]+1][cord[1]][hN] != -1:
            if [cord[0]+1,cord[1]] not in closed:
                temp.append([cord[0]+1,cord[1]])
                board[cord[0]+1][cord[1]][0] = board[cord[0]][cord[1]][0] + 1
        if cord[0]-1 >= 0 and [cord[0]-1,cord[1]] not in open and board[cord[0]-1][cord[1]][hN] != -1:
            if [cord[0]-1,cord[1]] not in closed:
                temp.append([cord[0]-1,cord[1]])
                board[cord[0]-1][cord[1]][0] = board[cord[0]][cord[1]][0] + 1
        if cord[1]+1 < 11 and [cord[0],cord[1]+1] not in open and board[cord[0]][cord[1]+1][hN] != -1:
            if [cord[0],cord[1]+1] not in closed:
                temp.append([cord[0],cord[1]+1])
                board[cord[0]][cord[1]+1][0] = board[cord[0]][cord[1]][0] + 1
        if cord[1]-1 >= 0 and [cord[0],cord[1]-1] not in open and board[cord[0]][cord[1]-1][hN] != -1:
            if [cord[0],cord[1]-1] not in closed:
                temp.append([cord[0],cord[1]-1])
                board[cord[0]][cord[1]-1][0] = board[cord[0]][cord[1]][0] + 1

    for t in temp:
        if t not in closed and t not in open:
            open.insert(0,t)


def Astar():
    global closed
    global open
    global start
    global goal
    calcManhattan()
    print(f"\n\033[36mStart : [{start[0]}][{start[1]}]\033[0m")
    print(f"\033[32mGoal : [{goal[0]}][{goal[1]}]\033[0m")
    printBoard()
    while(1):
        sleep(1)
        minblocks = []
        minblocks = findMinInd(open)
        print(minblocks)
        addNeighbours(minblocks)
        
        if goal in closed:
            printBoard()
            print("Path found!!")
            break
        printBoard()
        
Astar()