# Week 4 Exercise - Python webscraper

> * Build a simple webscraper that scrapes a set of documents from the internet and summarises them using gensim.
> * If you manage to achieve this, extract keywords from all the different documents and see if any are more popular than others.
> * Search for documents that contain those keywords using Python and then summarise those documents too.

### Build a simple webscraper

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
