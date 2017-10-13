from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

sum_tot = 0
tags = soup('span')
for tag in tags:
    print('URL:', tag.get('href', None))
    print ('Contents: ', tag.contents[0])
    sum_tot += int(tag.contents[0])
    print (sum_tot)

