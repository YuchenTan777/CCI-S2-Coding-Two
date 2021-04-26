# CCI-S2-Coding-Two

Hello everyone, I'm very happy to present my coding-2 lab work to you. I will present 4 projects here.

## Week 2 Exercise - Your first OF project
First is the second week's exercise, Select a JavaScript project I completed last term and port it to C++ using openFrameworks.

The name of this project is Circle Loop.

For this exercise I mainly modified last semester's 3D graphics assignment and added modifiers to modify the number of graphics and their orientation in the x, y, and z-axis in real time. It is worth mentioning that because I put in the z-axis, I can convert flat 2D graphics to 3D when using the mouse.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%202%20Exercise%20-%20Your%20first%20OF%20project/Images/Final%20work/mix.png)  

**This week's project made me more familiar with c++ and open framework.**


## Week 3 Exercise - The Python Challenge!
This challenge has a total of 33 levels, each level has a picture & file & hint & nothing, need logic, imagination and write some scripts in python to get it done, and finally get a new url address, is the address of the next level.

It is very helpful to improve my programming skills.

It requires good observation skills and logical thinking, and of course, imagination.

I found it interesting after I got the answer.

### Current knowledge covered：

* 1. Module: string

partitioning, indexing, common operation functions, mapping

* 2. module:urllib

Access & parse

* 3. module pickle

Read, parse

* 4. Module Image(PIL library)

Image processing

## Week 4 Exercise - Python webscraper

Next was the fourth week of exercises to build a Python webscraper. I built two webscraper
here.

For the first project, I’ll scrape data from IMDb’s “Top 1,000” movies, specifically the top 50 movies on this page. 
Here is the information I’ll gather from each movie listing:
* The title
* The year it was released
* How long the movie is
* IMDb’s rating of the movie
* The Metascore of the movie
* How many votes the movie got
* The U.S. gross earnings of the movie

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%204%20Exercise%20-%20Python%20webscraper/table.png)

### Summarization of News Articles Using Gensim

In today’s digital world, we’re bombarded with endless information. We’ve got infinitely scrolling social media feeds and a 24-hour news cycle. So there’s plenty of news to stay aware of and we’ve got to be able to digest it quickly!

So I use `bs` and `gensim` to help me quickly summarize news and extract news keywords

``` 
# Imports
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from gensim.summarization import keywords
```
```
summary = summarize(article_text, ratio=0.3)
```

> Where the Ratio represents the fraction of sentences in the original text should be returned as an output. For example, a ratio of 0.5 represents that we want to retain 50% of the original version. The default ratio is 20% or 0.2.

### Summarises and extract keywords from news using gensim 💫

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%204%20Exercise%20-%20Python%20webscraper/Gensim/gensim.png)

## Week 6 Exercise - Signal Processing in Numpy and Tensorflow

The last project is Signal Processing in Numpy and Tensorflow
Image augmentation is a strategy that can greatly increase the diversity of images available for training models without actually collecting new images. 

For training any machine learning model, especially a deep learning model, having a large dataset is very important and can greatly improve the performance of the model. When we train a deep learning model on images, we need at least tens of thousands of images to generalize the patterns of the images.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/gray.png)
![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/fliplr.png)
![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/rotate.png)
![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/wrap.png)


Generating image data is expensive and tedious work. Machines are blind without data. 

In such a case, we can generate more images from existing images by applying different transformations techniques on it. There are different techniques like rotation, flipping, shifting, etc. which can help us to diversify the image data. We can generate more than 10X or 100X images if we have at least 4–5 transformations techniques. We can also use methods to blur the image and add random noise to image, to generate more images.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/oildream.jpg)





