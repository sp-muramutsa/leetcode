from collections import defaultdict


class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_count += 1
        self.tweets[userId].append((-self.tweet_count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        max_heap = []
        users = self.following[userId].union({userId})

        # Each user's most recent tweets
        for user_id in users:
            tweets = self.tweets[user_id]
            n = len(tweets)
            if n > 0:
                latest_timestamp, last_tweet_id = tweets[-1]
                heapq.heappush(max_heap, (latest_timestamp, last_tweet_id, n - 1, user_id))

       
        # Lazy loading till we get 10 most recent tweets
        top_10_tweets = []
        while max_heap:
            timestamp, tweet_id, index, user_id = heapq.heappop(max_heap)

            if index - 1 >= 0:
                latest_timestamp, last_tweet_id = self.tweets[user_id][index - 1]
                heapq.heappush(max_heap, (latest_timestamp, last_tweet_id, index - 1, user_id))

            top_10_tweets.append(tweet_id)

            if len(top_10_tweets) == 10:
                break

        return top_10_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

