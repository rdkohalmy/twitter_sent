# Twitter Sentiment Analysis

This code was written by following a tutorial from the [Computer Science](https://www.youtube.com/channel/UCbmb5IoBtHZTpYZCDBOC1CA) YouTube channel.
There are some variants in how a few tasks are accomplished because that is how I already knew to reach the goal that block of code is tasked to do.
This project was made to further my education on Python and Data Science as well as to give me a tool quickly do some research on a company that I am
applying to for a job, or who has reached out to me for my resume.

### Requirements
* Python3
* Tweepy
* TextBlob
* Pandas
* Numpy
* Re
* Matplotlib
* Twitter API application for API keys
  * More info [here](https://developer.twitter.com/)

### What to change
You will need to add your own API credentials into the twitter_credentials.py file. You will also need to edit the path to export the CSV file.
line 97 `df.to_csv(r'path/to/folder', index=False, header=True)`

#### Why collect 360 Tweets from a user?

The reason for this is that I do not want it to take forever getting the tweets and the industry "standard" for number of tweets per day by a company
is 12. Multiply the number of industry standard daily tweets by 30 days to represent one month of tweets. This should give me a good data set to look
at and make a informed decision.

[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-netflix.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com)
