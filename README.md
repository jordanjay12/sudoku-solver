# CSC320 Sudoku Solver Project

**Introduction**

The project involves writing a simple program to translate partially solved Sudoku puzzle into CNF formulas such that the CNF is satisfiable iff the puzzle has a solution. The project is written in python3, and is to be used with either miniSAT or Gsat. (For more information about the SAT Solvers, visit [link](http://www.cs.ubc.ca/~hoos/SATLIB/index-ubc.html)).

**Contents**

+ sud2sat reads the sudoku puzzle and converts it to CNF formula (DIMACS format). 
+ sat2sud reads the output of SAT solver for a given puzzle, and converts it back into the sudoku puzzle.

**sud2sat.py**

usage: python3 sud2sat.py <file_name> [-gsat | -minisat] -extended=[true | false]

+ Input: sudoku_puzzle_file.
+ Output: CNF formulas ready to be solved by either miniSAT or gsat.

The valid sudoku_puzzle_file has a following format:

```
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
```

The empty cells can be indicated by either '0', '.', '*', or '?' symbols.

**sat2sud.py**

+ Input: computed result file of sudoku puzzle SAT problem.
+ Output: solved human-readable sudoku puzzle.

--- Work in Progress ---
--- miniSAT conversion works. Gsat incoming. ---

### Contributions

jordanjay12, jiinmoon
