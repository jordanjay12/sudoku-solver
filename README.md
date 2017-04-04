# CSC320 Sudoku Solver Project

**Introduction**

The project involves writing a simple program to translate partially solved Sudoku puzzle into CNF formulas such that the CNF is satisfiable iff the puzzle has a solution. The project is written in python3, and is to be used with either miniSAT or Gsat. (For more information about the SAT Solvers, visit [link](http://www.cs.ubc.ca/~hoos/SATLIB/index-ubc.html)).

**Contents**

+ sud2sat reads the sudoku puzzle and converts it to CNF formula (DIMACS format). 
+ sat2sud reads the output of SAT solver for a given puzzle, and converts it back into the sudoku puzzle.
+ grid_parser - parses the basic task puzzles into separate test files for shell script testing.
+ extended_parser - parses the extended "hard" task puzzles into separate test files for shell script testing.
+ input.sh - shell script for testing the basic task
+ extended_input.sh - shell script for testing extended task (1) - "hard" puzzles

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

usage: python3 sat2sud.py <file_name> [-gsat | -minisat]

+ Input: computed result file of sudoku puzzle SAT problem from either minisat or gsat.
+ Output: solved human-readable sudoku puzzle.

**How to**

Following shows the example of how to use these program:

With miniSAT:

1. Create valid sudoku_puzzle_file. Suppose its name is "test_file.txt"
2. Use sud2sat.py to generate the satisfying assignment. This is done in terminal by typing "python3 sat2sud.py test_file.txt -minisat -extended=false > input.in".
3. Confirm that input.in has been created which should contain CNF formulas for the given sudoku puzzle.
4. Use miniSAT to solve the satisfiability. This is done in terminal by typing "./minisat_release input.in output.out"
5. By doing so, it will show stastics on the given problem, and output in "output.out" file.
6. To convert the output into human readable form, we need to use sat2sud.py.
7. Use sat2sud.py to convert output from miniSAT. This is done in terminal by typing "python3 sud2sat.py output.out -minisat".
8. The result should be on terminal.

With GSAT:

1. Create valid sudoku_puzzle_file following the input format specificed above. Suppose its name is "test_file.txt"
2. Use sud2say.py to generate the satisfying assignment. This is done in terminal by typing "python3 sat2sud.py test_file.txt -gsat - extended=false > input.in"
3. Confirm that input.in has been created which should contain CNF formulas for the given sudoku puzzle that would be acceptable for GSAT Solver.
4. Use GSAT to solve the satisfiability. It should give two output files, but first file is the one we will use as second file simply contains statistics.
5. By doing so, GSAT should return the best-fit model. Suppose the generated output file is named "output.out".
6. To convert this output file into human readable format, we need to use sat2sud.py.
7. Use sat2sud.py to convert "output.out" from GSAT. This is done so in terminal by typing "python3 sud2say.py output.out -gsat".
8. The result should be on terminal.

### Contributions

Jordan Jay, Ji-In Moon, Andrew Eng, Tyler Luo Dai
