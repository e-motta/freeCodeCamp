import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs

url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = bs(html, 'html.parser')

a_tags = soup('a')
for tag in a_tags:
    print(tag.get('href', None))