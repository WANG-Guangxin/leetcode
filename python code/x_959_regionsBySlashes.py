r'''
在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

返回区域的数目。

 

示例 1：

输入：
[
  " /",
  "/ "
]
输出：2
解释：2x2 网格如下：

示例 2：

输入：
[
  " /",
  "  "
]
输出：1
解释：2x2 网格如下：

示例 3：

输入：
[
  "\\/",
  "/\\"
]
输出：4
解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
2x2 网格如下：

示例 4：

输入：
[
  "/\\",
  "\\/"
]
输出：5
解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
2x2 网格如下：

示例 5：

输入：
[
  "//",
  "/ "
]
输出：3
解释：2x2 网格如下：

 

提示：

1 <= grid.length == grid[0].length <= 30
grid[i][j] 是 '/'、'\'、或 ' '。
'''

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        class unionfind:
            def __init__(self,n):
                self.parent = list(range(n*n + 2*n +2))
                self.area = 1

            def find(self,x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self,x,y):
                xroot = self.find(x)
                yroot = self.find(y)
                self.parent[xroot] = yroot

            def isClosed(self,x,y):
                xroot = self.find(x)
                yroot = self.find(y)
                if xroot == yroot:
                    self.area += 1
                    return True
                else:
                    return False


        n = len(grid)
        uf = unionfind(n)

    	# 连接边缘
        node = n*n + 2*n + 1
        for i in range(n+1):
            uf.union(node,i) # 连接上边缘
            uf.union(node,n*n +n +i) # 连接下边缘
            uf.union(node,i*(n+1)) # 连接左边缘
            uf.union(node,i*(n+1) + n) #连接右边缘

    	# 连接斜杠
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    node1 = (n+1) * (i+1) + j
                    node2 = (n+1) * i + (j+1)
                    if not uf.isClosed(node1,node2):
                        uf.union(node1,node2)
                elif grid[i][j] == '\\':
                    node1 = (n+1) *i +j
                    node2 = (n+1) * (i+1) +(j+1)
                    if not uf.isClosed(node1,node2):
                        uf.union(node1,node2)

        return uf.area
