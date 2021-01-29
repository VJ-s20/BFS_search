

class BFS:
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
        maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
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
        i = start
        j = 0
        pos = set()
        for move in path:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            pos.add((j, i))
        for i, row in enumerate(maze):
            for j, col in enumerate(row):
                if maze[i][j]=="#" and i==0:
                    col="_"
                if maze[i][j]=="#" and i==len(maze)-1:
                    col="‾"
                if (i, j) in pos:
                    print("+", end=" ")
                else:
                    print(col+"", end=" ")
            print()


    def findend(self,maze, moves):
        for index, pos in enumerate(maze[0]):
            if pos == "O":
                start = index
        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
        if maze[j][i] == "X":
            print("Found:", moves)
            self.printMaze(maze, moves)
            return True
        return False


    def valid(self,maze, moves):
        for index, pos in enumerate(maze[0]):
            if pos == "O":
                start = index
        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
                return False
            elif maze[j][i] == "#":
                return False
        return True


# ** Main Algorithm
def main():
    bfs=BFS()
    queue = [""]
    moves = ""
    maze = bfs.createMaze()
    while not bfs.findend(maze, moves):
        moves = queue.pop(0)
        for i in ["L", "R", "U", "D"]:
            move = moves+i
            if bfs.valid(maze, move):
                queue.append(move)

if __name__=="__main__":
    main()


# ‾
