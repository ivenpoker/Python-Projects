#!/usr/bin/env  python3

#######################################################################
#                                                                     #
#       Program purpose: Get the top stories from Google news.        #                                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>        #
#       Creation Date  : September 5, 2019                            #
#                                                                     #
#######################################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

if __name__ == "__main__":
    news_url = "https://news.google.com/news/ress"
    client = urlopen(news_url)
    xml_page = client.read()
    client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")

    # Print news title, url and publish date

    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-" * 60)
