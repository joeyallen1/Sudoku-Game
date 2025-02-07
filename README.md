# Sudoku Game

A simple interactive Sudoku game built using Python and Pygame, where users can generate and solve randomized Sudoku puzzles.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Controls](#controls)
5. [License](#license)

## Features
- Generates randomized Sudoku puzzles with a single, unique solution using backtracking and recursion
- Allows users to input numbers to solve the puzzle using a GUI
- Clear board functionality to remove user inputs  
- "New Game" button to generate fresh puzzles  
- Timer display to track puzzle-solving time  

## Installation
To get started with the Sudoku game, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:joeyallen1/Sudoku-Game.git
2. Navigate to the Project Directory
   ```bash
   cd "Sudoku Game"
3. Install Dependencies
   ```bash
   pip install pygame numpy
4. Run the Game
   ```bash
   python Sudoku.py

## Usage
Once the game starts, a randomly generated Sudoku puzzle will appear on the screen. Use the mouse to select cells and input numbers to solve the puzzle. Correct guesses will appear in blue and incorrect guesses will appear in red.

You can also clear the board, generate new puzzles, and press the finish button to freeze the timer.

## Controls
- Input Numbers: Click on a blank square and press any number key (1-9) to fill it in.
- Clear Board: Click the "Clear Board" button to remove all user-inputted numbers.
- New Game: Click the "New Game" button to generate a fresh puzzle.
- Finish: Click the "Finish!" button to check the puzzle and stop the timer.

Enjoy the game!
