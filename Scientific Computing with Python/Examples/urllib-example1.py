import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/page2.htm')
for line in fhand:
    print(line.decode().strip())