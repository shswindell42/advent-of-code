
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.


maze: list[list[str]] = []
with open('./day10.txt', 'r') as fp:
    for line in fp.readlines():
        maze.append([*line.strip()])

# find the S position (row, column)
for i, l in enumerate(maze):
    for j, c in enumerate(l):
        if c == 'S':
            startingPosition = (i, j)
            break

# start at S, try each type of Pipe and see which has the longest loop
pipes = ['|', '-', 'L', 'J', '7', 'F']
maxSteps = 0
maxPipe = "."
maxLoopPath = []
startPipe = '|'
for p in pipes:
    maze[startingPosition[0]][startingPosition[1]] = p
    steps = 0
    curPos = startingPosition
    prevPos = startingPosition
    stop = False
    wasLoop = False
    loopPath = []
    
    # navigate the maze
    while not stop:
        curPipe = maze[curPos[0]][curPos[1]]
        if curPipe == "|":
            up = (curPos[0] - 1, curPos[1])
            down = (curPos[0] + 1, curPos[1])

            if maze[up[0]][up[1]] in ["7", "F", "|"] and up != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = up
            elif maze[down[0]][down[1]] in ["L", "J", "|"] and down != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = down
            else:
                stop = True
        elif curPipe == "-":
            left = (curPos[0], curPos[1] - 1)
            right = (curPos[0], curPos[1] + 1)

            if maze[left[0]][left[1]] in ["F", "L", "-"] and left != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = left
            elif maze[right[0]][right[1]] in ["J", "7", "-"] and right != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = right
            else:
                stop = True
        elif curPipe == "L":
            up = (curPos[0] - 1, curPos[1])
            right = (curPos[0], curPos[1] + 1)

            if maze[up[0]][up[1]] in ["|", "7", "F"] and up != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = up
            elif maze[right[0]][right[1]] in ["7", "J", "-"] and right != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = right
            else:
                stop = True
        elif curPipe == "J":
            up = (curPos[0] - 1, curPos[1])
            left = (curPos[0], curPos[1] - 1)

            if maze[up[0]][up[1]] in ["|", "7", "F"] and up != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = up
            elif maze[left[0]][left[1]] in ["F", "L", "-"] and left != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = left
            else:
                stop = True

        elif curPipe == "7":
            left = (curPos[0], curPos[1] - 1)
            down = (curPos[0] + 1, curPos[1])

            if maze[left[0]][left[1]] in ["F", "L", "-"] and left != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = left
            elif maze[down[0]][down[1]] in ["L", "J", "|"] and down != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = down
            else:
                stop = True

        elif curPipe == "F":
            right = (curPos[0], curPos[1] + 1)
            down = (curPos[0] + 1, curPos[1])

            if maze[right[0]][right[1]] in ["J", "7", "-"] and right != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = right
            elif maze[down[0]][down[1]] in ["L", "J", "|"] and down != prevPos:
                loopPath.append(curPos)
                prevPos = curPos
                curPos = down
            else:
                stop = True

        steps += 1

        if curPos == startingPosition:
            stop = True
            wasLoop = True
    
    if wasLoop:
        if maxSteps < steps:
            maxSteps = steps
            maxLoopPath = loopPath
            startPipe = p

maze[startingPosition[0]][startingPosition[1]] = startPipe

print(f"Longest loops is {maxSteps} steps, farthest point is {maxSteps / 2} steps away")

# update all the locations in the map to a "V" for down
# and "^" for up
# for i, l in enumerate(maxLoopPath):
#     if maxLoopPath[i-1][0] > l[0]:
#         maze[l[0]][l[1]] = 'V'
#     elif maxLoopPath[i-1][0] < l[0]:
#         maze[l[0]][l[1]] = '^'
#     else: 
#         maze[l[0]][l[1]] = '~'

# for i, l in enumerate(maxLoopPath):
#     maze[l[0]][l[1]] = '@'

# for r in maze:
#     for c in r:
#         print(c, end="")
#     print()

upChars = ["|", "L", "J"]
tileCount = 0
inLoop = False
for i, r in enumerate(maze):
    for j, c in enumerate(r):
        if (i, j) in maxLoopPath:
            if c in upChars:
                inLoop = not inLoop
        else:
            if inLoop:
                tileCount += 1
        

print(f"There are {tileCount} tiles inside the loop")