#  File: BST_Cipher.py

#  Description: This program utilizes a binary tree to encrypt and decrypt string with a given key.

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/10/2018

#  Date Last Modified: 11/12/2018

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        for i in encrypt_str:
            self.insert(i)

    # Helper function that determines whether a character already
    # exists in the tree.
    def duplicate (self, ch):
        current = self.root
        duplicate = False
        while current != None:
            if current.data == ch:
                duplicate = True
                break
            if ch < current.data:
                current = current.lchild
            else:
                current = current.rchild
        return duplicate

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new_node = Node(ch)
        if self.root == None:
            self.root = new_node
            return

        if not self.duplicate(ch):
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if ch < current.data:
                    current = current.lchild
                else:
                    current = current.rchild
            if ch < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node


    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if not self.duplicate(ch):
            return ""

        current = self.root
        if ch == current.data:
            return "*"

        series = ""
        while current != None and current.data != ch:
            if ch < current.data:
                current = current.lchild
                series += "<"
            else:
                current = current.rchild
                series += ">"
        return series

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        if st == "*":
            return current.data
        for i in st:
            if current != None:
                if i == "<":
                    current = current.lchild
                elif i  == ">":
                    current = current.rchild
            else:
                return ""
        return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        new_str = ""
        st = st.lower()
        for i in st:
            if i.isalpha() or i == " ":
                new_str += i
        encrypted = ""
        for i in new_str:
            encrypted += str(self.search(i)) +"!"

        return encrypted[0:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        new_str = ""
        for i in st:
            if i == "<" or i == ">" or i == "*" or i == "!":
                new_str += i
        dlist = new_str.split('!')
        decrypted = ""
        for i in dlist:
            decrypted += self.traverse(i)
        return decrypted

def main ():
    enkey = input("Enter encryption key: ")
    enkey = enkey.lower()
    key = Tree(enkey)
    print()

    en_string = input("Enter string to be encrypted: ")
    en_string = key.encrypt(en_string)
    print("Encrypted string: " + str(en_string))
    print()

    de_string = input("Enter string to be decrypted: ")
    de_string = key.decrypt(de_string)
    print("Decrypted string: "+ str(de_string))

main()