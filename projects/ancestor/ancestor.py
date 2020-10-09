
## this is my graph, son!
class Graph:
    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):

    g = Graph()
    # go through the ancestors
    for i in ancestors:
        # Given a list of tuples ->
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        g.add_edge(i[1], i[0])
    # Add Queue for BFS
    q = Queue()
    # Enqueue as a list so we remember our path
    q.enqueue([starting_node])
    # If there is more than one ancestor tied for "earliest"
    max_path = 1
    # If the input individual has no parents, the function should return -1.
    earliest = -1
    # if queue is not empty
    while q.size() > 0:
        # then dequeue the first path
        path = q.dequeue()
        # mark the last node in the path as visited
        v = path[-1]
        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)
        for next_item in g.vertices[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    return earliest
