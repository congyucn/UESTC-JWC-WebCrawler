import scrapy
from JwcInfoCrawler.items import JwcinfocrawlerItem
import zmail
import json

URL_BASE = "http://www.jwc.uestc.edu.cn/"


class JwcInfoSpider(scrapy.Spider):
    name = 'uestcjwc'
    allowed_domains = ["jwc.uestc.edu.cn"]
    start_urls = [
        "http://www.jwc.uestc.edu.cn/web/News!queryHard.action?currentPage=1"]

    def parse(self, response):
        def mail(url, title):
            server = zmail.server('yourmail@example.com', 'yourpassword')

            mail = {
                'subject': 'NEW JWC NOTIFICATION:%s' % (title),
                'content_html': url,
            }
            server.send_mail('yourfriend@example.com', mail)

        sel = scrapy.selector.Selector(response)
        item = JwcinfocrawlerItem()

        url_id = sel.xpath(
            '//div[@class="textAreo clearfix"]/a/@newsid')[0].extract().strip()
        item['title'] = sel.xpath(
            '//div[@class="textAreo clearfix"]/a/text()')[0].extract().strip()
        item['url'] = "http://www.jwc.uestc.edu.cn/web/News!view.action?id=" + url_id
        item['date'] = sel.xpath(
            '//div[@class="textAreo clearfix"]/i/text()')[0].extract().strip()

        f = open(
            '/Users/cong/Projects/UESTC-JWC-WebCrawler/JwcInfoCrawler/id.txt', 'r')
        id = f.readline()
        f.close()
        if id != url_id:
            f = open(
                '/Users/cong/Projects/UESTC-JWC-WebCrawler/JwcInfoCrawler/id.txt', 'w')
            f.write(url_id)
            f.close()
            mail(item['url'], item['title'])

        return item
