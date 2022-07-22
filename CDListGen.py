from bs4 import BeautifulSoup
import requests

URL = input('URL: ')
getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})

soup = BeautifulSoup(getURL.text, 'html.parser')

linklist = []

for link in soup.find_all('a'):
    linklist.append(link.get('href')) # Adds all hyperlinks to a list

del linklist[:5] # Removes first 6 unwanted items in list

linklistnum = len(linklist) # Generates number of how many items are in list

del linklist[(linklistnum - 5):] # Removes last 6 unwanted items in list

new_list = [x[26:] for x in linklist]

newlistnum = len(new_list) # Generates number for items in list
newlistdelnumber = 0 # Sets newlistdelnumber to 0

listremovedlinks = [] # Creates a new list

new_list.pop(0) # Removes first item from list

for x in range(newlistnum):
    while (newlistnum) > (newlistdelnumber):
        newlistdelnumber = newlistdelnumber + 2
        
        try:
            listremovedlinks.append(new_list[newlistdelnumber])
        except:
            pass

mp4links = []
listwithoutmp4 = []

for x in listremovedlinks: # Seperates .mp4 from link list
    if '.mp4' in x:
        mp4links.append('https://fs-05.cyberdrop.to' + (x))
    else:
        listwithoutmp4.append('https://cyberdrop.me' + (x))

with open(r'links.txt', 'w', encoding="utf-8") as fp:
    for item in listwithoutmp4:
        fp.write("%s\n" % item)
    for item in mp4links:
        fp.write("%s\n" % item)
    print('Done')