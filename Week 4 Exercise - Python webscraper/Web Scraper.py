import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

# initialize empty lists where you'll store your data
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:
    # Name
    name = container.h3.a.text
    titles.append(name)

    # Year
    year = container.h3.find('span', class_="lister-item-year").text
    years.append(year)

    # Time
    runtime = container.p.find('span', class_='runtime').text if container.p.find(
        'span', class_='runtime') else '-'
    time.append(runtime)

    # IMDB rating
    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    # metascore
    m_score = container.find('span', class_='metascore').text if container.find(
        'span', class_='metascore') else ''
    metascores.append(m_score)

    # nv-containers : First - votes
    nv = container.find_all('span', attrs={'name': 'nv'})
    vote = nv[0].text
    votes.append(vote)

    # nv-containers : Second - gross
    grosses = nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)

    #print(titles)
    #print(years)
    #print(time)
    #print(imdb_ratings)
    #print(metascores)
    #print(votes)
    #print(us_gross)

    movies = pd.DataFrame({
        'movie': titles,
        'year': years,
        'timeMin': time,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
        'us_grossMillions': us_gross,
    })

    print(movies)


