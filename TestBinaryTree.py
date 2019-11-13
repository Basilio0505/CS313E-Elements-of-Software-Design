#  File: TestBinaryTree.py

#  Description: This program will utilize binary trees and use four special functions: is_similar, print_level,
#   get_height and num_nodes

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/16/2018

#  Date Last Modified: 11/16/2018

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__(self):
        self.root = None
        self.size = 0

    # Inserts a node into the tree
    def insert(self, data):
        new_node = Node(data)

        if self.root == None:
            self.root = new_node
            self.size += 1
            return

        current = self.root
        parent = self.root
        while current != None:
            parent = current
            if data < current.data:
                current = current.lchild
            else:
                current = current.rchild

        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node
        self.size += 1

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        if self.root == None and pNode.root == None:
            return True
        elif self.size != pNode.size:
            return False
        else:
            return self.is_similarHelper(self.root, pNode.root)

    #Goes through each node in both trees and makes sure they are equal
    def is_similarHelper (self, node1, node2):
        if node1 == None and node2 ==None:
            return True
        elif node1.data == node2.data and \
            self.is_similarHelper(node1.lchild,node2.lchild) and \
            self.is_similarHelper(node1.rchild,node2.rchild):
            return True
        else:
            return False

    # Prints out all nodes at the given level
    def print_level (self, level):
        if self.root == None:
            return None
        self.print_levelHelper(self.root,level, 1)

    # Goes through a tree and only prints a node once the given level is reached.
    def print_levelHelper(self,node, lvl, currentlvl):
        if node == None:
            return
        elif lvl == currentlvl:
            print(node.data, end=' ')
        else:
            self.print_levelHelper(node.lchild, lvl, currentlvl+1)
            self.print_levelHelper(node.rchild, lvl, currentlvl+1)

    # Returns the height of the tree
    def get_height (self):
        if self.root == None:
            return 0
        else:
            return self.get_heightHelper(self.root)

    def get_heightHelper(self, node):
        if node == None:
            return 0
        else:
            lheight = self.get_heightHelper(node.lchild)
            rheight = self.get_heightHelper(node.rchild)

            if(lheight > rheight):
                return lheight +1
            else:
                return rheight +1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        if self.root == None:
            return 0
        else:
            return self.num_nodesHelper(self.root)


    def num_nodesHelper(self, node):
        if node == None:
            return 0
        else:
            return self.num_nodesHelper(node.lchild)+1+ self.num_nodesHelper(node.rchild)

def main():
    # Create three trees - two are the same and the third is different
    binarytree1 = Tree()
    binarytree2 = Tree()
    binarytree3 = Tree()
    list1 = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    list2 = [50, 30, 32, 78, 23]

    for i in list1:
        binarytree1.insert(i)
        binarytree2.insert(i)

    for i in list2:
        binarytree3.insert(i)

    # Test your method is_similar()
    print("Testing is_similar")
    if binarytree1.is_similar(binarytree2):
        print("\nBinary Tree 1 is similar to Binary Tree 2")
    else:
        print("\nBinary Tree 1 is not similar to Binary Tree 2")

    if binarytree1.is_similar(binarytree3):
        print("\nBinary Tree 1 is similar to Binary Tree 3")
    else:
        print("\nBinary Tree 1 is not similar to Binary Tree 3")

    # Print the various levels of two of the trees that are different
    print("\nTesting print_level")
    print("level 3 of Binary Tree 1")
    binarytree1.print_level(3)
    print()
    print("level 3 of Binary Tree 3")
    binarytree3.print_level(3)
    print()

    # Get the height of the two trees that are different
    print("\nTesting get_height")
    print("Binary Tree 1 Height:")
    print(binarytree1.get_height())
    print("Binary Tree 3 Height:")
    print(binarytree3.get_height())

    # Get the total numbe of nodes a binary search tree
    print("\nTesting num_nodes")
    print("Number of nodes in Binary Tree 1:")
    print(binarytree1.num_nodes())
    print("Number of nodes in Binary Tree 2:")
    print(binarytree2.num_nodes())
    print("Number of nodes in Binary Tree 3:")
    print(binarytree3.num_nodes())

main()