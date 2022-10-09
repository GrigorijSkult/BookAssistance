from bs4 import BeautifulSoup
import requests
from pprint import pprint


def getMeaning(text):
    # create url
    url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + text
    # define headers
    headers = {'User-Agent': 'Generic user agent'}
    # get page
    page = requests.get(url, headers=headers)
    # let's soup the page
    soup = BeautifulSoup(page.text, 'html.parser')
    pprint(soup)

    word = 'Mathematics'
    word = word.strip()
    getMeaning(word.lower())