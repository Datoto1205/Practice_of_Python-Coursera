# Maze Problem (applied the idea of stack)
maze = [[0,0,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,1],
[1,0,1,1,0,0,1,0,1,1],
[1,0,0,0,0,1,0,0,0,1],
[1,1,0,1,0,1,0,1,0,1],
[1,1,1,1,1,1,0,1,1,1],
[1,0,0,0,0,0,0,1,0,0],
[1,1,0,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]]
# We assume that the the most top left one is the origin of the corordinate, 1 means wakk, and 0 means road.
# We assume that the extrance of this maze was on the top & left side.

correctRoute = []   # It involved all the point of the correct route.
routeHistory = []   # It involved all the point we went through so that we could use it to force the computer to change the direction if we entered the blind alley.

def findTheStart(maze):
    for i in range(0, len(maze)):
        if (maze[i][0] == 0):
            correctRoute.append([i, 0])
            break
# We use this function to find the extrance of the maze.

findTheStart(maze)

# Afterward, we devided our movement into four parts with the direction.
def goUp():

    location = correctRoute[len(correctRoute)-1]
    movedLocation = [location[0]-1, location[1]]

    if (location[0] == 0):
        return False
        # Go out of the maze.

    if (maze[location[0]-1][location[1]] == 1):
        return False
        # Face the wall.

    if (movedLocation in routeHistory):
        return False
        # To prevent the problem of blind alley.
        # We could use syntax "a in b" to examine whether a is in b.
    else:
        correctRoute.append(movedLocation)
        routeHistory.append(movedLocation)
        return True

def goRight():

    location = correctRoute[len(correctRoute)-1]
    movedLocation = [location[0], location[1]+1]

    if (location[1] == 11):
        return False
    elif (maze[location[0]][location[1]+1] == 1):
        return False
    elif (movedLocation in routeHistory):
        return False
    else:
        correctRoute.append(movedLocation)
        routeHistory.append(movedLocation)
        return True

def goDown():

    location = correctRoute[len(correctRoute)-1]
    movedLocation = [location[0]+1, location[1]]

    if (location[0] == 11):
        return False
    elif (maze[location[0]+1][location[1]] == 1):
        return False
    elif (movedLocation in routeHistory):
        return False
    else:
        correctRoute.append(movedLocation)
        routeHistory.append(movedLocation)
        return True

def goLeft():

    location = correctRoute[len(correctRoute)-1]
    movedLocation = [location[0], location[1]-1]

    if (location[1] == 0):
        return False
    elif (maze[location[0]][location[1]-1] == 1):
        return False
    elif (movedLocation in routeHistory):
        return False
    else:
        correctRoute.append(movedLocation)
        routeHistory.append(movedLocation)
        return True

def exploring():
    location = correctRoute[len(correctRoute)-1]

    if (goUp() == False):   # When we check whether it is false, it seems that python would run this code of line automatically.
        if (goDown() == False):
            if (goRight() == False):
                if (goLeft() == False):
                    correctRoute.pop()  # To prevent the problem of blind alley.

    correctRouteLocationX = correctRoute[len(correctRoute)-1]   # Latest location
    if (correctRouteLocationX[1] < 9):  # If you did not find the exit which located on the right & bottom side of the maze, keep searching it.
        exploring()


exploring()
print("The the ordinates of each point in the route were shown below:")
print(correctRoute)
