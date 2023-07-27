"""
我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形
 i 左下角的坐标，
 (xi1, yi1) 是该矩形 左下角 的坐标，
 (xi2, yi2) 是该矩形 右上角 的坐标。 

 计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。 

 返回 总面积 。因为答案可能太大，返回
 10⁹ + 7 的 模 。 

 

 示例 1： 

 

 
输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
输出：6
解释：如图所示，三个矩形覆盖了总面积为6的区域。
从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
从(1,0)到(2,3)，三个矩形都重叠。
 

 示例 2： 

 
输入：rectangles = [[0,0,1000000000,1000000000]]
输出：49
解释：答案是 10¹⁸ 对 (10⁹ + 7) 取模的结果， 即 49 。
 

 

 提示： 

 
 1 <= rectangles.length <= 200 
 rectanges[i].length = 4
 
 0 <= xi1, yi1, xi2, yi2 <= 10⁹ 
 矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。 
 

 Related Topics 线段树 数组 有序集合 扫描线 👍 196 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        hbound = set()
        for rect in rectangles:
            # 下边界
            hbound.add(rect[1])
            # 上边界
            hbound.add(rect[3])

        hbound = sorted(hbound)
        m = len(hbound)
        # 「思路与算法部分」的 length 数组并不需要显式地存储下来
        # length[i] 可以通过 hbound[i+1] - hbound[i] 得到
        seg = [0] * (m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            # 左边界
            sweep.append((rect[0], i, 1))
            # 右边界
            sweep.append((rect[2], i, -1))
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break

            # 一次性地处理掉一批横坐标相同的左右边界
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                left, right = rectangles[idx][1], rectangles[idx][3]
                for x in range(m - 1):
                    if left <= hbound[x] and hbound[x + 1] <= right:
                        seg[x] += diff

            cover = 0
            for k in range(m - 1):
                if seg[k] > 0:
                    cover += (hbound[k + 1] - hbound[k])
            ans += cover * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % (10 ** 9 + 7)
# leetcode submit region end(Prohibit modification and deletion)
