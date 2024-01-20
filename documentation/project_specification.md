## Project Specification

The goal of the project is to implement an algorithm that can play [https://en.wikipedia.org/wiki/Connect_Four](Connect 4). The user will be able to select the depth or the time-limit of the algortihm to tune the difficulty. The user will also be able to let different versions of the algorithm play against eachother repeatedly, so that the results of the optimisations can be seen. The same algorithm can also be compared to itself with a different time-limit or depth, so that the tradeoff between execution-time and strength can be compared.

The program is implemented in Python. I can review a program written in Java as well. The code, comments and documentation are written in English, but I am also able to review projects written in Finnish.  

This project implements the [https://en.wikipedia.org/wiki/Minimax](minimax algorithm) on the Connect 4 game. The goal of the project is to optimise the minimax algorithm using different methods, such as:
- Organising the order of calculation to find the optimal choice more quickly
- Iterative deepening with a time limit
- Use of a hashmap to store the results of previous runs during the same move 

Depending on how quickly the project progresses additional optimisations might be implemented. The minimax algorithm is chosen as it is an easy algorithm to implement, which shifts the focus more towards the optimisation of the algorithm rather than its implementation. 

The program will run in a terminal. The user will be able to select the algorithms and its time-limit or depth, and the amount of times the algorithms play against eachother. The program will display how many times each algorithm won, and how much time each algorithm ran.

I am in the tietojenkäsittelytieteen kandidaatti (TKT) programme.
