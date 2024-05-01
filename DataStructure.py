from collections import defaultdict, deque

class RecipeGraph:
    
    """
    A class representing a graph of recipes and ingredients.

    Attributes:
    - graph (defaultdict): A defaultdict where keys are recipe or ingredient nodes,
                           and values are lists of adjacent nodes.

    Methods:
    - add_edge(node1, node2): Add an edge between node1 and node2 in the graph.
    - bfs(start): Perform a Breadth-First Search (BFS) starting from the given node.
    - print_graph(): Print the graph (for debugging purposes).
    - get_graph(): Get the graph.
    """
    
    def __init__(self):
        """
        Initialize RecipeGraph with empty defaultdict.
        """
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2):
        """
        Add an edge between two nodes in the graph.

        Parameters:
        - node1 (any): The first node.
        - node2 (any): The second node.
        """
        self.graph[node1].append(node2)

    def bfs(self, start):
        """
        Perform a Breadth-First Search (BFS) starting from the given node.

        Parameters:
        - start (any): The starting node for BFS.

        Returns:
        - results (defaultdict): A defaultdict containing the BFS results,
                                 where keys are nodes visited during BFS,
                                 and values are lists of adjacent nodes.
        """
        visited = set()
        queue = deque([(start, [])])
        results=defaultdict(list)
        while queue:
            node, path = queue.popleft()
            if node not in visited:
                visited.add(node)
                if start in self.graph[node]:
                    results[node]=self.graph[node]
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return results
                    
    def print_graph(self):
        """ 
        Print the graph
        """
        print(self.graph)
        
    def get_graph(self):
        """Get the graph

        Returns:
            graph (defaultdict): The graph containing recipe and ingredient nodes with their adjacent nodes.
        """
        return self.graph