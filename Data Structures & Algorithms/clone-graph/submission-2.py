"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node

        oton = {}

        stk = [start]

        visited = set()
        visited.add(start)

        while stk:
            node = stk.pop()
            oton[node] = Node(val=node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        
        for old_node, new_node in oton.items():
            for nei in old_node.neighbors:
                new_nei = oton[nei]
                new_node.neighbors.append(new_nei)
        
        return oton[start]






        