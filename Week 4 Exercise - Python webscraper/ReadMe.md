# Week 4 Exercise - Python webscraper

> * Build a simple webscraper that scrapes a set of documents from the internet and summarises them using gensim.
> * If you manage to achieve this, extract keywords from all the different documents and see if any are more popular than others.
> * Search for documents that contain those keywords using Python and then summarise those documents too.

## Build a simple webscraper

For this project, I’ll scrape data from IMDb’s “Top 1,000” movies, specifically the top 50 movies on this page. Here is the information we’ll gather from each movie listing:


* The title
* The year it was released
* How long the movie is
* IMDb’s rating of the movie
* The Metascore of the movie
* How many votes the movie got
* The U.S. gross earnings of the movie

**important things :**

Every website has a different structure. These are a few important things to think about when building a web scraper:

* What’s the structure of the web page that contains the data you’re looking for?
* How do we get to those web pages?
* Will you need to gather more data from the next page?

> HTML describes the structure of a web page semantically, and originally included cues for the appearance of the document.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%204%20Exercise%20-%20Python%20webscraper/container.png)

### Building a DataFrame With pandas 💫

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%204%20Exercise%20-%20Python%20webscraper/table.png)


## Summarization of News Articles Using Gensim

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
