import copy

class Twitter:
    def __init__(self):
        self.all_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)
        self.priority = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_tweets[userId].append((self.priority, tweetId))
        self.priority -= 1
        if len(self.all_tweets[userId]) > 10:
            del self.all_tweets[userId][0]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        userIds = self.user_follows[userId]
        userIds.add(userId)
        feed = []
        heap = []

        for uId in userIds:
            print(userId, ' follows ', uId)
            for p, c in self.all_tweets[uId]:
                print('p,c', p, c)
                heapq.heappush(heap, (p,c))
        print('uId', userId, 'heap', heap)

        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId) 
        
