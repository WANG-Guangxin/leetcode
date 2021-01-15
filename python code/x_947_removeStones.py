n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

示例 1：

输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
示例 2：

输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
示例 3：

输入：stones = [[0,0]]
输出：0
解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。

提示：

1 <= stones.length <= 1000
0 <= xi, yi <= 104
不会有两块石头放在同一个坐标点上

class Solution:
	def removeStones(self, stones: List[List[int]]) -> int:
		'''
		优化建图 + 深度优先
		'''
		n = len(stones)
		edge = collections.defaultdict(list)
		rec = collections.defaultdict(list)
		for i,(x,y) in enumerate(stones):
			rec[x].append(i)
			rec[1000 + y].append(i)

		for vec in rec.values():
			k = len(vec)
			for i in range(1,k):
				edge[vec[i]].append(vec[i-1])
				edge[vec[i-1]].append(vec[i])

		def dfs(node):
			vis.add(node)
			for y in edge[node]:
				if y not in vis:
					dfs(y)

		vis = set()
		num = 0
		for i in range(n):
			if i not in vis:
				num += 1
				dfs(i)

		return n - num




    def removeStones_1(self, stones: List[List[int]]) -> int:
    	'''
    	深度优先
    	'''
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    edge[i].append(j)
        
        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)
        
        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)
        
        return n - num







    def removeStones_2(self, stones: List[List[int]]) -> int:
    	'''
    	优化建图 + 并查集
    	'''
        dsu = DisjointSetUnion()
        for x, y in stones:
            dsu.unionSet(x, y + 10000)
        return len(stones) - dsu.numberOfConnectedComponent()
class DisjointSetUnion:
    def __init__(self):
        self.f = dict()
        self.rank = dict()
    
    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            return x
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)




