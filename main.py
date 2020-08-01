#!/usr/bin/python3

import requests
from termcolor import colored

# Some websites show forbidden message if
# user-agent is not present

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# The file containig the list of URL

urlFile = "urls.txt"
urlList = []

# Read all the URLs into a list of URLs

with open(urlFile) as f:
	urlList = f.readlines()

# Strip off the trailing \n at the end of lines
# If \n is present, the result will not be correct

urlList = [x.strip() for x in urlList]

# Read headers of all the URLs and check them for
# X-Frame-Options header. If it's value is set to
# either SAMEORIGIN or DENY, then it's fine. In any
# other case, it's vulnerable to clickjacking

for url in urlList:
	req = requests.head(url)
	head = req.headers
	if 'x-frame-options' in head:
		if head['x-frame-options'] == "SAMEORIGIN" or head['x-frame-options'] == "DENY":
			safeUrl = colored("[Safe]: " + url,'green')
			print(safeUrl)
		else:
			msg = colored("[" + url + "]: X-frame-options is present but it's value is too permissive","yellow")
			print(msg)
	else:
		vuln = colored("[Vulnerable]: " + url, 'red')
		print(vuln)