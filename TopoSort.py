#  File: TopoSort.py

#  Description: This program is meant to utilize and test a topological sort for a graph.

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 12/02/2018

#  Date Last Modified: 12/03/2018

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

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def hasCycle (self):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.hasCycleHelper(None, self.Vertices[i]):
                return True

            #reset visited flags to false
            for i in range(nVert):
                self.Vertices[i].visited = False
        return False

    #Helper function that checks all neighbors for each vertex for a cycle
    def hasCycleHelper(self, previous, vertex):
        #If vertex has already been visited then cycle is complete
        if vertex.visited == True:
            return True

        vertex.visited = True
        neighbors = self.getNeighbors(vertex.label)

        #Don't travel back to vertex visited just before
        if previous in neighbors:
            neighbors.remove(previous)
        #If there are no other neighbors then there is no cycle
        if len(neighbors) == 0:
            return False

        for i in neighbors:
            return self.hasCycleHelper(vertex,i)


    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        nVert = len(self.Vertices)
        #Duplicate graph
        newGraph = Graph()
        for i in range(nVert):
            newGraph.addVertex(self.Vertices[i])
        for a in range(nVert):
            for b in range(nVert):
                newGraph.addDirectedEdge(a, b, self.adjMat[a][b])

        #If a cycle is present then an empty list is returned
        sort = []
        if self.hasCycle():
            return sort

        #Traverse graph until vertex with no successor is found
        while nVert >0:
            x = 0
            while x < nVert:
                for i in range(nVert):
                    if newGraph.adjMat[x][i] != 0:
                        x+=1
                        break

                # Add the vertex with no succesor to list and remove from the graph
                if i == nVert-1:
                    final = newGraph.Vertices[x]
                    sort.insert(0,final)
                    newGraph.deleteVertex(final.label)
                    break
            nVert-=1
        return sort

def main():
    #create graph
    graph = Graph()

    #read file
    in_file = open("./topo.txt", "r")

    #Get number of vertices
    numVertices = in_file.readline().strip()
    numVertices = int(numVertices)

    #add vertices to the graph
    for i in range(numVertices):
        vert = in_file.readline().strip()
        graph.addVertex(vert)

    #Get number of Edges
    numEdges = in_file.readline().strip()
    numEdges = int(numEdges)

    #add directed edges to graph and vertices
    for i in range(numEdges):
        edge = in_file.readline().strip()
        edge = edge.split()
        start = graph.getIndex(edge[0])
        finish = graph.getIndex(edge[1])
        graph.addDirectedEdge(start, finish)

    #close file
    in_file.close()

    # test if a directed graph has a cycle
    print("Testing hasCycle() function")
    print(graph.hasCycle())
    print()

    # test topological sort
    print("Testing toposort() function")
    topolist = graph.toposort()
    for i in topolist:
        print(i, end=" ")

main()