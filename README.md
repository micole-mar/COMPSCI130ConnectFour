# COMPSCI130ConnectFour
COMPSCI130 Semester 2 2022 Assignment: Connect 4 Python Game

Connect4 game with implemented Computer AI (implementing minimax algorithm)

To enhance the AI's decision-making capabilities, I devised a scoring framework centered on identifying patterns of 2-in-a-row, 3-in-a-row, and 4-in-a-row moves. This scoring system serves a dual purpose, as it accounts for both the AI's and the opponent's achievements in these patterns.

Here's how moves are assigned scores:

Any move that results in a four-in-a-row for the AI: Earns 1000 points.  
Any move that leads to a three-in-a-row for the AI: Gains 5 points.  
Any move that establishes a 2-in-a-row for the AI: Accumulates 2 points.  
Any move by the opponent that forms a four-in-a-row: Deducts 1000 points.  
Any move by the opponent resulting in a three-in-a-row: Subtracts 100 points.  
Any move by the opponent that leads to a two-in-a-row: Incurs a penalty of 2 points.  
It's important to note that this scoring mechanism considers the entire game board, encompassing all past occurrences of 2-in-a-row, 3-in-a-row, and 4-in-a-row, rather than focusing solely on the most recent move.  

