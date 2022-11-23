from urllib import request
from bs4 import BeautifulSoup

site = request.urlopen('http://py4e-data.dr-chuck.net/comments_1683145.html').read()
soup = BeautifulSoup(site, features="lxml")
tags = soup('span')
sum=0
for tag in tags:
    sum = sum + int(tag.contents[0])

print('The sum is', sum)
