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
>pipe_mask = np.array(Image.open(path.join("/images/lisaw/desktop//", "elephant.jpg")))

####Text File:
On line #14, add a path to the text file:
>text = open(path.join('//Users/lisaw/desktop/tapper.txt')).read()

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

###Credit
Stacie Mahuna (smahuna)
