# --------------------------------------------------
# extended_parser.py
#
# parser for extended task to solve harder challenges
# found at http://magictour.free.fr/top95
#
# it reads each puzzles in the grids.txt into 
# seperate test_file0.txt, test_file1.txt, ...
#
# Author: jiinmoon
# Last modified: Mar.30 2017
# --------------------------------------------------

def main():

  file_name = "hard_puzzles.txt"
  in_f = open(file_name, 'r')
  in_data = in_f.read().strip().split()

  k = 0
  j = 9

  for puzzle in in_data:
    out_file_name = "test_file{}.txt".format(k)
    out_f = open(out_file_name, 'w+')
    result = [puzzle[i:i+j] for i in range(0, len(puzzle), j)]
    for line in result:
      out_f.write(line + "\n")
    k += 1

if __name__ == '__main__':
  main()