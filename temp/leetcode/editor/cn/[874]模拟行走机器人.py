# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令： 
# 
#  
#  -2：向左转 90 度 
#  -1：向右转 90 度 
#  1 <= x <= 9：向前移动 x 个单位长度 
#  
# 
#  在网格上有一些格子被视为障碍物。 
# 
#  第 i 个障碍物位于网格点 (obstacles[i][0], obstacles[i][1]) 
# 
#  机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。 
# 
#  返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。 
# 
#  
# 
#  示例 1： 
# 
#  输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#  
# 
#  示例 2： 
# 
#  输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= commands.length <= 10000 
#  0 <= obstacles.length <= 10000 
#  -30000 <= obstacle[i][0] <= 30000 
#  -30000 <= obstacle[i][1] <= 30000 
#  答案保证小于 2 ^ 31 
#  
#  Related Topics 贪心算法 
#  👍 121 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacles = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
