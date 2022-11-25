import urllib.request as UR
import xml.etree.ElementTree as ET

url = input('Enter your location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml' = Test
# 'http://py4e-data.dr-chuck.net/comments_1683147.xml' = Graded

total_number = 0
sum = 0

print('Retrieving the URL: ', url)
xml = UR.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tr = ET.fromstring(xml)
count = tr.findall('.//count')
for item in count:
    sum += int(item.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
