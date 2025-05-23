# ----------------------------------------------------------------------------------------------------------------------
# A graph has nodes (vertices) and edges
#   - Nodes: Information associated with them
#   - Edges: Can be undirected, directed and/or weighted

# Trees are a special case of graphs
# ----------------------------------------------------------------------------------------------------------------------


class Node(object):
    def __init__(self, name):
        """assumes name is a string"""
        self.name = name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name


class Edge(object):
    def __init__(self, start, end):
        """assumes start and end are Nodes"""
        self.start = start
        self.end = end
    def __str__(self):
        return self.start.__str__() + ' --> ' + self.end.__str__()
    def getStart(self):
        return self.start
    def getEnd(self):
        return self.end

class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node not in self.edges:
            self.edges[node] = []
        else:
            raise ValueError("Duplicate node")
    def addEdge(self, edge):
        start = edge.getStart()
        end = edge.getEnd()
        if not(start in self.edges and end in self.edges[start]):
            self.edges[start].append(end)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges  # returns True or False

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError("Node '" + name + "' not found")

    def __str__(self):
        result = ""
        for start in self.edges:
            for end in self.edges[start]:
                result += start.getName() + ' -> ' + end.getName() + '\n'
        return result


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getEnd(), edge.getStart())
        Digraph.addEdge(self, rev)


p = Node('Porter')
c = Node('Central')
n = Edge(p, c)

di = Digraph()
di.addNode(p)
di.addNode(c)
di.addEdge(n)

print(di.edges)

print(n)

