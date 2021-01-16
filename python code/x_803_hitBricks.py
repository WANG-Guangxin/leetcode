
有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

一块砖直接连接到网格的顶部，或者
至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

 

示例 1：

输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：
网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2] 。
示例 2：

输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：
网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0], 
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0] 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] 为 0 或 1
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
所有 (xi, yi) 互不相同


class UnionFind:
	def __init__(self):
		self.father = {}
		self.size_of_set = {}

	def get_size_of_set(self,x):
		'''
		获取所在连通块的大小
		'''
		return self.size_of_set[self.find(x)]

	def find(size,x):
		root = x

		while self.father[root] != None:
			root = self.father[root]

		# 路径压缩
		while x != root:
			original_father = self.father[x]
			self.father[x] = root
			x = original_father
		
		return root

	def is_connected(self,x,y):
		return self.find(x) == self.find(y)

	def merge(self,x,y):
		root_x,root_y = self.find(x),self.find(y)

		if root_x != root_y:
			self.father[root_x] = root_y
			# 更新根节点连通块数量
			self.size_of_set[root_y] += self.size_of_set[root_x]
			del self.size_of_set[root_x]

	def add(self,x):
		if x not in self.father:
			self.father[x] = None
			self.size_of_set[x] = 1



class Solution:
	def __init__(self):
		self.CEILING = (-1,-1)
		self.DIRECTION = ((1,0),(-1,0),(0,1),(0,-1))

	def initalize(self,uf,m,n,grid,hits):
		'''
		初始化
		'''
		# 添加天花板
		uf.add(self.CEILING)

		# 敲掉所有要敲掉的砖块
		for x,y in hits:
			grid[x][y] -= 1

		# 连接，合并剩余的砖块
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					uf.add((i,j))

		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					self.merge_neighbors(uf,m,n,grid,i,j)

		# 与天花板合并
		for j in range(n):
			if grid[0][j] == 1:
				uf.merge((0,j),self.CEILING)

	def is_valid(self,x,y,grid,m,n):
		return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

	def merge_neighbors(self,uf,m,n,grid,x,y):
		'''
		与上下左右的砖块合并
		'''
		for dx,dy in self.DIRECTION:
			nx,ny = x + dx,y+dy
			if not self.is_valid(nx,ny,grid,m,n):
				continue
			uf.merge((x,y),(nx,ny))


    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    	uf = UnionFind()
    	m,n = len(grid),len(grid[0])
    	res = [0] + len(hits)

    	# 初始化
    	self.initalize(uf,m,n,grid,hits)

    	for i in range(len(hits)-1,-1,-1):
    		x,y = hits[i][0],hits[i][1]

    		# 还原敲击
    		grid[x][y] += 1

    		# 敲的地方原本就不是砖块
    		if grid[x][y] != 1:
    			continue