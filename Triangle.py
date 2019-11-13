#  File: Triangle.py

#  Description: This program will use four different algorithms to determine the largest sum path in a
#   given triangle.

#  Student's Name: Basilio Bazan

#  Student's UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/01/2018

#  Date Last Modified: 11/02/2018

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force(grid):
    size = len(grid)
    max = 0

    #creates all possible path sets with indexes to be used in finding the largest sum path
    all_paths = [[0]]
    for i in range(1, size+1):
        new_path = []
        for x in all_paths:
            a = x[-1]
            path_1 = x[:]
            path_1.append(a)
            path_2 = x[:]
            path_2.append(a+1)

            new_path.append(path_1)
            new_path.append(path_2)
        all_paths = new_path

    #Generates the sum of each path then check if it is the current max.
    for path in all_paths:
        sum = 0
        for i in range(size):
            value = int(grid[i][path[i]])
            sum += value

        if sum > max:
            max = sum

    return max

# returns the greatest path sum using greedy approach
def greedy(grid):
    return int(grid[0][0]) + greedy_helper(grid, 1, 0)

def greedy_helper(grid, row, idx):
    # Returns 0 and ends function cycle once reaching the end of the triangle rows.
    if row >= len(grid):
        return 0
    else:
        # Checks which of the two branch offs is bigger and continues on that path.
        if grid[row][idx] > grid[row][idx+1]:
            return int(grid[row][idx]) + greedy_helper(grid, row+1, idx)
        else:
            return int(grid[row][idx+1]) + greedy_helper(grid,row+1, idx+1)

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return max(divide_conquer_helper(grid,0,0,0))

# Uses a list of all the sums as it recursively adds up each path.
def divide_conquer_helper(grid, row, idx, sum):
    if row >= len(grid):
        return [sum]
    else:
        if row == len(grid) - 1:
            return divide_conquer_helper(grid, row+1,idx,sum+ int(grid[row][idx]))
        else:
            return divide_conquer_helper(grid, row+1,idx,sum+ int(grid[row][idx]))+ \
                     divide_conquer_helper(grid,row+1,idx+1, sum + int(grid[row][idx]))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    return dynamic_prog_helper(grid, 0, 0)

def dynamic_prog_helper(grid, row, idx):
    if row >= len(grid):
        return 0
    else:
        left = int(grid[row][idx]) + dynamic_prog_helper(grid, row+1, idx)
        right = int(grid[row][idx])+ dynamic_prog_helper(grid, row+1, idx+1)
    #returns the largest of the two branches
    if left > right:
        return left
    else:
        return right

# reads the file and returns a 2-D list that represents the triangle
def read_file():
    in_file = open('./triangle.txt', 'r')

    # First line tells us how many rows there are
    numlines = in_file.readline()
    numlines = numlines.strip()
    numlines = int(numlines)
    triangle = []

    #Reads each row of triangle and adds it as a list to triangle
    for line in range(numlines):
        row = in_file.readline()
        row = row.strip()
        row = row.split()
        triangle.append(row)

    #Close file
    in_file.close()

    return triangle

def main ():
  # read triangular grid from file
  grid = read_file()

  # output greatest path from exhaustive search
  times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  x = brute_force(grid)
  print("The greatest path sum through exhaustive search is "+str(x)+".")
  print("The time taken for exhaustive search is "+str(times)+" seconds.")
  print()

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  x = greedy(grid)
  print("The greatest path sum through greedy search is " + str(x) + ".")
  print("The time taken for exhaustive search is " + str(times) + " seconds.")
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  x = divide_conquer(grid)
  print("The greatest path sum through recursive search is " + str(x) + ".")
  print("The time taken for exhaustive search is " + str(times) + " seconds.")
  print()

  grid = read_file()

  # output greatest path from dynamic programming
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  x = dynamic_prog(grid)
  print("The greatest path sum through dynamic programming is " + str(x) + ".")
  print("The time taken for exhaustive search is " + str(times) + " seconds.")
  print()

if __name__ == "__main__":
  main()