Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

类型 1：只能由 Alice 遍历。
类型 2：只能由 Bob 遍历。
类型 3：Alice 和 Bob 都可以遍历。
给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

 

示例 1：



输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
示例 2：



输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
输出：0
解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
示例 3：



输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
输出：-1
解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。
 

提示：

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
所有元组 (typei, ui, vi) 互不相同

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        并查集还不会 这是一个纯深度优先的方法 
        分别 构建边类型 1 3 组成的图 和 类型 2 4 组成的图 判断是否可遍历
        如果可遍历  再对类型 3 组成的图进行遍历 并且计算连通分量的个数
        可删除的变数  等于  
        
        类型 3 的边总数 - （节点总数 - 连通分量数）
        +
        类型 1 的边总数 - （连通分量数 - 1）
        +
        类型 2 的边总数 - （连通分量数 - 1）

        '''

        # 深度优先
        def dfs(node,edge,seen):
            seen.add(node)
            for n in edge[node]:
                if n not in seen:
                    dfs(n,edge,seen)

        # 判断是否可遍历
        def ke_bian_li(edge):
            seen = set()
            dfs(0,edge,seen)
            if len(seen) < n:
                return False
            else:
                return True
        

        # 建图
        edgesA = collections.defaultdict(list)
        edgesB = collections.defaultdict(list)
        edgesC = collections.defaultdict(list)
        c = nums1 = nums2 = 0
        for x,y,z in edges:
            if x == 1 or x == 3:
                edgesA[y-1].append(z-1)
                edgesA[z-1].append(y-1)
            if x == 2 or x == 3:
                edgesB[y-1].append(z-1)
                edgesB[z-1].append(y-1)
            if x == 3:
                edgesC[y-1].append(z-1)
                edgesC[z-1].append(y-1)
                c += 1
            if x == 1: nums1 += 1
            if x == 2: nums2 += 1
        
        if not ke_bian_li(edgesA):return -1
        if not ke_bian_li(edgesB):return -1

        

        # 计算连通分量个数
        vis = set()
        ltfl = 0
        for i in range(n):
            if i not in vis:
                ltfl += 1
                dfs(i,edgesC,vis)

        # 返回最大可删除边数
        return nums1-(ltfl-1)+nums2-(ltfl-1)+c-(n-ltfl)


'''
====================官方题解：并查集========================
'''

# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        
        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.unite(u, v):
                    ans += 1
                else:
                    ufb.unite(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.unite(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.unite(u, v):
                    ans += 1

        if ufa.setCount != 1 or ufb.setCount != 1:
            return -1
        return ans
