# This Python program is written by Ryan Kohalmy with the assistance an educational guide
# as a resume project while I am learning Python and Data Science. A lot of code is similar
# to the guide from the Computer Science YouTube (https://www.youtube.com/watch?v=ujId4ipkBio&t=3s)
# tutorial but I have added my own take on some of the code that I have learned from other resources.
# If you have questions feel free to reach out to me on GitHub (rdkohalmy) or on Twitter (kingkolGG).

# Resources needed to make it work
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethrityeight')

#Authentification for Twitter API
import twitter_credentials
consumerKey = twitter_credentials.CONSUMER_KEY()
consumerSecret = twitter_credentials.CONSUMER_SECRET()
accessToken = twitter_credentials.ACCESS_TOKEN()
accessSecret = twitter_credentials.ACCESS_SECRET()

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)

auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Set variable usrName by asking the user what the Twitter handle is.
usrName = input('what is the Twitter handle of the orginization? ')

# Use Twitter API to grab the last 500 tweets from the above input.
# See GitHub README.md for reasoning behind 360 tweets.
posts = api.user_timeline(screen_name = usrName, count= 500, lang= "en", tweet_mode="extended")
i = 1
print("Show the 5 more recent tweets: \n")
for tweet in posts[0:5]:
    print(str(i) + ') ' + tweet.full_text + '/n')
    i = i + 1

# Here we are making a data frame with pandas to store, orginize, and later visualize the tweets.
df = pd.DataFrame( [tweet.full_text for tweet in posts], columns=['Tweets'])
df.head()

# Here we remove the links in the tweets, we are leaving the @mentions so we can investigate
# those accounts if we want to. We also leave hashtags for further research.
def cleanTxt(text):
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text

df['Tweets']= df['Tweets'].apply(cleanTxt)

df

# Here we will look at the Subjectivity and Polarity or each tweet that we collected.
def getSubjectivity(text):
     return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Let's put that new information and put it into our data frame.
df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)

df

# Here we will take the score fo each tweet's polarity score and we can make correlations.
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

df['Analysis'] = df['Polarity'].apply(getAnalysis)

df

# Now let's plot some charts to let ourselves see what side of the polarity spectrum
# this orginization is most consistant on.
plt.figure(figsize=(8,6))
for i in range(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show

# Lastly we are going to export our DataFrame to a CSV file if you want to import
# this data into a SQL database for visualization by software like metabase or to
# be able to refer to it later.

df.to_csv(r'path/to/folder', index=False, header=True)
