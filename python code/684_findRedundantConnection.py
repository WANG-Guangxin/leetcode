# 在本问题中, 树指的是一个连通且无环的无向图。

# 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

# 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

# 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

# 示例 1：

# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的无向图为:
#   1
#  / \
# 2 - 3
# 示例 2：

# 输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# 输出: [1,4]
# 解释: 给定的无向图为:
# 5 - 1 - 2
#     |   |
#     4 - 3
# 注意:

# 输入的二维数组大小在 3 到 1000。
# 二维数组中的整数在1到N之间，其中N是输入数组的大小。

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        我的代码
        '''
        n = len(edges)
        parent = [-1] * n
        rank = [0] * n
        def find(x,parent):
            while parent[x] != -1:
                x = parent[x]
            return x
        def unionset(x,y,parent,rank):
            x_root = find(x,parent)
            y_root = find(y,parent)
            if x_root != y_root:
                if rank[x_root] < rank[y_root]:
                    parent[x_root] = y_root
                elif rank[y_root] < rank[x_root]:
                    parent[y_root] = x_root
                else:
                    parent[y_root] = x_root
                    rank[x_root] += 1
                return True
            else:
                return False
        for x in edges:
            if not unionset(x[0]-1,x[1]-1,parent,rank):
                return x

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    	'''
    	并查集  该学一下了


    	'''
        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        
        return []

