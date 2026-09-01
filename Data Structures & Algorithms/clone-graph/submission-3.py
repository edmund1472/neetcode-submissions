class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oton = {}

        def dfs(node):
            if node in oton:
                return oton[node]

            copy = Node(node.val)
            oton[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)