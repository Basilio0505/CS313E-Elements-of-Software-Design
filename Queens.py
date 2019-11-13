#  File: Queens.py

#  Description: This program will take a size input from the user then solves the Queens board
#   problem and finds all possible solutions.

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10/29/2018

#  Date Last Modified: 10/29/2018

class Queens(object):
    # initialize the board
    def __init__(self, n = 8):
        self.board = []
        self.n = n

        # keeps track of the amount of boards possible
        self.count = 0

        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if self.board[row][i] == 'Q' or self.board[i][col] == 'Q':
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # a recursive backtracking function that finds all solutions for a given size
    # if the problem has a solution print the board
    def solve(self, col):
        if col == self.n:
            self.count+=1
            self.print_board()
            print()
        else:
            for row in range(self.n):
                if self.is_valid(row, col):
                    self.board[row][col] = 'Q'
                    self.solve(col+1)
                    self.board[row][col] = '*'


def main():
    # Prompt user to enter the size of the board
    size = 0
    while not(size >= 1) or not(size <= 8):
        size = input("Enter the size of board: ")
        print()
        try:
            size = int(size)
        except:
            size = 0
            print("Invlaid input. Please enter a value from 1-8")
            print()

    # create a regular chess board
    game = Queens(size)

    # place the queens on the board
    game.solve(0)
    print("There are "+str(game.count)+" solutions for a "+str(size)+" x "+str(size)+" board.")

main()
