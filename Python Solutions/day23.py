import queue

# Gloabal variables
inputGrid = [
    ['f','f','f','f'],
    ['t','t','f','t'],
    ['f','f','f','f'],
    ['f','f','f','f']
]

start = (3,0)
end = (0,0)
numRows = len(inputGrid)
numCols = len(inputGrid[0])

# Variables to keep track of the number of steps taken
moveCount = 0
nodeLeftInLayer = 1
nodeInNextLayer = 0

# Variable used of track whether the "E" character ever gets reached uring BFS
global reachedEnd 
reachedEnd = False
visitedMatrix = [[False] * numCols ] * numRows

rq = queue.Queue(numRows * numCols)
cq = queue.Queue(numRows * numCols)

def explore(row, col):
    rd = [-1, 0, 1, 0]
    cd = [0, 1, 0, -1]

    for i in range(4):
        
        rr = row + rd[i]
        cc = col + cd[i]

        # checking if neighbour is out of boundaries
        if rr < 0 or rr >= numRows: continue
        if cc < 0 or cc >= numCols: continue

        # checking if neighbour is already visited, or an obstacle
        if visitedMatrix[rr][cc] == True: continue
        if inputGrid[rr][cc] == 't': continue

        # add elements to row and col queues
        rq.put(rr)
        cq.put(cc)
        visitedMatrix[rr][cc] = True
        nodeInNextLayer += 1


def findShortestPath(startNode, endNode):
    rq.put(startNode[0])
    cq.put(startNode[1])
    visitedMatrix[startNode[0]][startNode[1]] = True

    while not rq.empty:
        r = rq.get()
        c = rq.get()
        if r == endNode[0] and c == endNode[1]:
            reachedEnd = True
            break
        explore(r, c)
        nodeLeftInLayer -= 1
        if nodeLeftInLayer == 0:
            nodeLeftInLayer = nodeInNextLayer
            nodeInNextLayer = 0
            moveCount += 1

    if reachedEnd == True:
        return moveCount
    return -1


if __name__ == "__main__":
    findShortestPath(start, end)


