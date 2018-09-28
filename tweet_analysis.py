import twitter


from credentials import twitterConfig


class Tweets:

    def __init__(self):

        self.twitter_api = twitter.Api(
            consumer_key=twitterConfig['consumer_key'],
            consumer_secret=twitterConfig['consumer_secret'],
            access_token_key=twitterConfig['token'],
            access_token_secret=twitterConfig['token_secret'],
            tweet_mode='extended',
            sleep_on_rate_limit=True
        )

        # Define the location id for the UK
        self.WOEID = 23424975 

        # Define language of tweets
        self.LANG = "en"

        # Define type of tweets we are after
        self.TWEETS_TYPE = "recent"

        # Save tweet subjects for later 
        self.data = {}


    def test(self):
        print(self.LANG)


    def get_trending(self):
        """
        Not guaranteed to return the number of results specified.

        Only some results have a tweet_volume property, it's also only for the previous 24 hours.

        So there may not be many current tweets about the same subject.

        By default returns top 50 trending tweets.
        """
        trending_tweets = []
        top_trends = self.twitter_api.GetTrendsWoeid(self.WOEID)

        for trend in top_trends:
            local_dict = {}
            local_dict['name'] = trend.name
            local_dict['query'] = trend.query

            trending_tweets.append(local_dict)

        # sets up the data values used to get tweets later
        for trend in trending_tweets:
            data[trend['name']] = []

        print(trending_tweets)



def main():
    t = Tweets()
    t.get_trending()


if __name__ == '__main__':
    main()
