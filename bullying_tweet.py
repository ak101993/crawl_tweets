import numpy as np
import pandas as pd
from twython import Twython
import csv
import time
data = pd.read_csv("data.csv")
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""
twitter = Twython(
                  CONSUMER_KEY, CONSUMER_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
tweet = twitter.show_status(id=99906065692495873)
print(tweet['text'])
for i in range(1007,data.shape[0]):
    try:
        tweet = twitter.show_status(id=(data.loc[i][0]))
        print(tweet['text'])
        csvFile =open('bullytweet.csv', 'a')
        csvWriter= csv.writer(csvFile)
        csvWriter.writerow([tweet['text'],str(data.loc[i][0]),str(data.loc[i][1]),str(data.loc[i][2]),
                            str(data.loc[i][3]),str(data.loc[i][4]),str(data.loc[i][5]),str(data.loc[i][6]),str(data.loc[i][7])])
        time.sleep(5)
    except:
        continue


print('Done')
