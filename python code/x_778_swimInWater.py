水位上升的泳池中游泳

在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

 

示例 1:

输入: [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例2:

输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
 

提示:

2 <= N <= 50.
grid[i][j] 是 [0, ..., N*N - 1] 的排列。

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        按照昨天的思路 写了个二分法的代码 
        但是执行超时 不明白到底为什么
        '''
        n = len(grid)
        left ,right ,ans= 0,n*n-1,n*n-1
        while left <= right:
            mid = (left+right) // 2
            q = []
            seen = set()
            if grid[0][0] <= mid:
                q.append((0,0))
            while q:
                x,y = q.pop(0)
                seen.add((x,y))
                for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in seen and grid[nx][ny] <= mid:
                        q.append((nx,ny))
            
            if (n-1,n-1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        别人的 二分法代码  
        对节点换了种编码方式
        少用了很多 append pop 这种方法 就能执行通过了
        '''
        n = len(grid)
        def hasPath(t):
            if grid[0][0]>t:
                return False
            q = []
            seen = [0]*(n**2)
            dirs = [1, 0, -1, 0, 1]
            q.append(0)
            while q:
                x = q[-1] % n
                y = q[-1] // n
                q.pop()
                if x == n - 1 and y == n - 1:
                    return True 
                for i in range(4):
                    tx = x + dirs[i]
                    ty = y + dirs[i+1]
                    if tx < 0 or ty < 0 or tx >=n or ty >= n or grid[tx][ty]>t:
                        continue
                    key = ty*n + tx
                    if seen[key]:
                        continue
                    seen[key] = 1
                    q.append(key)
            return False

        l = 0
        r = n * n 
        while l < r:
            m = l + (r - l) // 2
            if hasPath(m):
                r = m 
            else:
                l = m + 1
        return l


class Solution:
    def swimInWater(self, grid):
        '''
        执行最快的代码
        就是广度优先的队列使用了 堆
        '''
        N = len(grid)
        seen1, seen2 = {(0, 0)}, {(N - 1, N - 1)}
        p = [(grid[0][0], 0, 0)]
        q = [(grid[-1][-1], N - 1, N - 1)]
        ans = 0
        while True:
            d, r, c = heapq.heappop(p)
            ans = max(ans, d)
            if (r, c) in seen2:
                return ans
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen1:
                    heapq.heappush(p, (grid[cr][cc], cr, cc))
                    seen1.add((cr, cc))
            d, r, c = heapq.heappop(q)
            ans = max(ans, d)
            if (r, c) in seen1:
                return ans
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen2:
                    heapq.heappush(q, (grid[cr][cc], cr, cc))
                    seen2.add((cr, cc))

'''=================================================================================
此题还可以使用并查集  最短路径算法  
参考 1631 最小体力消耗路径
'''


