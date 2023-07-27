# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数
# 值排序之后中间两个数的平均值。 
# 
#  例如， 
# 
#  [2,3,4] 的中位数是 3 
# 
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
# 
#  设计一个支持以下两种操作的数据结构： 
# 
#  
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
#  double findMedian() - 返回目前所有元素的中位数。 
#  
# 
#  示例 1： 
# 
#  输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
#  
# 
#  示例 2： 
# 
#  输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000] 
# 
#  
# 
#  限制： 
# 
#  
#  最多会对 addNum、findMedian 进行 50000 次调用。 
#  
# 
#  注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-strea
# m/ 
#  Related Topics 堆 设计 
#  👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))


    def findMedian(self) -> float:
        if self.count & 1:
            return self.max_heap[0][1]
        else:
            return (self.max_heap[0][1] + self.min_heap[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    f = MedianFinder()
    f.addNum(2)
    f.addNum(3)
    f.addNum(4)
    print(f.findMedian())
