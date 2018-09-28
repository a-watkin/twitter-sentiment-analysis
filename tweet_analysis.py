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





def main():
    t = Tweets()



if __name__ == '__main__':
    main()
