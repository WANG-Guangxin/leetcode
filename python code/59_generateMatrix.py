59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        dirct = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 1
        i = j = 0
        cur_d = 0
        up,down,left,right = 1,n-1,0,n-1
        while count <= n**2:
            res[i][j] = count
            if cur_d == 0 and j == right:
                cur_d += 1
                right -= 1
            elif cur_d == 1 and i == down:
                cur_d += 1
                down -= 1
            elif cur_d == 2 and j == left:
                cur_d += 1
                left += 1
            elif cur_d == 3 and i == up:
                cur_d += 1
                up += 1
            cur_d = cur_d % 4
            i += dirct[cur_d][0]
            j += dirct[cur_d][1]
            count += 1
        return res

