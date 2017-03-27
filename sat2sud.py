import sys

def read_file():
  file = str(sys.argv[1])
  f = open(file, 'r')
  solution = f.read().split()
  result = []
  for symbol in solution:
  	result.append(symbol)
  	#Everything is now being stored in result list
  satisfiable = result.pop(0)  #getting rid of the first element
  
  if(satisfiable == 'UNSATISFIABLE'):
  	print("The given puzzle is not satisfiable")
  	return
  else:
  	print("The given puzzle is satisfiable")

  solved_board = []
  for element in result:
  	if(int(element) > 0):
  		solved_board.append(element)
  #print("The board should only contain positive values now")
  #print(solved_board)


  # final_solution now contains the specific values for the sudoku puzzle, format later to look like a solve puzzle
  final_solution = []
  for element in solved_board:
  	i = (int(element)/81) +1
  	j = (int(element)/9) +1
  	k = (int(element)%9)
  	if k == 0:
  		k = 9
  	final_solution.append(k)

  print(final_solution)


def main():
	read_file()

if __name__ == '__main__':
  main()