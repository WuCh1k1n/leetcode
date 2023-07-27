# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个
# 功能： 
# 
#  
#  postTweet(userId, tweetId): 创建一条新的推文 
#  getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
#  
#  follow(followerId, followeeId): 关注一个用户 
#  unfollow(followerId, followeeId): 取消关注一个用户 
#  
# 
#  示例: 
# 
#  
# Twitter twitter = new Twitter();
# 
# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
# twitter.postTweet(1, 5);
# 
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# twitter.getNewsFeed(1);
# 
# // 用户1关注了用户2.
# twitter.follow(1, 2);
# 
# // 用户2发送了一个新推文 (推文id = 6).
# twitter.postTweet(2, 6);
# 
# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# twitter.getNewsFeed(1);
# 
# // 用户1取消关注了用户2.
# twitter.unfollow(1, 2);
# 
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
# twitter.getNewsFeed(1);
#  
#  Related Topics 设计 哈希表 链表 堆（优先队列） 
#  👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Twitter:
    class Node:
        def __init__(self):
            self.followee = set()
            self.tweet = list()

    def __init__(self):
        self.time = 0
        self.recentMax = 10
        self.tweetTime = dict()
        self.user = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user:
            self.user[userId] = Twitter.Node()
        self.user[userId].tweet.append(tweetId)
        self.time += 1
        self.tweetTime[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user:
            return list()
        ans = self.user[userId].tweet[-self.recentMax:][::-1]
        for followeeId in self.user[userId].followee:
            if followeeId in self.user:
                opt = self.user[followeeId].tweet[-self.recentMax:][::-1]
                i, j, combined = 0, 0, list()
                while i < len(ans) and j < len(opt):
                    if self.tweetTime[ans[i]] > self.tweetTime[opt[j]]:
                        combined.append(ans[i])
                        i += 1
                    else:
                        combined.append(opt[j])
                        j += 1
                combined.extend(ans[i:])
                combined.extend(opt[j:])
                ans = combined[:self.recentMax]
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.user:
                self.user[followerId] = Twitter.Node()
            self.user[followerId].followee.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user:
                self.user[followerId].followee.discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# leetcode submit region end(Prohibit modification and deletion)
