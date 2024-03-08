## Implementation

The program uses the minimax algorithm to decide what move to play. The minimax algorithm has a time complexity of O(m^d), where m is the amount of possible moves and d is the depth that the algorithm calculates to.

The heuristic function called by the algorithm looks for how many sequences there with three of the same player and one empty slot. It does not take into account whether the empty slot can be played immediately or only in many turns.

Alpha-beta pruning was used to optimise this algorithm. With alpha-beta pruning, the time complexity in the worst case stays the same, and in the best case becomes O(sqrt(m^d)).

To fasten up the program, it is desirable to have good games be anaylsed first, so that bad ones can be pruned and not calculated. Each time a game situation has been analysed, it is saved. If the same situation has already been analysed, the move with the best score is ran first, as if a move is worse there is a higher chance it will be pruned.
On top of this iterative deepening was used. This increases the information about the possible moves, and thus increases the pruning even more.

The project could be improved by allowing the user to change the difficulty without having to modify the code, and by having a clearer way on how to select columns and maybe a nicer looking board too. 

Large language models were used for information retrieval about the minimax algorithm. Large language models have not been used to generate or correct code.

Source for the best case time complexity with alpha beta pruning: [wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
