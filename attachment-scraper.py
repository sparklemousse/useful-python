"""
Created on Tues 28 February 2017
@author: paulcronk
Tested on Python 3.5.

Uses Beautiful Soup

1. This script takes a set of URLs from a csv file
2. It then passes these URLs through Beautiful Soup to count the number of words and scrapes some headings
3. The results are written into a csv file
"""

#import urllib2
import urllib.request
from bs4 import BeautifulSoup as bsoup
from collections import Counter
from nltk import word_tokenize
import re
#from textstat.textstat import textstat
from google2pandas import *


import requests
import csv
import pandas as pd

results_list = []

# set variables
abstract = ""
words = 0
characters = 0


# get a list of URLs from a CSV file.

with open("/Users/paulcronk/python/text/attachment-list.csv", "rU") as f:
    urlfile = csv.reader(f)
    count = 1

    for row in urlfile:
        i = row[0]
        print(i)
# loop through each URL
        # pass URL errors
        try:

            # open the URL
            page = urllib.request.urlopen(i).read()

            asset_list = ["-","-","-","-","-","-","-","-""-","-"]

            # pass through Beautiful Soup looking for title and selected class
            title = " ".join([i.text.strip() for i in bsoup(page, "html.parser").find_all('title')])

            # open the URL
            page = urllib.request.urlopen(i).read()
            for x in range(0,9):
                try:
                    asset_list[x] = bsoup(page, "html.parser").select('div.attachment-details > p.metadata > span.type > abbr[title]')[x]
                    # clean_asset_list = re.sub('<abbr title=\"[a-zA-Z\s]*\">|<\/abbr>','',asset_list)
                except:
                    asset_list[x] = 'null'

            #print(asset_list)
            #print(i)

            # Appends the variables to a list
            results_list.append([i,title,asset_list])

            #results_list.append([i,title,asset_list[0],asset_list[1],asset_list[2],asset_list[3],asset_list[4],asset_list[5],asset_list[6],asset_list[7],asset_list[8],asset_list[9]])
            #print(results_list)

        except:
            pass

        print(count)

        count += 1

#results = pd.DataFrame(results_list,columns=['URL','Title','Asset 1','Asset 2','Asset 3','Asset 4','Asset 5','Asset 6','Asset 7','Asset 8','Asset 9', 'Asset 10'])
results = pd.DataFrame(results_list,columns=['URL','Title','Assets'])
print(results)
results.to_csv(path_or_buf='/Users/paulcronk/python/text/attachment-list-results.csv', sep=',',encoding='utf-8')
