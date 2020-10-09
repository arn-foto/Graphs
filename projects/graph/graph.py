"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # keys are all sets in the graph, values are a set of adj verts

    def add_vertex(self, vertex_id): 
        self.vertices[vertex_id] = set()
        # """
        # Add a vertex to the graph.
        # """
        
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        
        # """
        # Add a directed edge to the graph.
        # """
      
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
        
        

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        # Init
        q.enqueue(starting_vertex)
        # while queue isn't empty
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                # "visit" the node
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
       
        # """
        # Print each vertex in breadth-first order
        # beginning from starting_vertex.
        # """
      
      
        
    def dft(self, starting_vertex):
        q = Stack()
        visited = set()
        # Init
        q.push(starting_vertex)
        # while queue isn't empty
        while q.size() > 0:
            v = q.pop()
            if v not in visited:
                # "Visit" the node
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)
        # """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        # """



    def dft_recursive(self, starting_vertex, visited=None):
        # we need to keep track of visited nodes
        if visited is None:
            visited = set()
        # this will keep this from going into an infinit loop
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for next_vertex in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vertex, visited)

        # """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.

        # This should be done using recursion.
        # """
        
        
        
    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue
        path = Queue()
        # Add the starting vertex to the path
        path.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # if queue is not empty
        while path.size() > 0:
            # dequeue the first path 
            new_path = path.dequeue()
            # grab the last vertext from
            edge = new_path[-1]
            # if the vertext has not been visited
            if edge not in visited:
                # check to see if this is the target
                if edge is destination_vertex:
                    # if so then return path
                    return new_path
                visited.add(edge)
                # add a path to its neighbor to the back of the stack
                neighbors = self.get_neighbors(edge)
                for neighbor in neighbors:
                    # Copy the path
                    path_copy = new_path.copy()
                    # append neighbor to the back
                    path_copy.append(neighbor)
                    path.enqueue(path_copy)
        # """
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in
        # breath-first order.
        # """



    def dfs(self, starting_vertex, destination_vertex):
        # Create an empty stack
        path = Stack()
        # Add the starting vertex to the path
        path.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        #  Add the starting vertex to the set
        visited.add(starting_vertex)
        # Loop while the stack is not empty
        while path.size() > 0:
            # Pop the first element
            new_edge = path.pop()
            # Add the popped element to the visited set
            visited.add(new_edge)
            # Get all neighbors
            neighbors = self.get_neighbors(new_edge)
           # Put all the neighbors on the stack
            for neighbor in neighbors:
                if neighbor not in visited:
                   path.push(neighbor)
                if neighbor is destination_vertex:
                    visited.add(neighbor)
                    return list(visited)

        # """
        # Return a list containing a path from
        # starting_vertex to destination_vertex in
        # depth-first order.
        # """

    def dfs_recursive(self, starting_vertex, destination_vertex,visited=None, path=None):
        if visited is None:
            visited = set()
            
        if path is None:
            path = [starting_vertex]
            
        print(starting_vertex)
        visited.add(starting_vertex)
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                
                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path
                
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
                
        return None
                
        # """
        # Return a list containing a path from
        # starting_vertex to destination_vertex in
        # depth-first order.

        # This should be done using recursion.
        # """


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
