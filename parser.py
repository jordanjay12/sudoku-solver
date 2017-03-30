# parser idea

import sys


def main():
  n = sys.argv[1]
  j = 0

  file_name = "grids.txt"
  
  in_f = open(file_name, 'r')

  data = in_f.read().split()

  while (data):
    data.pop(0)
    data.pop(0)
    i = 9
    out_file_name = "test_file{}.txt".format(j)
    out_f = open(out_file_name, 'w+')
    while (i >0):
      out_f.write(data.pop(0) + "\n")
      i -= 1
    j += 1





if __name__ == '__main__':
  main()