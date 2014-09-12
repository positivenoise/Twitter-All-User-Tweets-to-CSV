import tweepy
import csv
import sys

#Twitter API credentials
consumer_key = "insert api credentials here"
consumer_secret = "insert api credentials here"
access_key = "insert api credentials here"
access_secret = "insert api credentials here"

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    at = []

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    at.extend(new_tweets)

    oldest = at[-1].id - 1
    print "Getting " + screen_name + " tweets"
    while len(new_tweets) > 0:

        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        at.extend(new_tweets)
        oldest = at[-1].id - 1

    ot = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in at]

    with open(screen_name + '.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(ot)

    print "Completed"
    pass

if __name__ == '__main__':

    get_all_tweets(sys.argv[1])