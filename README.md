# Pacman-search-algorithms
## About :thought_balloon:
My contribution for this project can be found in the following classes: search.py, node.py, searchAgents.py. Using the framework given I implemented some search algorithms, such as: DFS, BFS, Dijkstra, A* with various heuristics.
## Features :white_check_mark:
- Pacman will find all the food in every case.
- Optimal heuristics for finding the food.
- Nice visualization of the algorithms.
- Posibility of comparison between the number of expanded states for each algorithm.
## Implementation and visualization :computer:
### Notable implementation details:
- BFS and DFS implemented iteratively using a queue respectively a stack.
- Dijkstra implemented using a priority queue.
- My heuristic for the A* algorithm where pacman had to eat all the food is based on a preprocessing of the maze where all the distances were saved in a matrix like structure. This heurisitc was rewarded with extra credit 5/4 points from the autograder.
### Depth first search (DFS)
![DFS](https://user-images.githubusercontent.com/63104735/222981178-53a4bf27-40c0-47d0-b6e7-263520e56f68.PNG)
### Breadth first search (BFS)
![BFS](https://user-images.githubusercontent.com/63104735/222981180-3559405e-e78b-49e3-a8b6-9f47abe33a20.PNG)
### Dijkstra
![Dijsktra](https://user-images.githubusercontent.com/63104735/222981184-5fa2cfe4-9608-474a-bac3-327df96a6501.PNG)
### A* 
![A star](https://user-images.githubusercontent.com/63104735/222981186-136b938f-92ac-4c31-a119-9f3a15c28319.PNG)
