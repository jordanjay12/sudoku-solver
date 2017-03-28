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

  # Getting rid of all values that are not greater than zero
  solved_board = []
  for element in result:
  	if(int(element) > 0):
  		solved_board.append(element)

  # final_solution now contains the specific values for the sudoku puzzle, format later to look like a solved puzzle
  final_solution = []
  for element in solved_board:
  	i = (int(element)/81) +1
  	j = (int(element)/9) +1
  	k = (int(element)%9)
  	if k == 0:
  		k = 9
  	final_solution.append(k)

  # Formatting the output to be printed as a Sudoku board
  col = 0
  row = 0
  for cell in final_solution:
  	col += 1
  	print str(cell),
  	if(col == 3 or col == 6):
  		print"|",
  	if(col == 9):
  		col = 0
  		row +=1
  		print
  		if(row == 3 or row == 6):
  			print "- - - - - - - - - - -"


def main():
	read_file()

if __name__ == '__main__':
  main()