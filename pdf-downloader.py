# asset download script

# Python 3+
# asks for file URL and required number of downloads
# requests the file and writes it locally
# random delay between each download

import urllib.request
import urllib.error
import time
from random import randint

first = 1
download = str(input('URL of file: ')) # example: https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/482097/gbs-air-conditioners-2015.pdf
cycles = int(input('Number of downloads: '))

while first <= cycles:
    response = urllib.request.urlopen(download)
    file = open(str(first) + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    response.close()
    print("Downloaded ", first)
    first = first + 1
    time.sleep(randint(1,5))
print("Completed all downloads")
