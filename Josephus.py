#  File: Josephus.py

#  Description: This program will use a circular list of values and eliminate one-by-one going clockwise
#    using an elimination value

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/08/2018

#  Date Last Modified: 11/09/2018

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    # Constructor
    def __init__ ( self ):
        self.first = None

    # Insert an element (value) in the list
    def insert ( self, data):
        new_link = Link(data)
        #If CircularList is empty create as first link
        if self.first == None:
            self.first = new_link
            new_link.next = new_link
            return

        current = self.first
        while current.next != self.first:
            current = current.next

        #Adds to end and end circles back to start
        current.next = new_link
        new_link.next = self.first

    # Find the link with the given data (value)
    def find ( self, data ):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            current = current.next

        return current

    # Delete a link with a given data (value)
    def delete ( self, data ):
        current = self.first
        previous = self.first

        #return None is list is empty
        if current == None:
            return None

        #Sets previous to lnk before first (end of list)
        while previous.next != self.first:
            previous = previous.next

        #locates link with matching data value
        while current.data != data:
            previous = current
            current = current.next

        #As long as list is not at final soldier sets first to the next value
        #after the one being deleted. So deletion continues after eliminated link
        if self.first != self.first.next:
            self.first = current.next
        else:
            self.first = None

        previous.next = current.next

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after ( self, start, n ):
        #current set to start link given in text file
        current = self.find(start)

        #Begins going 'clockwise' by elimination value
        for i in range(1,n):
            current = current.next

        print(str(current.data))

        #Deletes link
        self.delete(current.data)
        return current.next

    # Return a string representation of a Circular List
    def __str__ ( self ):
        s = ""
        current = self.first

        while current.next != self.first:
            s += str(current.data) + " "
            current = current.next

        return s

def main():
    #Read file
    in_file = open('josephus.txt','r')

    #Get amount of soldiers
    soldiers = in_file.readline()
    soldiers = soldiers.strip()
    soldiers = int(soldiers)

    # Get starting soldier for elimination
    start = in_file.readline()
    start = start.strip()
    start = int(start)

    #Get number for elimination
    num = in_file.readline()
    num = num.strip()
    num = int(num)

    #close file
    in_file.close()

    #Create circular list object and insert all soldiers
    group = CircularList()
    for i in range(1, soldiers + 1):
        group.insert(i)

    #eliminates soldiers one-by-one until one is left
    for i in range(1,soldiers):
        start = group.delete_after(start, num)
        start = start.data
    #Print the lone survivor
    start = group.delete_after(start,num)
    print()

main()
