# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 
#  👍 300 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if pivot_element == target:
                return True
            elif pivot_element > target:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
