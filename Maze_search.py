

class Maze:
    def createMaze(self):
        maze = []
        maze.append(["#", "#", "#", "#", "#", "O", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", "#", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

        return maze


    def createMaze2(self):
        maze = []
        maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])
        return maze

    def printMaze(self,maze, path=""):
        for index, pos in enumerate(maze[0]):
            if pos == "O":
                start = index
                break
        i = start
        j = 0
        pos = set()
        for move in path:
            j,i=self.path(move,i,j)
            pos.add((j, i))
        for i, row in enumerate(maze):
            for j, col in enumerate(row):
                if (i, j) in pos:
                    print("+", end="  ")
                else:
                    print(col+"", end="  ")
            print()

    def path(self,move,i,j):
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        return (j,i)
    
    def valid(self,maze, moves):
        for index, pos in enumerate(maze[0]):
            if pos == "O":
                start = index
                break
        i = start
        j = 0
        pos=set()  #* To keep track of previous traversed pos
        for move in moves:
            j,i=self.path(move,i,j)
            if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
                return False
            if (j,i) in pos:
                return False
            elif maze[j][i] == "#":
                return False
            pos.add((j,i))
        return True

    def findend(self,maze, moves):
        for index, pos in enumerate(maze[0]):
            if pos == "O":
                start = index
                break
        i = start
        j = 0
        for move in moves:
            j,i=self.path(move,i,j)
        if maze[j][i] == "X":
            print("Found:", moves)
            self.printMaze(maze, moves)
            return True
        return False

#**  Main Algorithm's
#* BFS 
def BFS(bfs):
    queue = [""]
    moves = ""
    maze = bfs.createMaze2()
    while not bfs.findend(maze, moves):
        moves = queue.pop(0)
        for i in ["L", "R", "U", "D"]:
            move = moves+i
            if bfs.valid(maze, move):
                queue.append(move)

#* DFS using stack
def dfs(traversal,moves):
    stack=[moves]
    maze=traversal.createMaze2()
    while not (traversal.findend(maze,moves)):
        moves=stack.pop()
        for i in ["L", "R", "U", "D"]:
            move=moves+i
            if traversal.valid(maze,move):
                stack.append(move)
# * DFS Using Recursion
def _dfs(traversal,maze,moves):
    if traversal.findend(maze,moves):
        exit()
    else:
        for i in ["L", "R", "U", "D"]:
            move=moves+i
            if traversal.valid(maze,move) :  
                _dfs(traversal,maze,move) #! Solved Infinity recursion 

def dfs_recursion(traversal):
    maze=traversal.createMaze2()
    return _dfs(traversal,maze,"")


if __name__=="__main__":
    search=Maze()
    BFS(search)
    dfs(search,"")
    # dfs_recursion(search)

