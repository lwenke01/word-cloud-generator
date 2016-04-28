
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread
import numpy as np
from PIL import Image


#read in image and its colors - this is optional in case you want to make the word cloud conform to a specific shape
pipe_mask = np.array(Image.open(path.join("./_twitter/", "twitter_mask.png")))
image_colors = ImageColorGenerator(pipe_mask)

# Read in the whole text
text = open(path.join('./_twitter/output.csv')).read()

#assign your stopwords as an object, this time pointing it to a text file
stopwordsfile = open(path.join('./_twitter/stopwords.txt')).read()
#generate word cloud and set specifications - font type, stop words, background, height/width, and set the shape of the word cloud to conform to your picture
wordcloud_final = WordCloud(
    stopwords = stopwordsfile,
    background_color='white',
    width=1800,
    height=1400,
    mask=pipe_mask
).generate(text)


# Open a plot of the generated image, using picture and image colors pulled from picture to shape the word cloud
plt.imshow(wordcloud_final.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(pipe_mask
    , cmap=plt.cm.gray)
plt.axis("off")
plt.show()
