import time
import os

while True:
    os.system("scrapy crawl uestcjwc -o JwcInfo.json")
    time.sleep(86400)    # 24*60*60=86400s
