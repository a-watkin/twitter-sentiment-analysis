import twitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pandas as pd

from credentials import twitter_config


class Tweets:

    def __init__(self):

        self.twitter_api = twitter.Api(
            consumer_key=twitter_config['consumer_key'],
            consumer_secret=twitter_config['consumer_secret'],
            access_token_key=twitter_config['token'],
            access_token_secret=twitter_config['token_secret'],
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
            self.data[trend['name']] = []

        print(trending_tweets)

    def get_tweets(self):

        for tweet_subject in self.data.keys():
            print(tweet_subject)

            query = self.twitter_api.GetSearch(
                tweet_subject,
                count=100,
                lang='en',
                result_type="recent",
                include_entities=False
            )

            analyser = SentimentIntensityAnalyzer()

            for tweet in query:
                if tweet.id in self.data[tweet_subject]:
                    break

                else:
                    self.data[tweet_subject].append(tweet.id)
                    tweet_data = []

                    vs = analyser.polarity_scores(tweet.full_text)

                    # used as a key for checking against the file
                    tweet_data.append(tweet.id)
                    tweet_data.append(tweet_subject)

                    # text of the tweet object
                    tweet_data.append(tweet.full_text)

                    # csv module requires list items to be a string
                    tweet_data.append(str(vs['neg']))
                    tweet_data.append(str(vs['neu']))
                    tweet_data.append(str(vs['pos']))
                    tweet_data.append(str(vs['compound']))

                    try:
                        self.data[tweet_subject].append(tweet_data)

                    except Exception as e:
                        print(e, self.data.keys())

    # def exp(self):

    #     query = self.twitter_api.GetSearch(
    #         count=10,
    #         lang='en',
    #         result_type="recent",
    #         include_entities=False
    #     )

    #     print(query)


def main():
    t = Tweets()
    t.get_trending()
    # print(type(t.data))
    # print(t.data)

    t.get_tweets()

    print(t.data)

    # t.exp()


if __name__ == '__main__':
    main()
