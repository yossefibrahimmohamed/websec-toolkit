from urllib.request import urlopen
import os

url = "https://www.tencent.com/en-us/partnership.html"
html = urlopen(url).read()

with open("file.html", "wb") as f:
    f.write(html)

os.system(r"grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.html")
