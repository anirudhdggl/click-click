#!/usr/bin/python3

import requests
from termcolor import colored

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

urlFile = "urls.txt"
urlList = []

with open(urlFile) as f:
	urlList = f.readlines()

urlList = [x.strip() for x in urlList]