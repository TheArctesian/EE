# pip install newsapi-python

from newsapi import NewsApiClient
import pandas as pd 
import datetime as dt
import logging

def setupDB():
    db = pd.DataFrame(
        columns=[
            "date",
            "headline",
            "source",
        ]
    )

def scrape ():
    key = NewsApiClient(api_key='3a9ab83923f249858a70f8ac907881fd')
    # headlines = key.get_top_headlines(  q='bitcoin',
    #                                    language='en',
    #                                    from_param=dt.date(2020, 5, 22),
    #                                    to=dt.date(2022, 6, 20),)
    raw = key.get_everything(
        q="bitcoin ",
        language="en",
        from_param=dt.date(2020, 5, 22),
        to=dt.date(2022, 6, 20),
    ) 

    # export to csv
    db = pd.DataFrame(
        columns=[
            "date",
            "headline",
            "source",
        ]
    )
    print(headline)
    for i in range(len(headline['articles'])):
        db.loc[i] = [
            headline['articles'][i]['publishedAt'],
            headline['articles'][i]['title'],
            headline['articles'][i]['source']['name'],
        ]
    db.to_csv('news.csv', index=False)

if __name__ == "__main__":
    setupDB() # create csv file
    scrape() # scrape news
    logging.info("Ran")