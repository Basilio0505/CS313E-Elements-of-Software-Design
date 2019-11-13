#  File: Boxes.py

#  Description: This program will take data of different boxes and then nest them within eachother in the largest
#    possible subset.

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10/18/2018

#  Date Last Modified: 10/19/2018


#Returns true if the box demensions are less than the box it would be placed in
def does_fit(box1, box2):
    return(box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def all_fit(set):
    for i in range(0, len(set)-1):
        if not(does_fit(set[i],set[i+1])):
            return False
    return True

#Modified subset function that will create subsets of boxes making sure they fit within eachother.
def subsets(a,b,lo,boxes):
    hi = len(a)
    if lo == hi:
        if all_fit(b):
            boxes.append(b)
            return
    else:
        c = b[:]
        b.append(a[lo])
        subsets(a, c, lo+1, boxes)
        subsets(a, b, lo+1, boxes)


def main():
    in_file = open('./boxes.txt', 'r')
    numlines = in_file.readline()
    numlines = numlines.strip()
    numlines = int(numlines)
    box_list = []

    #Take each line and make box
    for i in range(numlines):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)
    in_file.close()

    #Sorts boxes in order from smallest to largest
    box_list.sort()

    #Create what would be the final organized box list
    sub_boxes = []
    hold = []
    subsets(box_list, hold, 0, sub_boxes)

    #Start the largest subset possible as the minimum possible then work up
    largest_subset = 2
    for x in sub_boxes:
        if len(x) > largest_subset:
            largest_subset = len(x)

    #Getting rid of all subsets that are less than the largest subset possible.
    smallsets = []
    for i in range(0, len(sub_boxes)):
        if len(sub_boxes[i]) != largest_subset:
            smallsets.append(sub_boxes[i])
    for set in smallsets:
        sub_boxes.remove(set)
    sub_boxes.sort()

    #Print out the results
    print("Largest Subset of Nesting Boxes")
    for set in sub_boxes:
        for box in set:
            print(box)
        print()
main()