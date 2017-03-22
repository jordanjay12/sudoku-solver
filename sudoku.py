# Creating the minimal encoding rules for SAT Solver
#
#
# Last Date Modified : Mar.21.2017


# Each cell should contain at least one number
def cell_atleast_one():
  result = []
  for i in range(1, 10):
    for j in range(1, 10):
      for k in range(1, 10):
        result.append("{}{}{} ".format(i,j,k))
      print("".join(result) + "0")
      result = []

# Each number appears at most once in every row
def row_atmost_once():
  for i in range(1, 10):
    for k in range(1, 10):
      for j in range(1, 9):
        for l in range(j+1, 10):
          print("-{}{}{} -{}{}{} 0".format(i,j,k,i,l,k))

# Each number appears at most once in every column
def col_atmost_once():
  for j in range(1, 10):
    for k in range(1, 10):
      for i in range(1,9):
        for l in range(i+1, 10):
          print("-{}{}{} -{}{}{} 0".format(i,j,k,l,j,k))

# Each number appears at most once in every 3x3 subgrid
def three_square_atmost_once():
  for k in range(1, 10):
    for a in range(0, 3):
      for b in range(0, 3):
        for u in range(1, 4):
          for v in range(1, 3):
            for w in range(v+1, 4):
              print("-{}{}{} -{}{}{} 0".format((3*a+u), (3*b+v), k, (3*a+u), (3*b+w), k))

  for k in range(1, 10):
    for a in range(0, 3):
      for b in range(0, 3):
        for u in range(1, 3):
          for v in range(1, 4):
            for w in range(u+1, 4):
              for t in range(1, 4):
                print("-{}{}{} -{}{}{} 0".format((3*a+u), (3*b+v), k, (3*a+w), (3*b+t), k))

def main():
  cell_atleast_one()
  row_atmost_once()
  col_atmost_once()
  three_square_atmost_once()

if __name__ == '__main__':
  main()