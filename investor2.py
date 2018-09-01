import praw
import datetime as dt
import time
import pandas as pd

reddit = praw.Reddit('investor')
#early: 20-30 minutes old
#mid: 60-75 minutes old
#mature: >5 hrs old
columns = ['id', 'earlyUpvotes', 'midUpvotes', 'numComments','upvotesMature']
df = pd.DataFrame(columns=columns)
subreddit = reddit.subreddit("memeeconomy")
ct = 0
def get_date(sub):
    time = sub.created
    return dt.datetime.fromtimestamp(time)

for submission in subreddit.new(limit=5):
    createdTime = submission.created
    ageSeconds = createdTime - time.mktime(dt.datetime.now().timetuple())
    print('dateTime: ' + str(get_date(submission) + ' diff (hrs): ' + str(ageSeconds / 3600) + ' title: ' + str(submission.title))
    submission 
