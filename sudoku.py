# Creating the minimal encoding rules for SAT Solver
#
#
# Last Date Modified : Mar.27.2017

import sys

# Read Sudoku file from standard in
exceptions = ['0', '.', '*', '?', "\n"]

def read_puzzle():
  # First terminal input is file name
  file = str(sys.argv[1])
  result = []

  f = open(file, 'r')

  count = 0
  row = 1
  col = 1

  puzzle = f.read().replace("\n", "")
  for symbol in puzzle:
    if col == 10:
      row += 1
      col = 1

    if symbol not in exceptions:
      input_num = 81*(int(row)-1) + 9*(int(col)-1) + (int(symbol)-1) + 1
      result.append(str(input_num) + " 0")
      #result.append(str(row)+ str(col) + symbol + " 0")
      count += 1

    col += 1

  #This total clauses is dependent on using the minimal encoding
  total_clauses = 8829 + count
  

  print("p cnf " + str(729) + " " + str(total_clauses))
  for i in result:
    print(i)

# Each cell should contain at least one number
def cell_atleast_one():
  #print("p cnf 729 81")
  result = []
  for i in range(1, 10):
    for j in range(1, 10):
      for k in range(1, 10):
        input_num = 81*(i-1) + 9*(j-1) + (k-1) + 1
        result.append("{} ".format(input_num))
      print("".join(result) + "0")
      result = []

# Each number appears at most once in every row
def row_atmost_once():
  #print("p cnf 729 2916")
  for i in range(1, 10):
    for k in range(1, 10):
      for j in range(1, 9):
        for l in range(j+1, 10):
          first_num = 81*(i-1) + 9*(j-1) + (k-1) + 1
          second_num = 81*(i-1) + 9*(l-1) + (k-1) + 1
          #print("-{}{}{} -{}{}{} 0".format(i,j,k,i,l,k))
          print("-{} -{} 0".format(first_num, second_num))

# Each number appears at most once in every column
def col_atmost_once():
  #print("p cnf 729 2916")
  for j in range(1, 10):
    for k in range(1, 10):
      for i in range(1,9):
        for l in range(i+1, 10):
          first_num = 81*(i-1) + 9*(j-1) + (k-1) + 1
          second_num = 81*(l-1) + 9*(j-1) + (k-1) +1 
          #print("-{}{}{} -{}{}{} 0".format(i,j,k,l,j,k))
          print("-{} -{} 0".format(first_num, second_num))

# Each number appears at most once in every 3x3 subgrid
def three_square_atmost_once():
  #print("p cnf 729 2916")
  for k in range(1, 10):
    for a in range(0, 3):
      for b in range(0, 3):
        for u in range(1, 4):
          for v in range(1, 3):
            for w in range(v+1, 4):
              first_num = 81*((3*a+u)-1) + 9*((3*b+v)-1) + (k-1) +1 
              second_num = 81*((3*a+u)-1) + 9*((3*b+w) -1) + (k-1) + 1
              #print("-{}{}{} -{}{}{} 0".format((3*a+u), (3*b+v), k, (3*a+u), (3*b+w), k))
              print("-{} -{} 0".format(first_num, second_num))

  for k in range(1, 10):
    for a in range(0, 3):
      for b in range(0, 3):
        for u in range(1, 3):
          for v in range(1, 4):
            for w in range(u+1, 4):
              for t in range(1, 4):
                first_num = 81*((3*a+u)-1) + 9*((3*b+v)-1) + (k-1) +1 
                second_num = 81*((3*a+w)-1) + 9*((3*b+t) -1) + (k-1) + 1
                #print("-{}{}{} -{}{}{} 0".format((3*a+u), (3*b+v), k, (3*a+w), (3*b+t), k))
                print("-{} -{} 0".format(first_num, second_num))


# *************************************************
# The functions below are for the extended encoding
# The extended encoding explicity asserts that each 
# entry in the grid has exactly one number
# *************************************************

# There is at most one number in each entry
def cell_atmost_once():
  print("p cnf 729 2916")
  for x in range(1, 10):
    for y in range(1,10):
      for z in range(1,9):
        for i in range(z+1, 10):
          first_num = 81*(x-1) + 9*(y-1) + (z-1) + 1
          second_num = 81*(x-1) + 9*(y-1) + (i-1) + 1
          print("-{} -{} 0".format(first_num, second_num))

# Each number appears at least once in each row
def row_atleast_once():
  print("p cnf 729 81")
  result = []
  for y in range(1,10):
    for z in range(1,10):
      for x in range(1,10):
        input_num = 81*(x-1) + 9*(y-1) + (z-1) + 1
        result.append("{} ".format(input_num))
      print("".join(result) + "0")
      result = []


# Each number appears at least once in each column
def col_atleast_once():
  print("p cnf 729 81")
  result = []
  for x in range(1, 10):
    for z in range(1, 10):
      for y in range(1, 10):
        input_num = 81*(x-1) + 9*(y-1) + (z-1) + 1
        result.append("{} ".format(input_num))
      print("".join(result) + "0")
      result = []        


# Each number appears at last once in each 3x3 sub-grid
def three_square_atleast_once():
  print("p cnf 729 81")
  result = []
  for z in range(1, 10):
    for i in range(0, 3):
      for j in range(0, 3):
        for x in range(1, 4):
          for y in range(1, 4):
            input_num = 81*((3*i+x)-1) + 9*((3*j+y)-1) + (z-1) + 1
            result.append("{} ".format(input_num))
        # here it doesn't seem to follow the pdf, but only way to make nine-ary clauses
        print("".join(result) + "0")
        result = []          



def main():
  read_puzzle()
  cell_atleast_one()
  row_atmost_once()
  col_atmost_once()
  three_square_atmost_once()


  # The functions below are called for the extended encoding
  # They are unnecessary for solving sudoku problems, as the minimal encoding works

  #cell_atmost_once()
  #row_atleast_once()
  #col_atleast_once()
  #three_square_atleast_once()

if __name__ == '__main__':
  main()