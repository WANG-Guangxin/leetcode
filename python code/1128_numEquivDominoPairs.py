给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

 

示例：

输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
 

提示：

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    	'''
    	二重循环超时
    	后来想到使用字典 哈希 这些方法 但是没有实现好
    	最后想着映射到二维矩阵里 再计算
    	这样做还涉及一些 细节 又加了几个判断调试一下 才通过
    	'''
        edges = [[0] * 9 for _ in range(9)]
        nums = 0
        for x,y in dominoes:
            if x == y:
                edges[x-1][y-1] += 1
            else:
                edges[x-1][y-1] += 1
                edges[y-1][x-1] += 1
        for i in range(9):
            for j in range(i,9):
                tmp = (edges[i][j]*(edges[i][j]-1))/2
                nums += tmp
        return int(nums)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    	'''
    	用字典的方式
    	'''
        dic = dict()
        res = 0
        for dom in dominoes:
            if dom[1] < dom[0]:
                dom = (dom[1],dom[0])
            else:
                dom = (dom[0],dom[1])
            if dom not in dic:
                dic[dom] = 1
            else:
                dic[dom] += 1
        for key in dic:
            if dic[key] > 1:
                res += dic[key]*(dic[key]-1)//2
        return res


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    	'''
    	官方题解的做法
    	把（x,y）-> 10x + y
    	循环里先累加到结果 再加一的方式很妙
    	其实节约了 等差数列求和的过程
    	'''
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val] 
            num[val] += 1
        return ret

