#CSC320 Sudoku Solver Project

The project involves writing a simple program to translate partially solved Sudoku puzzle into CNF formulas such that the CNF is satisfiable iff the puzzle has a solution.

###Basic Task

+ sud2sat reads a Sudoku puzzle and converts it to a CNF formula (DIMACS format) which will be used by miniSAT SAT solver. 
+ sat2sud reads the output of miniSAT for a given puzzle instance and converts it back into a solved Sudoku puzzle.

...
