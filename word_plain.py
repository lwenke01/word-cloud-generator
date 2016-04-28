
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join('//Users/lisabisa25/desktop/word_cloud/prince.txt')).read()
wordcloud = WordCloud().generate(text)

# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
