class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        self.d = 0
        self.f = 0
        self.color = 'white'
        self.pi = None

time = 0
def dfs(s, e):
    s.color = 'gray'
    s.d = time + 1    
    for v in s.neighbors:
        if v == e:
            return True
        if v.color == 'white':
            v.pi = s
            if dfs(v, e) == True:
                return True
    s.f = time + 1 
    s.color = 'black'
    return False 
        
if __name__ == "__main__":
    n1 = GraphNode(1)
    n2 = GraphNode(2)
    n3 = GraphNode(3)
    n4 = GraphNode(4)

    n1.neighbors.append(n2)
    n2.neighbors.append(n3)
    n4.neighbors.append(n3)
    
    print dfs(n1, n3) 
    print dfs(n1, n4) 
