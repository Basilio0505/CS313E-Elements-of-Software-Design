#  File: Work.py

#  Description: reads a file given the total amount of lines of code needed as well as the productivity level and
#   uses a binary search to find figure out the minimum allowable value of v for a given productivity
#   factor that will allow him to write at least n lines of code before he falls asleep.

#  Student Name: Basilio Bazan

#  Student UT EID:  bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10/08/2018

#  Date Last Modified: 10/08/2018

#Checks to see if mid needs to be raised or lowered
def is_done(n,k,mid):
    x, sum = 1, mid
    while(mid//k**x !=0)and (sum<n):
        sum+= mid//k**x
        x+=1
    return sum>=n

#Calculates the minimum value needed.
def binarySearch(n,k):
    lo, hi=1, n
    while lo<=hi: #Once lo passes hi it will return the set min
        mid = (lo + hi)//2 #sets the mid value
        if (is_done(n,k,mid)):
            hi = mid-1
            min = mid
        elif not (is_done(n,k,mid)):
            lo = mid+1
    return min

def main():
    in_file = open("./work.txt", "r")
    numlines = in_file.readline() #Opens file and grabs first value representing total cases.

    #Loop to process each case.
    for i in numlines:
        line = in_file.readline()
        line = line.strip()
        line = line.split()
        codelines = int(line[0]) #number of lines to work with
        production = int(line[1]) #productivity factor
        print(binarySearch(codelines, production))

    in_file.close()

main()