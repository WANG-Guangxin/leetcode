# 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

# 返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。

#  

# 示例 1：

# 输入：[0,1,1]
# 输出：[true,false,false]
# 解释：
# 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
# 示例 2：

# 输入：[1,1,1]
# 输出：[false,false,false]
# 示例 3：

# 输入：[0,1,1,1,1,1]
# 输出：[true,false,false,false,true,false]
# 示例 4：

# 输入：[1,1,1,0,1]
# 输出：[false,false,false,false,false]
#  

# 提示：

# 1 <= A.length <= 30000
# A[i] 为 0 或 1
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    	'''
    	一开始暴力解题  超时了
    	后来看了答案  发现每次增加一个数只是上一个数的左移加当前数值 也就是2倍加当前数值  快了一些
    	再后来发现 被 5 整除只需要记录个位数就行了 也就是除 10 取余数
    	但是，对于个位数 6 ，6 = 1 + 5， 6 * 2 = （1 + 5）* 2，6 * 2 % 10 = (1 + 5) * 2 % 10 = 2 
    	因此每次记录除以 5 的余数即可。 
    	'''
        n = len(A)
        ans = [False] * n
        tmp = 0
        for i in range(n):
            tmp = (tmp * 2 + A[i]) % 5
            if tmp == 0:
                ans[i] = True
        return ans 
