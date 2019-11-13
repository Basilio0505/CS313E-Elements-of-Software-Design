#  File: Graph.py

#  Description:

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 11/28/2018

#  Date Last Modified: 11/30/2018

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append ( item )

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek (self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty (self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len(self.stack))

class Queue (object):
    def __init__ (self):
        self.queue = []

    def enqueue (self, item):
        self.queue.append (item)

    def dequeue (self):
        return (self.queue.pop(0))

    def isEmpty (self):
        return (len (self.queue) == 0)

    def size (self):
        return len (self.queue)

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def wasVisited (self):
        return self.visited

    # determine the label of the vertex
    def getLabel (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

class Graph (object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex already exists in the graph
    def hasVertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).label):
                return True
        return False

    # get index from vertex label
    def getIndex (self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if ((self.Vertices[i]).label == label):
                return i
        return -1

    def addVertex(self, label):
        if not self.hasVertex(label):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix for the new Vertex
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex in the adjacency matrix
            newRow = []
            for i in range(nVert):
                newRow.append(0)
            self.adjMat.append(newRow)

    # add weighted directed edge to graph
    def addDirectedEdge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def addUndirectedEdge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v
    def getAdjUnvisitedVertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
                return i
        return -1

    # do the depth first search in a graph
    def dfs(self, v):
        # create a Stack
        theStack = Stack()

        # mark vertex v as visited and push on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit other vertices according to depth
        while (not theStack.isEmpty()):
            # get an adjacent unvisited vertex
            u = self.getAdjUnvisitedVertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)
        # the stack is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do breadth first search in a graph
    def bfs(self, v):
        # create a Queue
        theQueue = Queue()

        # mark the vertex as visited and enqueue
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit other vertices according to depth
        while (not theQueue.isEmpty()):
            # get the front vertex
            front = theQueue.dequeue()
            # get an adjacent unvisited vertex
            adj = self.getAdjUnvisitedVertex(front)
            while (adj != -1):
                (self.Vertices[adj]).visited = True
                print(self.Vertices[adj])
                theQueue.enqueue(adj)
                adj = self.getAdjUnvisitedVertex(front)

        # queue is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
        weight = self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]
        if weight == 0:
            return -1
        return weight

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def getNeighbors (self, vertexLabel):
        neighbors = []
        v = self.getIndex(vertexLabel)
        for i in range(len(self.Vertices)):
            if (self.adjMat[v][i] > 0):
                neighbors.append(self.Vertices[i])
        return neighbors

    # get a copy of the list of vertices
    def getVertices (self):
        vert_list = []
        for i in self.Vertices:
            vert_list.append(i)
        return vert_list

    # delete an edge from the adjacency matrix
    def deleteEdge (self, fromVertexLabel, toVertexLabel):
        start = self.getIndex(fromVertexLabel)
        finish = self.getIndex(toVertexLabel)
        #Set edge to 0 meaning no edge
        self.adjMat[start][finish] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def deleteVertex (self, vertexLabel):
        v = self.getIndex(vertexLabel)
        nVert = len(self.Vertices)

        # Delete column
        for i in range(nVert):
            for j in range(v, nVert - 1):
                self.adjMat[i][j] = self.adjMat[i][j + 1]
            self.adjMat[i].pop()

        # Delete row
        self.adjMat.pop(v)

        #Delete vertex
        for vertex in self.Vertices:
            if vertex.label == vertexLabel:
                self.Vertices.remove(vertex)

def main():
    #create a Graph object
    cities = Graph()

    #Open File
    inFile = open("./graph.txt", "r")

    # read the Vertices
    numVertices = int((inFile.readline()).strip())
    #print(numVertices)

    for i in range(numVertices):
        city = (inFile.readline()).strip()
        #print(city)
        cities.addVertex(city)

    # read the edges
    numEdges = int((inFile.readline()).strip())
    #print(numEdges)
    for i in range(numEdges):
        edge = (inFile.readline()).strip()
        #print(edge)
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])
        cities.addDirectedEdge(start, finish, weight)

    #Get Starting Vertex for search
    start = (inFile.readline()).strip()

    # test depth first search
    print("Depth First Search")
    cities.dfs(cities.getIndex(start))
    print()

    # test breadth first search
    print("Breadth First Search")
    cities.bfs(cities.getIndex(start))
    print()

    #Get Edge to delete
    delete_city = (inFile.readline()).strip()
    delete_city = delete_city.split()

    # test deletion of an edge
    print("Deletion of an Edge")
    cities.deleteEdge(delete_city[0],delete_city[1])

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range(numVertices):
        for j in range(numVertices):
            print(cities.adjMat[i][j], end=' ')
        print()
    print()

    # Get Vertex to delete
    delete_vertex = (inFile.readline()).strip()

    # test deletion of a vertex
    print("Deletion of a Vertex")
    print("\nList of Vertices")
    cities.deleteVertex(delete_vertex)
    for i in cities.Vertices:
        print(i.label)

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range(numVertices-1):
        for j in range(numVertices-1):
            print(cities.adjMat[i][j], end=' ')
        print()
    print()

    #close file
    inFile.close()

if __name__ == "__main__":
    main()