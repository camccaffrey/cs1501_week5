'''
Author: Connor McCaffrey
email ID: cam7qp
Date: 10-13-2021

Description: This program searches the first 25 tweets on my Twitter timeline and prints
             the one with the most likes along with the username and time created.
'''

import tweepy

auth = tweepy.OAuthHandler("nvSVcrNQTdn7Fkti5EBLdfgfX","70XQ2ytgfxsE0vpBRQZH6jyPthIceiLo92xjqCXi05UhcoH8YY")
auth.set_access_token("1448457173101592577-OM3QDIcaeRYFYjObgJbIwV3UfMXMqU", "um1noevNOUyeYSdr6YMdvPgGXld1er6nap67dmnptIOAc")

api = tweepy.API(auth)


timeline = api.home_timeline()

maxLikes = 0
bestTweet = None

count = 25
i = 1

for tweet in timeline:
    if( i > 25 ):
        break
    else:
        if( tweet.favorite_count > maxLikes ):
            maxLikes = tweet.favorite_count
            bestTweet = tweet
        i = i + 1

print("At " + str(bestTweet.created_at) + ", " + bestTweet.user.name + " (" + str(maxLikes) + " likes) tweeted, '" + bestTweet.text + "'")
