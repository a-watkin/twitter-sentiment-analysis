
import os
import datetime

try:
    from tools.twitter.twitter_interface import TwitterInterface
except Exception as e:
    from twitter_interface import TwitterInterface

import pandas as pd

# Sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class TwitterDataAnalysis(TwitterInterface):
    def __init__(self):
        super().__init__()

    def get_search_topic_tweets(self, topic, limit=100):
        tweet_data = []
        tweets = super().search_tweets(topic, limit)
        analyser = SentimentIntensityAnalyzer()

        for tweet in tweets:
            local_dict = {}
            if topic in tweet.full_text:
                local_dict['name'] = topic
                local_dict['id'] = tweet.id_str
                local_dict['full_text'] = str(tweet.full_text)
                vs = analyser.polarity_scores(tweet.full_text)
                local_dict['neg'] = vs['neg']
                local_dict['neu'] = vs['neu']
                local_dict['pos'] = vs['pos']
                local_dict['compound'] = vs['compound']

                tweet_data.append(local_dict)

        return tweet_data

    def make_initial_df(self, data):
        tweet_df = pd.DataFrame(data)
        return tweet_df

    def make_histograms(self, data, name):
        """
        Function to build the histograms and write the results to separate files.
        """
        # Importing here to prevent auto linters from messing with the order.
        import matplotlib
        # NOT using the default of TTK because it sometimes crashes.
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        try:
            # this doesn't work for outputting graphs
            # matplotlib.use('Agg')
            plt.figure(figsize=(20, 10))
            plt.hist(data, width=0.1)

            plt.title('Trend name: {} \nOverall sentiment: {} '
                      '\nTotal samples: {}'.format(
                          name, round(sum(data), 2), len(data)))

            plt.xlabel('Compound sentiment')
            plt.ylabel('Samples')

            file_name = '{}.png'.format(name)
            file_path = os.path.join(self.get_save_path(), file_name)

            plt.savefig(
                file_path
            )

            # Prevents the plt from being stored in memory.
            # Might be causing a problem.
            plt.close()

            # for use in the frontend
            return self.get_img_path(file_path)
        except Exception as e:
            print(e, 'tkinter problem? ', e)

    def get_sentiment(self, topic):
        tweet_data = self.get_search_topic_tweets(topic, 100)
        if len(tweet_data) > 0:
            df = self.make_initial_df(tweet_data)
            file_path = self.make_histograms(df['compound'].values, topic)
            if file_path:
                return file_path

        return tweet_data

    def get_top_trends_sentiment(self):
        """
        Gets the the trends that have tweet_volume.

        Outputs sentiment frequency charts for each tweet.
        """
        trends = super().get_top_trends()
        for trend in trends:
            self.get_sentiment(trend['name'])

    def get_trends_sentiment(self):
        """
        Gets all trending topics regardless of tweet_volume.

        Outputs sentiment frequency charts for each tweet.
        """
        trends = super().get_trending()
        for trend in trends:
            self.get_sentiment(trend['name'])

    @staticmethod
    def get_save_path():
        """
        Returns the path to save graphs in the format of year-month-day in a subdirectory.
        """
        # location to save graphs
        save_path = os.path.join(os.getcwd(), 'static', 'graphs')
        # save in a folder by month and day
        date = datetime.datetime.now()
        save_dir = os.path.join(
            save_path, '{}-{}-{}'.format(date.year, date.month, date.day))
        # check if path exists, create if not
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        return save_dir

    def get_img_path(self, file_path):
        path = file_path
        split_path = path.split('/')
        return '/' + '/'.join(split_path[len(split_path) - 4:])


if __name__ == "__main__":
    # print(
    #     os.path.join(os.getcwd(), 'graphs')
    # )

    tda = TwitterDataAnalysis()
    # print(tda.get_img_path())
    # print(tda.get_save_path())

    # trends = tda.get_top_trends()
    # for trend in trends:
    #     print(trend)
    # print(tda.get_sentiment('eggs'))

    tda.get_sentiment('git')
    # tda.get_top_trends_sentiment()
    # tda.get_trends_sentiment()

    # my_path = os.path.abspath(__file__)
    # print(my_path)
