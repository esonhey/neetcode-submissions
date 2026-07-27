import copy

class Twitter:
    def __init__(self):
        self.all_tweets = defaultdict(list)
        self.user_follows = defaultdict(list)
        self.priority = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_tweets[userId].append((self.priority, tweetId))
        self.priority -= 1
        if len(self.all_tweets[userId]) > 10:
            del self.all_tweets[userId][0]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        userIds = [userId] + self.user_follows.get(userId, [])
        feed = []
        heap = []
        heapq.heapify(heap)

        for uId in userIds:
            for p, c in self.all_tweets.get(uId,[]):
                heapq.heappush(heap, (p,c))

        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.user_follows.get(followerId,[]): 
            self.user_follows[followerId] += [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.user_follows or followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId) 
        
