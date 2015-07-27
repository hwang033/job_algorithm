#definition for a undirected graph node

class UndirectedGraphNode:

    def __init__(self, x):

        self.label = x

        self.neighbors = []



class Solution:

    # @param node, a undirected graph node

    # @return a undirected graph node

    def cloneGraph(self, node):

        if not node:

            return node

        

        visited_node = {}

 

        

        old_neighbors_list = [node]

        return_node = None

        

        while len(old_neighbors_list) > 0:

            cur_node = old_neighbors_list.pop()

            neighbors_list = []

            
            new_node1 = None

            if not visited_node.has_key(cur_node):

                new_node1 = UndirectedGraphNode(cur_node.label)

                visited_node[cur_node] = new_node1
            else:
                new_node1 = visited_node[cur_node]

            

            return_node = new_node1 if return_node is None else return_node

            

            for neighbor in cur_node.neighbors:

            

                if visited_node.has_key(neighbor):

                    neighbors_list.append(visited_node[neighbor])



                else:

                    old_neighbors_list.append(neighbor)

                    new_node2 = UndirectedGraphNode(neighbor.label)

                    

                    neighbors_list.append(new_node2)

                    visited_node[neighbor] = new_node2


            new_node1.neighbors = neighbors_list[:]
            print  new_node1.label           
            print  len(new_node1.neighbors)

        return return_node

if __name__ == "__main__":
       

    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(-1)
    n2.neighbors = [n1]
    s = Solution()
    node = s.cloneGraph(n2)
    print node.label
    print node.neighbors[0].label
    


