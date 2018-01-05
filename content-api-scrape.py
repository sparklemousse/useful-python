"""
Created in December 2017
@author: paulcronk
Works on Python 3.5

Sends a set of GOV.UK slugs to the content API and
returns some dates
"""

import requests
import csv
#import json
import pandas as pd

list = []

# get a list of URLs from a CSV file.
with open('content-urls.csv', 'rU') as f:
    urlfile = csv.reader(f)

# loop through each constructed URL on the API. This is a simple filter for specific pages
    for i in urlfile:

        url = "https://www.gov.uk/api/content/%s" % i[0]
        print (url)
    # read JSON result into r
        r = requests.get(url).json()

    # chose the fields you want to scrape. This scrapes the first 5 instances of organisation, error checking as it goes
    # this exception syntax might not work in Python 3

        # gather organisation fields
        try:
            public_update = r['public_updated_at']
        except (IndexError, KeyError) as e:
            public_update = 'null'

#        try:
#            organisation2 = r['results'][0]['organisations'][2]['title']
#        except (IndexError, KeyError) as e:
#            organisation2 = 'null'

    # Appends the scraped fields to a list
        list.append([i[0],public_update])

# Converts the list to dataframe, prints it and writes it to a CSV file
results = pd.DataFrame(list,columns=['slug','Last major update'])
print (results)
results.to_csv(path_or_buf='content-results.csv', sep=',')
