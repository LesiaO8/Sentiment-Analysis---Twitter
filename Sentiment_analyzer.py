import tweepy
from textblob import TextBlob

consumer_key="ENTER YOUR CONSUMER KEY"
consumer_secret="ENTER YOUR CONSUMER SECRET KEY"

access_token="ENTER YOUR ACCESS TOKEN"
access_token_secret="ENTER YOUR SECRET ACCESS TOKEN"

#for authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

#Keyword we are using is "Global Warming" 
public_tweets = api.search("Global Warming")

#output the sentiment tuple to a file and process the data per your requirements
with open("output.txt", 'a') as the_file:
    for tweet in public_tweets:
        #print(tweet.text)
        analysis = TextBlob(tweet.text)
        #write the sentiment tuple to the output file
        the_file.write(str(analysis.sentiment) + "\n")
