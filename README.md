# COMPSCI130ConnectFour
COMPSCI130 Semester 2 2022 Assignment: Connect 4 Python Game

Connect4 game with implemented Computer AI (implementing minimax algorithm)

To enhance the AI's decision-making capabilities, I devised a scoring framework centered on identifying patterns of 2-in-a-row, 3-in-a-row, and 4-in-a-row moves. This scoring system serves a dual purpose, as it accounts for both the AI's and the opponent's achievements in these patterns.

Here's how moves are assigned scores:

Any move that results in a four-in-a-row for the AI: Earns 1000 points.  
Any move that leads to a three-in-a-row for the AI: Earns 5 points.  
Any move that establishes a 2-in-a-row for the AI: Earns 2 points.  
Any move by the opponent that forms a four-in-a-row: Deducts 1000 points.  
Any move by the opponent resulting in a three-in-a-row: Deducts 100 points.  
Any move by the opponent that leads to a two-in-a-row: Deducts 2 points.  
It's important to note that this scoring mechanism considers the entire game board, encompassing all past occurrences of 2-in-a-row, 3-in-a-row, and 4-in-a-row, rather than focusing solely on the most recent move.  

The Minimax Algorithm Functions:  
My Minimax algorithm relies on two core functions:

choose_move(self, player): This function serves a dual role: firstly, it triggers the Minimax algorithm, and secondly, it identifies and returns the column of the optimal move to make. This decision is made by evaluating all possible moves up to three turns ahead.

choose_move_for_minimax_points(self, player_to_play, player_to_evaluate, should_maximize, depth): This function embodies the Minimax algorithm's recursive logic. It continually calls itself to explore all potential game states, up to a depth of three moves ahead, and returns the points and corresponding move location for the best possible move each time. To ensure that the board's state remains unchanged during this process, I've introduced an auxiliary function called copy(self) to replicate the board. This way, each recursive move is executed on a copied version of the board, preserving the original state for display purposes without modification.
