给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        A = nums[-1]
        B = nums[-2]
        C = nums[-3]
        D = nums[0]
        E = nums[1]
        return A*B*C if A*B*C > A*D*E else A*D*E