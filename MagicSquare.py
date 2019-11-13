'''
  File: MagicSquare.py

  Description: The Magic Squares program will take a odd number and will then create a magic square making so that each
  row and colum seperately add up to the sam total.

  Student's Name: Basilio Bazan

  Student's UT EID: bb36366

  Course Name: CS313E

  Unique Number: 51345

  Date Created: 09/07/2018

  Date Last Modified: 09/08/2018
'''

def make_square ( n ):
    magic_square = [[0 for c in range(n)]for r in range(n)]
    col = int(n/2)
    row = n-1

    num = 1
    while num <= (n*n):
        if col == n and row == n:
            row = n-2
            col= n-1
        else:
            if row == n:
                row = 0
            if col == n:
                col = 0
        if magic_square[row][col]:
            row = row-2
            col = col-1
            continue
        else:
            magic_square[row][col] = num
            num = num+1
        row = row + 1
        col = col + 1
    return magic_square

def print_square(magic_square):
    for row in magic_square:
        for val in row:
            print('{:3d} '.format(val), end='')
        print()

def check_square(magic_square):
    sum = 0
    check_sum = 0

    for x in range(len(magic_square)):
        check_sum += magic_square[0][x]
    for y in range(len(magic_square)):
        for x in range(len(magic_square)):
            sum += magic_square[x][y]
        if sum != check_sum:
            return False
        else:
            sum = 0

    for y in range(len(magic_square)):
        for x in range(len(magic_square)):
            sum += magic_square[y][x]
        if sum != check_sum:
            return False
        else:
            sum = 0

    return True

def main():
    try:
        n=0
        while n%2 == 0:
            n = int(input("Please enter an odd number: "))
            if n%2 == 0 or n < 0:
                print("Sorry the value you entered was not an odd number.")
    except:
        print("The value entered was invalid.")

    magic_square = make_square(n)
    print("")
    print("Here is a "+str(n)+" x "+str(n)+ " magic square:")
    print("")
    print_square(magic_square)

    if check_square(magic_square):
        print("")
        print("This is a magic square and the canonical sum is ", int(n*((n*n) + 1)/2))
    else:
        print("This is not a magic square")

if __name__ == "__main__":
    main()