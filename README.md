# Maze Searching
>Using searching algorithms BFS and DFS for finding the path between start and end of the maze  
* Untraversed Maze  

```
Maze1  
# # # # # O #      
#       #   #        O is the Start of the maze  
#   #   #   #        X is the End of the maze
#   #       #  
#   # # #   #  
#       # # #         
# X # # # # # 



* Maze2  

# # # # # O # # #  
#               #  
#   # #   # #   #  
#   #       #   #  
#   #   #   #   #  
#   #   #   #   #
#   #   #   # # #    
#               #  
# # # # # # # X #    
```
* Solution Using Breadth first search(BFS):


```
Maze 1
Path: DDDLLDDLLD

#  #  #  #  #  O  #  
#           #  +  #  
#     #     #  +  #  
#     #  +  +  +  #  
#     #  +  #     #  
#  +  +  +  #  #  #  
#  +  #  #  #  #  # 

Maze 2
Path: DLDDRDDDDRRD      

#  #  #  #  #  O  #  #  #  
#           +  +        #  
#     #  #  +  #  #     #  
#     #     +  +  #     #  
#     #     #  +  #     #  
#     #     #  +  #     #  
#     #     #  +  #  #  #  
#              +  +  +  #  
#  #  #  #  #  #  #  +  #  

```

* Solution Using Defth first search(DFS):


```
Maze 1
Path: DDDLLUULLDDDDD

#  #  #  #  #  O  #  
#  +  +  +  #  +  #  
#  +  #  +  #  +  #  
#  +  #  +  +  +  #  
#  +  #     #     #  
#  +        #  #  #  
#  +  #  #  #  #  #  

Maze 2
Path: DLLLLDDDDDDRRRRRRD

#  #  #  #  #  O  #  #  #  
#  +  +  +  +  +        #
#  +  #  #     #  #     #
#  +  #           #     #
#  +  #     #     #     #
#  +  #     #     #     #
#  +  #     #     #  #  #
#  +  +  +  +  +  +  +  #
#  #  #  #  #  #  #  +  #
```