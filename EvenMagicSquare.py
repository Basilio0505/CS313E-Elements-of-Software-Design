#  File: EvenMagicSquare.py

#  Description: This program will use a brute force algorithm to create 4x4 magic squares using permutation
#   with focus on optimization.

#  Student Name: Basilio Bazan III

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10/20/2018

#  Date Last Modified: 10/24/2018

def permute (a, lo, correct_squares, total_squares):
    #side dimensions of the magic square.
    side = 4
    hi = len(a)
    if lo == hi:
        #Checks if indeed a magic square then prints it
        square = make_square(a)
        if check_square(square):
            print_square(square)
            #adds the magic square to array and checks if reached user input amount
            correct_squares.append(square)
            if(len(correct_squares)== total_squares):
                exit()
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            if(lo+1) % side == 0:
                if notMagic(a,lo):
                    a[lo], a[i] = a[i], a[lo]
                    continue
            if lo >= (side - 1) * side:
                if notMagic(a,lo):
                    a[lo], a[i] = a[i], a[lo]
                    continue
            permute(a, lo + 1, correct_squares, total_squares)
            a[lo], a[i] = a[i], a[lo]

def notMagic(a, lo):
    theSum = 34
    square = make_square(a)
    #sets idx to the row where lo is permuting at.
    if lo >= 12:
        idx = 3
    elif lo >= 8:
        idx = 2
    elif lo >= 4:
        idx = 1
    else:
        idx = 0

    #Checks to see if row sum is equal to the canonical sum.
    if (square[idx][0]+square[idx][1]+square[idx][2]+square[idx][3]) == theSum:
        return False
    else:
        return True


def make_square (n):
    count = 0
    side = 4
    magic_square = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for r in range(side):
        for c in range(side):
            magic_square[r][c] = n[count]
            count += 1

    return magic_square


#Format prints out the magic square
def print_square(magic_square):
    for row in magic_square:
        for val in row:
            print('{:3d} '.format(val), end='')
        print()
    print()

#checks to see if created square is indeed a magic square
def check_square(magic_square):
    sum = 0
    check_sum = 0

    #gets sum of the of the first row and uses it to check all other rows/colunms
    for x in range(len(magic_square)):
        check_sum += magic_square[0][x]

    #Checks if all rows are equal in sums
    for y in range(len(magic_square)):
        for x in range(len(magic_square)):
            sum += magic_square[x][y]
        if sum != check_sum:
            return False
        else:
            sum = 0

    #checks if all colunms are equal in sums
    for y in range(len(magic_square)):
        for x in range(len(magic_square)):
            sum += magic_square[y][x]
        if sum != check_sum:
            return False
        else:
            sum = 0

    #Checks both diagnols of the magic square
    for i in range(len(magic_square)):
        sum += magic_square[i][i]
    if sum != check_sum:
        return False
    else:
        sum = 0

    for i in range(len(magic_square)):
        sum += magic_square[i][len(magic_square)-i-1]
    if sum != check_sum:
        return False
    else:
        sum = 0

    return True

def main():
    #Prompt user to enter the number of magic squares making sure within 1-10
    total_squares = 0
    while (not(total_squares >= 1)) or (not (total_squares <= 10)):
        total_squares = input("Enter number of magic squares (1 - 10): ")
        try:
            total_squares = int(total_squares)
        except:
            total_squares = 0
            print("Invlaid input. Please enter a value from 1-10.")
            print()

    #Create a 1D list from 1-16 to be permuted.
    perm_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #Empty array that will be used to store magic squares
    correct_squares = []
    permute(perm_list, 0, correct_squares, total_squares)

main()