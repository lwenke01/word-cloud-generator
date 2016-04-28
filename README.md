# word-cloud-generator

###Install
*using Python 2.7 (does not work with 3.5)

```python
pip install wordcloud
```
```python
pip install matplotlib
```
```python
pip install numpy
```

###Add Data and Image in Script
####Image:
On line #10, change the path to an image:
```
pipe_mask = np.array(Image.open(path.join("./images/", "elephant.jpg")))
```

####Text File:
On line #14, add a path to the text file:
```
text = open(path.join('//Users/lisaw/desktop/tapper.txt')).read()
```

###Run Script
```python
python word.py
```

###Output Example
Used the transcript from the March 12, 2016 GOP debate and an image of an elephant.

Here is what the script changes the image output to:

>Original image:

>![original image](/images/elephant.jpg "pre-script")

>Output Image:

>![image output](/images/figure_1.png "post-script")


##Using with TwitterBot

###Set up API access
Go to Twitter and get access keys: http://apps.twitter.com/

Create a ```oauth_info.py``` file to store the keys:

```
CONSUMER_KEY = 'enter your information here'
CONSUMER_SECRET = 'enter your information here'
ACCESS_TOKEN = 'enter your information here'
ACCESS_TOKEN_SECRET = 'enter your information here'
USER_NAME = 'enter your twitter handle here'
```

**REMEMBER to .gitignore this file if pushing to Git**

###install packages:

The packages can be downloaded and installed, e.g., via pip:

* twitter
* pandas
* pyprind

```
pip install <package_name>
```
or

```
python -m pip install <package_name>
```
###Getting User Tweets
In the ```twitter_timeline.py``` script, on line #29 change the self.screen_name:

```self.screen_name = 'realdonaldtrump'```

Next, run the script with an output file to save the tweets to a csv file on the CLI:

```python twitter_timeline.py --out 'output.csv'```

Tweets should download and come back with this when it is completed:

```
Authentification successful: True
Tweets downloaded: 195()
```

###Running the WordCloud Script
Open the  ```word_twit.py``` file and make sure the script is reading the correct output file on line #15:

```text = open(path.join('./_twitter/output.csv')).read()```

Now run the file and watch the magic happen!
```python word_twit.py```



###Sources
WordCloud Github: https://github.com/amueller/word_cloud
https://github.com/staseface7

TwitterBot: http://sebastianraschka.com/Articles/2014_twitter_wordcloud.html
https://github.com/rasbt/datacollect/tree/master/twitter_timeline
