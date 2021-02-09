K 个不同整数的子数组

给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。

（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

返回 A 中好子数组的数目。

 

示例 1：

输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        官方题解
        '''
        n = len(A)
        num1, num2 = collections.Counter(), collections.Counter()
        tot1 = tot2 = 0
        left1 = left2 = right = 0
        ret = 0

        for right, num in enumerate(A):
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1
            
            while tot1 > K:
                num1[A[left1]] -= 1
                if num1[A[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > K - 1:
                num2[A[left2]] -= 1
                if num2[A[left2]] == 0:
                    tot2 -= 1
                left2 += 1
            
            ret += left2 - left1
        
        return ret






class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        超时解法
        '''
        n = len(A)
        if n < K :return 0
        res = 0
        for i in range(n-K+1):
            tmp = set()
            for x in range(i,n):
                if A[x] in tmp and len(tmp) == K:
                    res += 1
                if A[x] not in tmp:
                    tmp.add(A[x])
                    if len(tmp) == K:
                        res += 1
                    elif len(tmp) > K:
                        break
      
        return res