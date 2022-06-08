# Python Script to Extract tweets of a
# particular Hashtag using Tweepy and Pandas

# import modules
import pandas as pd
import tweepy


class col:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# function to display data of each tweet
def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Time: {ith_tweet[0]}")
    print(f"Username:{ith_tweet[1]}")
    print(f"Description:{ith_tweet[2]}")
    print(f"Location:{ith_tweet[3]}")
    print(f"Following Count:{ith_tweet[4]}")
    print(f"Follower Count:{ith_tweet[5]}")
    print(f"Total Tweets:{ith_tweet[6]}")
    print(f"Retweet Count:{ith_tweet[7]}")
    print(f"Tweet Text:{ith_tweet[8]}")
    print(f"Hashtags Used:{ith_tweet[9]}")


# function to perform data extraction
def scrape(words, date_since, numtweet):

    # Creating DataFrame using pandas
    db = pd.DataFrame(
        columns=[
            "date",
            "unix",
            "retweetcount",
            "text",
        ]
    )

    # We are using .Cursor() to search
    # through twitter for the required tweets.
    # The number of tweets can be
    # restricted using .items(number of tweets)
    tweets = tweepy.Cursor(
        api.search_tweets, words, lang="en", since_id=date_since, tweet_mode="extended"
    ).items(numtweet)

    # .Cursor() returns an iterable object. Each item in
    # the iterator has various attributes
    # that you can access to
    # get information about each tweet
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        date = tweet.created_at.strftime("%Y-%m-%d")
        time = tweet.created_at.timestamp()
        retweetcount = tweet.retweet_count
        # Retweets can be distinguished by
        # a retweeted_status attribute,
        # in case it is an invalid reference,
        # except block will be executed
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text

        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [date, time, retweetcount, text]

        if ith_tweet[2] > 100:
            db.loc[len(db)] = ith_tweet
            print(ith_tweet[2])
            i = i + 1
        else:
            continue
    filename = "scraped_tweets.csv"

    # we will save our database as a CSV file.
    db.to_csv(filename)


if __name__ == "__main__":

    # Enter your own credentials obtained
    # from your developer account
    consumer_key = "L2BKElNco18WhHak3NkCM05t4"
    consumer_secret = "DXL2KqEegX03uJbQNPxecGFqPiKUhw5vCpnzukiL3OvxFaJIiF"
    access_key = "1042321525901152256-Po8en0crJfjW74hUWUgKt34n5AAAlP"
    access_secret = "74bEpnfXM8O3Or3kajQERMeTjJVoYJFGXamUa5qDopE7y"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Enter Hashtag and initial date
    words = "crypto"
    date_since = "2021--01--01"

    # number of tweets you want to extract in one run
    numtweet = 100
    scrape(words, date_since, numtweet)
    print("Scraping has completed!")
