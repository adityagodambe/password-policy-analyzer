#!/usr/bin/env python
'''This script crawls Alexa's top 50 US sites list and stores it in a csv file'''

import requests
from bs4 import BeautifulSoup
import re

__author__ = "Aditya Godambe"
__email__ = "agodambe@cs.stonybrook.edu"


url = "https://www.alexa.com/topsites/countries/US"

r = requests.get(url)
c = r.content

soup = BeautifulSoup(c, "html.parser")

all=soup.find_all("div",{"class":"td number"})

listingsTable=soup.find_all("div",{"class":"listings table"})

tr_site_listing=soup.find_all("div",{"class":"tr site-listing"})


with open("sites.csv", 'a') as file:
    for link in tr_site_listing:
        site = link.find("a").text
        file.write(site + "\n")

