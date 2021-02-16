给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

 

示例 1：

输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：

我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
示例 2：

输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
示例 3：

输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4
示例 4：

输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000
示例 5：

输入：points = [[0,0]]
输出：0
 

提示：

1 <= points.length <= 1000
-106 <= xi, yi <= 106
所有点 (xi, yi) 两两不同。

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    	'''
    	自己写的代码  
    	一开始想用 findmin 函数来找 最小边 
    	但是执行超时 
    	排序就能通过
    	难道排序比直接找最小更节省时间？排序是 n*log(n)  找的话 应该是 n^2
    	'''
        n = len(points)
        if n == 1:return 0
        edges = []
        for i in range(n):
            for j in range(i):
                if i != j:
                    edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]),i,j))
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
        # def findmin(edges):
        #     Min = edges[0]
        #     ind = 0
        #     for i,x in enumerate(edges):
        #         if x[2] < Min[2]:
        #             Min = x
        #             ind = i
        #     edges.pop(ind)
        #     return Min
        edges.sort()
        cost = count = 0
        for x,i,j in edges:
            if unionset(i,j,parent,rank):
                count += 1
                cost += x
                if count == n-1:break
        return cost



class DisjointSetUnion:
	'''
	官方题解
	'''
	def __init__(self, n):
		self.n = n
		self.rank = [1] * n
		self.f = list(range(n))

	def find(self, x:int) -> int:
		if self.f[x] == x:
			return x
		self.f[x] = self.find(self.f[x])
		return self.f[x]

	def unionSet(self,x:int ,y:int) -> bool:
		fx, fy = self.find(x),self.find(y)
		if fx == fy:
			return False
		if self.rank[fx] < self.rank[fy]:
			fx,fy = fy,fx

		self.rank[fx] += self.rank[fy]
		self.f[fy] = fx
		return True

class Solution:
	def minCostConnectPoints(self,points: List[List[int]]) -> int:
		dist = lambda x,y:abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

		n = len(points)
		dsu = DisjointSetUnion(n)
		edges = list()

		for i in range(n):
			for j in range(i+1,n):
				edges.append((dist(i,j),i,j))

		edges.sort()

		ret , num = 0,1
		for length,x,y in edges:
			if dsu.unionSet(x,y):
				ret += length
				num += 1
				if num == n:
					break

		return ret