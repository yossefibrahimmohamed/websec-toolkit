from urllib.request import urlopen
import os

url = "http://0.0.0.0:8000/secrets.js"
html = urlopen(url).read()

with open("file.js", "wb") as f:
    f.write(html)

os.system("grep -oE 'https?://[a-zA-Z0-9./?=_-]+' file.js")
