from twython import TwythonStreamer
import csv
import wget


credentials = {}
credentials['CONSUMER_KEY'] = ""
credentials['CONSUMER_SECRET'] = ""
credentials['ACCESS_TOKEN'] = ""
credentials['ACCESS_SECRET'] = ""


# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    if "retweeted_status" not in tweet:
        if 'entities' in tweet:
            if 'media' in tweet['entities']:
                d["ID"] = tweet['id']
                d['text'] = tweet['text'].encode("utf-8")
                d['media_url'] = tweet['entities']['media'][0]['media_url']
    return d


# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):

    # Received data
    def on_success(self, data):
        # Only collect tweets in English
        if data['lang'] == 'en':
            if "retweeted_status" not in data:
                if 'entities' in data:
                    if 'media' in data['entities']:
                        tweet_data = process_tweet(data)
                        self.save_to_csv(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(tweet.values())
            wget.download(tweet['media_url'], "D:\Twitter\image")
        print(tweet)


# Instiate from our streaming class
stream = MyStreamer(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'],
                    credentials['ACCESS_TOKEN'], credentials['ACCESS_SECRET'])
# Start the stream
stream.statuses.filter(track=["Halloween","PennState"])
