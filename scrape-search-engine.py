# Using MechanicalSoup to get the results from DuckDuckGo & Google
# Python 3
# Dec 2017

import mechanicalsoup
import re
import csv
import pandas as pd

# Connect to Google
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com/")
search_results = []
result = []
all_search_results = []
target = []

# open file of search terms
with open("search-terms.csv", newline=None ) as f:

    urlfile = csv.reader(f)
    # for each search term
    for row in urlfile:
        search_term = row[0]
        # Fill-in the form
        browser.select_form('form[action="/search"]')
        browser["q"] = search_term
        browser.submit_selected(btnName="btnG")
        print(row)
        search_results = []
        # add each search term to the list
        search_results = row

        # get the links on the search research page
        for link in browser.links():
            target = link.attrs['href']

            # Filter-out unrelated links and extract actual URL from Google's click-tracking
            if (target.startswith('/url?') and not
                    target.startswith("/url?q=http://webcache.googleusercontent.com")):
                target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
                # add each results link to the list
                search_results.extend([target])

        # add each search term to list as next row
        all_search_results.extend([search_results])

# turn into dataframne and export to csv
search_results_df = pd.DataFrame(all_search_results)
search_results_df.rename(columns={0: 'Search term'}, inplace=True)
search_results_df.to_csv(path_or_buf='search-results.csv', sep=',',encoding='utf-8')



"""
### for Duck Duck Go

# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://duckduckgo.com/")

# Fill-in the search form
browser.select_form('#search_form_homepage')
browser["q"] = search_term
browser.submit_selected()

# Display the results
for link in browser.get_current_page().select('a.result__a'):
    print(link.text, '->', link.attrs['href'])
"""
