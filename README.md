# Maze Searching
Using searching algorithms BFS and DFS for finding the path between start and end of the maze

* Untraversed Maze
Maze1
# # # # # O #    
#       #   #        O is the Start of the maze
#   #   #   #        X is the End of the maze
#   #       #
#   # # #   #
#       # # #       
# X # # # # #
Maze2
# # # # # O # # #
#               #
#   # #   # #   #
#   #       #   #
#   #   #   #   #
#   #   #   #   #
#   #   #   # # #
#               #
# # # # # # # X #

* Solution Using Breadth first search(BFS) to find the path between start and end
Maze 1
Found: DDDLLDDLLD
#  #  #  #  #  O  #  
#           #  +  #  
#     #     #  +  #  
#     #  +  +  +  #  
#     #  +  #     #  
#  +  +  +  #  #  #  
#  +  #  #  #  #  # 
Maze 2
Found: DLDDRDDDDRRD        
#  #  #  #  #  O  #  #  #  
#           +  +        #  
#     #  #  +  #  #     #  
#     #     +  +  #     #  
#     #     #  +  #     #  
#     #     #  +  #     #  
#     #     #  +  #  #  #  
#              +  +  +  #  
#  #  #  #  #  #  #  +  #  
* Solution Using Defth first search(DFS) to find the path between start and end
Maze 1
Found: DDDLLUULLDDDDD
#  #  #  #  #  O  #  
#  +  +  +  #  +  #  
#  +  #  +  #  +  #  
#  +  #  +  +  +  #  
#  +  #     #     #  
#  +        #  #  #  
#  +  #  #  #  #  #  
Maze 2
Found: DLLLLDDDDDDRRRRRRD
#  #  #  #  #  O  #  #  #  
#  +  +  +  +  +        #
#  +  #  #     #  #     #
#  +  #           #     #
#  +  #     #     #     #
#  +  #     #     #     #
#  +  #     #     #  #  #
#  +  +  +  +  +  +  +  #
#  #  #  #  #  #  #  +  #
