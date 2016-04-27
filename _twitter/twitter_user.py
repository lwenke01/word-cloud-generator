
from twython import Twython # pip install twython
import time # standard lib


CONSUMER_KEY = 'ot5GrizGS8O3sw5fWScC4IIvW'
CONSUMER_SECRET = '68dcGVQjOaOHfQg2Dp2rdBRq2wigPi8xMhSjkEIMSwaAwiPoWB'
ACCESS_KEY = '714496252805664768-UhfHINGIEeFkm1oW6gujPnwD9OlVtTp'
ACCESS_SECRET = 'PwenPaEmPSfbXPrF056jexb9x5gKJUcra1pkp939dkcpA'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [467020906049835008] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name='realDonaldTrump',
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute rest between api calls
    

    for tweet in user_timeline:
        print tweet['text'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
