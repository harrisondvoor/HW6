import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = input("Enter URL: ")
my_url = urllib.request.urlopen(html, context=ctx).read()
my_count = int(input("Enter count: "))
my_position = int(input("Enter position: ")) - 1
counter = 1

print("Retrieving: " + str(html))
while (counter < my_count):
    x = BeautifulSoup(my_url, "html.parser")
    my_html = x.find_all('a')[my_position].get('href')
    print("Retrieving: " + str(my_html))
    my_url = urllib.request.urlopen(my_html, context=ctx).read()
    counter += 1

x1 = BeautifulSoup(my_url, "html.parser")
print("Retreiving: " + x1.find_all('a')[my_position].get('href'))
print(x1.find_all('a')[my_position].string)
