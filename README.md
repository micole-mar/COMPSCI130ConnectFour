# COMPSCI130ConnectFour
COMPSCI130 Semester 2 2022 Assignment: Connect 4 Python Game

Connect4 game with implemented Computer AI (implementing minimax algorithm)

To enhance the AI's decision-making capabilities, I devised a scoring framework centered on identifying patterns of 4-in-a-row moves. This scoring system serves a dual purpose, as it accounts for both the AI's and the opponent's achievements in these patterns.

It's important to note that this scoring mechanism considers the entire game board, encompassing all past occurrences of 4-in-a-row, rather than focusing solely on the most recent move.  

AI player:

Maximise Points: The AI player aims to maximize its own points. It evaluates the current game board and tries to make moves that result in the AI player earning more points.

Minimise Opponent's Points: If there are no immediate moves that would increase the AI player's points, the AI player checks if the opponent (Player 1) has any moves that could result in them earning a large number of points. In this case, the AI tries to block the opponent's potential wins.

Fallback to Center Columns: If there are no moves that maximize points or block the opponent, the AI player chooses columns that are as close to the center of the board as possible. This is a heuristic to select potentially strategic columns.

Simple Evaluation: The AI player doesn't perform an in-depth evaluation of game states, nor does it consider future moves beyond the current turn. It makes decisions based on the current state of the board and the heuristic rules mentioned above.

Skills:  
- Object-Oriented Programming (OOP): The code is organized into classes (GameBoard and FourInARow) to encapsulate game logic and behavior, demonstrating an understanding of OOP principles.
- Game Logic Implementation: The project involves implementing the rules and logic of the Connect Four game, including win conditions, turns, and game state management.
- User Input Handling: The code captures and validates user input, ensuring that players can interact with the game by choosing columns for their moves.
- AI Decision-Making: Although it uses a heuristic-based approach rather than a complex AI algorithm, the code demonstrates the implementation of a basic AI opponent that can make decisions based on simple rules.
- Looping and Control Structures: The game loop controls the flow of the game, allowing players to take turns and checking for game-over conditions.
- Data Structures: Lists and nested lists are used to represent the game board and manage the state of the game.
- Conditional Statements: Conditional statements are employed throughout the code for various game logic purposes, including checking for wins, determining AI moves, and validating user input.
- Error Handling: Basic error handling is implemented to manage potential issues, such as invalid user input or board operations.
- Lists and Indexing: Lists are used extensively to manage the game board and track the state of each column.
- Math Operations: Mathematical operations are used to calculate the number of free positions, points, and determine the center of the game board.
- User Interaction: The code interacts with users by displaying messages, requesting input, and providing feedback on the game's progress.
- Heuristic-Based Decision-Making: The AI's heuristic-based decision-making demonstrates an understanding of creating basic strategies for game opponents.
- Print and Display: The code includes a mechanism to print and display the game board, allowing players to visualize the game's state.
