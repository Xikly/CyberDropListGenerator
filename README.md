# CyberDrop List Generator

A Cyberdrop.me list generator,
Cyberdrop has recently has some fucky wuckies when it comes to downloading media from them,
this tiny python script generates a .txt file containing cyberdrop links that removes the old fs-0 direct link style in favour for cyberdrop.me, one that works.

Requirements:
1. Python(Latest) - https://www.python.org/downloads/
2. beautifulsoup4 - https://pypi.org/project/beautifulsoup4/
3. requests - https://pypi.org/project/requests/

How to use:
1. Obtain a cyberdrop.me link that you wish to download the files from.
2. Launch the script from terminal using py ./CDListGen.py while working in the directory.
3. Paste the link into the terminal when 'URL:' pops up and press enter.
4. View the links.txt file created in the scripts directory, you will have your links.
5. Use a tool like JDownloader 2 (https://jdownloader.org/) to add the list of links to linkGrabber.
6. Click Start all Downloads in JDownloader 2 and your download will begin.

Enjoy.
