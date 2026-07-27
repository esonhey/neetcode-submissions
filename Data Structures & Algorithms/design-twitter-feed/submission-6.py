import copy

class Twitter:
    def __init__(self):
        self.all_tweets = {}
        self.user_follows = {}
        self.priority = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        li =  self.all_tweets.get(userId, [])

        li.append((self.priority, tweetId))
        self.priority -= 1
        if len(li) > 10:
            del li[0]
        self.all_tweets[userId] = li
        

    def getNewsFeed(self, userId: int) -> List[int]:
        userIds = [userId] + self.user_follows.get(userId, [])
        feed = []
        heap = []
        heapq.heapify(heap)

        for uId in userIds:
            for p, c in self.all_tweets.get(uId,[]):
                heapq.heappush(heap, (p,c))
        print('heap', heap)

        while heap and len(feed) < 10:
            print('feed', feed)
            feed.append(heapq.heappop(heap)[1])
        print('feed', feed)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.user_follows.get(followerId,[]): 
            self.user_follows[followerId] = self.user_follows.get(followerId, []) + [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.user_follows or followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId) 
        
