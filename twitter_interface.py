
import string
import twitter

from twitter_config import twitterConfig


class TwitterInterface(object):
    def __init__(self):
        # Define the location id for the UK
        # self.WOEID = 23424975

        # world
        self.WOEID = 1

        # Define language of tweets
        self.LANG = "en"
        # Define type of tweets we are after
        self.TWEETS_TYPE = "recent"

        self.api = twitter.Api(
            consumer_key=twitterConfig['consumer_key'],
            consumer_secret=twitterConfig['consumer_secret'],
            access_token_key=twitterConfig['token'],
            access_token_secret=twitterConfig['token_secret'],
            tweet_mode='extended',
            sleep_on_rate_limit=True
        )

        # Used to get rate limit info.
        self.api.InitializeRateLimit()
        rate_limit_dict = self.api.rate_limit.resources

    @staticmethod
    def isEnglish(s):
        try:
            s.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True

    def get_trending(self):
        """
        Returns current trending tweet topics.

        Some may not have a volume.

        Filters for latin chars only.
        """
        trends = []
        # tweet volume is the number of tweets using the hashtag
        trending = self.api.GetTrendsCurrent()

        for trend in trending:
            # print(type(trend), trend.name)
            if self.isEnglish(trend.name) and self.isEnglish(trend.query):
                trends.append(trend.AsDict())

        return trends

    def get_top_trends(self):
        """
        Returns a list of dicts each representing a trending topic.

        Dicts are sorted by tweet volume.
        """
        trends = []
        top_trends = self.api.GetTrendsWoeid(self.WOEID)

        for trend in top_trends:
            # Not all tweets have a volume value, this gets only those that do
            # and only those using latin alphabet.
            if trend.volume and self.isEnglish(trend.name):
                trends.append(trend.AsDict())

        return list(reversed(sorted(trends, key=lambda k: k['tweet_volume'])))

    def search_tweets(self, topic, limit=100):
        """
        Get 100 tweets on a particular topic.

        Accepts a string that is the topic of interest.

        Returns upto 100 tweets although this is not guaranteed to return 100.
        """

        search_term = topic + ' -filter:retweets'

        query = self.api.GetSearch(
            search_term,
            count=limit,
            lang=self.LANG,
            result_type=self.TWEETS_TYPE,
            include_entities=False
        )

        return query


if __name__ == "__main__":
    ti = TwitterInterface()
    # print(dir(ti.api.GetTrendsCurrent()))
    # ti.get_trending()
    # trends = ti.get_top_trends()
    # trends = ti.get_trending()

    # print(len(trends))

    # for trend in trends:
    #     print(trend)

    search_query = ti.search_tweets('futurama')
    print(search_query)
    # print(search_query)
    # print(len(search_query))

    # for trend in trends:
    #     import sentiment_topic as st
    #     st.get_sentiment(trend['name'])
