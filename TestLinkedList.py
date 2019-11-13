#  File: TestLinkedList.py

#  Description: This function contains and tests functions that make up a linked lst.

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/05/2018

#  Date Last Modified: 11/05/2018

class Link(object):
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        count = 0
        if self.first == None:
            return count

        current = self.first
        count +=1
        while current.next != None:
            current = current.next
            count+=1
        return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            current = current.next
        current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_link = Link(data)
        current = self.first
        if current == None or current.data > new_link.data:
            self.insert_first(new_link.data)
            return

        while current.next != None and current.next.data <= new_link.data:
            current = current.next

        new_link.next = current.next
        current.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next
        return current.data

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            elif current.data > data:
                return None
            else:
                current = current.next
        return current.data

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first
        if current ==None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current ==self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current.data

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        list_string = ''
        current = self.first
        list_len = self.get_num_links()
        count =0

        for i in range(list_len):
            list_string += str(current.data) + '  '
            current = current.next
            count += 1

            #Starts a new line after every 10 values
            if count % 10 == 0:
                list_string += '\n'
        return list_string

    # Copy the contents of a list and return new list
    def copy_list(self):
        new_list = LinkedList()
        current = self.first
        while current != None:
            new_list.insert_last(current.data)
            current = current.next
        return new_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        new_list = LinkedList()
        current = self.first
        while current != None:
            new_list.insert_first(current.data)
            current = current.next
        return new_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        new_list = LinkedList()
        current = self.first
        while current != None:
            new_list.insert_in_order(current.data)
            current = current.next
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        while current.next != None:
            if current.data > current.next.data:
                return False
            else:
                current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first == None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        new_list = LinkedList()
        current = self.first

        #Adds one of the lists to the new empty one
        while current != None:
            new_list.insert_last(current.data)
            current = current.next

        #Adds the other list to the end
        current = other.first
        while current != None:
            new_list.insert_last(current.data)
            current = current.next

        #The actual marge/sort of the two lists
        new_list = new_list.sort_list()
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        #First check if both lists are same size
        if self.get_num_links() != other.get_num_links():
            return False

        current = self.first
        current_other = other.first
        for i in range(self.get_num_links()):
            if current != current_other:
                return False
            else:
                current = current.next
                current_other = current_other.next

        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        new_list = LinkedList()
        current = self.first
        length = self.get_num_links()
        count = 0

        holder = set([])

        if length == 0:
            return None
        while current != None:
            holder.add(current.data)
            count +=1
            if len(holder) == count:
                new_list.insert_last(current.data)
            else:
                current = current.next
                count -=1
        return new_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    list = LinkedList()
    print("Testing insert_first() and __str__() methods")
    list.insert_first(34)
    list.insert_first(12)
    list.insert_first(76)
    list.insert_first(4)
    list.insert_first(23)
    list.insert_first(52)
    list.insert_first(12)
    list.insert_first(8)
    list.insert_first(1)
    list.insert_first(89)
    print(list)
    print()

    # Test method insert_last()
    print("Testing method insert_last()")
    list.insert_last(50)
    print(list)
    print()

    # Test method insert_in_order()
    print("Testing method insert_in_order()")
    list.insert_in_order(29)
    print(list)
    print()

    # Test method get_num_links()
    print("Testing method get_num_links()")
    print(list.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print("Testing method find_unordered()")
    print(list.find_unordered(4))
    print(list.find_unordered(100))
    print()

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print("Testing method find_ordered(). Original list is sorted.")
    sorted_list = list.sort_list()
    print(sorted_list)
    print()
    print(sorted_list.find_ordered(23))
    print(sorted_list.find_ordered(0))
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print("Testing method delete_link()")
    print(list)
    print()
    print(list.delete_link(29))
    print(list.delete_link(90))
    print()
    print(list)
    print()

    # Test method copy_list()
    print("Testing method copy_list()")
    print(list.copy_list())
    print()

    # Test method reverse_list()
    print("Testing method reverse_list()")
    print(list.reverse_list())
    print()

    # Test method sort_list()
    print("Testing method sort_list()")
    print(list.sort_list())
    print()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Testing method is_sorted()")
    sorted_list = list.sort_list()
    print(sorted_list.is_sorted())
    print(list.is_sorted())
    print()

    # Test method is_empty()
    print("Testing method is_empty()")
    print(list.is_empty())
    print()

    # Test method merge_list()
    print("Testing method merge_list()")
    other = LinkedList()
    other.insert_last(66)
    other.insert_last(31)
    other.insert_last(14)
    print(list.merge_list(other))
    print()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print("Testng method is_equal()")
    double = list
    empty = LinkedList()
    print(list.is_equal(double))
    print(list.is_equal(empty))
    print()

    # Test remove_duplicates()
    print("Testing method remove_duplicates()")
    print(list)
    print()
    print(list.remove_duplicates())
    print()

if __name__ == "__main__":
    main()