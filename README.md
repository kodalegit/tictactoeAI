# TictactoeAI
Minimax algorithm to solve adversarial search problem implemented in tictactoe

## Background
Tic-tac-toe is a game that involves two adversarial agents trying to get three consecutive moves vertically, horizontally or diagonally. In this program, an AI model recursively uses the minimax algorithm to determine the best possible move in any game state.

## Description
The AI model takes the current board as input and returns the most optimal move by recursively applying the minimax algorithm. Player 0 is visualized to have the minimum utility, -1, player X is visualized to have the maximum utility 1 and a draw is visualized as a utility of 0. For any given state, the maximizing player attempts to produce the highest value of the minimum values of the state while the minimizing player attempts to produce the lowest value of the maximum values of the state. This process is repeated recursively to find the most optimal move for the agent.

## Getting Started
The program is run using the command-line argument `python runner.py`
