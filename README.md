# click-click

Clickjacking is an issue where your website opens up in an iframe and some other person can put another invisible iframe on top of it to make the visitor feel like he is using your website, when in reality, he is not.

## How to use click-click

To use click click, write down all the urls that you want to scan in a file. Save that file as urls.txt and keep it in the same folder as the main.py script.

Then using your terminal grant execution permission to the script by running:

```chmod 777 main.py```

Then simply run the script by typing

```./main.py```

## How to fix your website?

To make sure that your website is free from this issue, you need to ensure that it does not open in any iframe. To do so, you need to set **X-Frame-Options** header to either *SAMEORIGIN* or *DENY*

SAMEORIGIN is a bit more permissive as compared to DENY. While DENY does not allow the website to be embedded as iframe at all, SAMEORIGIN allows it to be embedded in an iframe on the same website, or domain name.

## How does click-click work?

Click-click scans your website for the *X-Frame-Options* HTTP header. If it's value is set for SAMEORIGIN or DENY, it marks the website as safe, else it marks it vulnerable.