import json
import urllib.request as UR
url = input('Enter location: ')
count = 0
print('Retrieving', url)
xml = UR.urlopen(url).read()
print('Number of characters retrieved = ', len(xml))
info = json.loads(xml)
for item in info["comments"]:
	number = int(item["count"])
	count = count + number

print('Sum = ', count)
