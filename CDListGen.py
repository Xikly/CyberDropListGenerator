from bs4 import BeautifulSoup
import requests
from os.path  import basename

URL = input('URL: ')
getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})

soup = BeautifulSoup(getURL.text, 'html.parser')

linklist = []

for link in soup.find_all('a'):
    linklist.append(link.get('href'))

del linklist[:7]

linklistnum = len(linklist)

del linklist[(linklistnum - 5):]

new_list = [x[26:] for x in linklist]

newlistnum = len(new_list)
newlistdelnumber = 0

new_list.pop(0)

for x in range(newlistnum):
    newlistdelnumber = newlistdelnumber + 2
    try:
        new_list.pop(newlistdelnumber)
    except:
        pass

newestlist = []
newlistaddnumber = len(new_list)

for x in range(len(new_list)):
    while (newlistaddnumber) > 0:
        newestlist.append('https://cyberdrop.me' + (new_list[newlistaddnumber - 1]))
        newlistaddnumber = (newlistaddnumber - 1)
    
with open(r'links.txt', 'w', encoding="utf-8") as fp:
    for item in newestlist:
        fp.write("%s\n" % item)
    print('Done')