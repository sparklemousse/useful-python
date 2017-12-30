# Using MechanicalSoup to get the results from DuckDuckGo & Google
# Python 3
# Dec 2017

import mechanicalsoup
import re

# input search term
search_term = "flextiles"

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

# Connect to Google
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com/")

# Fill-in the form
browser.select_form('form[action="/search"]')
browser["q"] = search_term
browser.submit_selected(btnName="btnG")

# Display links
for link in browser.links():
    target = link.attrs['href']
    # Filter-out unrelated links and extract actual URL from Google's
    # click-tracking.
    if (target.startswith('/url?') and not
            target.startswith("/url?q=http://webcache.googleusercontent.com")):
        target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
        print(target)
