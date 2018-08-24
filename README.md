# UESTC JWC WebCrawler

## Introduction

We use Python Scrapy to crawl News in website <http://www.jwc.uestc.edu.cn>

Project JwcInfoCrawler crawls **title**, **url** and **date** of the latest News, and email a notification to you.

Project JwcContCrawler crawls **content** of News.

## Requirements

- Python3
- Scrapy
- zmail

## Usage

In folder JwcInfoCrawler:
```
$ scrapy crawl uestcjwc -o JwcInfo.json
```
In folder JwcContCrawler:
```
$ scrapy crawl uestcjwc -o JwcCont.json
```
The results will be stored in *JwcInfo.json* and *JwcCont.json*.

## Author

Cong Yu / [@congyucn](https://congyucn.github.io/)