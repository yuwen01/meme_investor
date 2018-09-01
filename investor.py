import praw
import datetime as dt
import time
import numpy as np
import pandas as pd
import math
import sys

NUMPOSTS = 25
reddit = praw.Reddit('investor')
#early: 20-30 minutes old
#mid: 60-75 minutes old
#mature: >5 hrs old
#numComments: early comments number
columns = ['title', 'earlyScore', 'midScore', 'numComments', 'matureScore']
df = pd.DataFrame(columns=columns)

subreddit = reddit.subreddit("memeeconomy")
ct = 0
def get_date(sub):

    time = sub.created
    return dt.datetime.fromtimestamp(time)

def getAgeMinutes(sub):
    createdTime = sub.created - 8 * 3600 #to account for time difference
    ageMinutes = (-createdTime + time.mktime(dt.datetime.now().timetuple()))/60
print(str(dt.datetime.now()))

#main
investedPosts =['']
ct = 0
while True:
    for submission in subreddit.new(limit=20):
        createdTime = submission.created - 8 * 3600 #to account for time difference
        ageMinutes = (-createdTime + time.mktime(dt.datetime.now().timetuple()))/60

        if (ageMinutes < 25) & (ageMinutes > 20) & (submission.score > 30) & (submission.id not in investedPosts):
            #print('right range')
            for topLevelComment in submission.comments:
                print(topLevelComment.author)
                if topLevelComment.author == 'MemeInvestor_bot':
                    print('gotem ' + submission.title)
                    topLevelComment.reply('!invest 100')
                    break

            investedPosts.append(submission.id)

