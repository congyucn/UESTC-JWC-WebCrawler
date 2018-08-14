import scrapy
from JwcInfoCrawler.items import JwcinfocrawlerItem

URL_BASE = "http://www.jwc.uestc.edu.cn/"
MAX_PAGE = 3


class JwcInfoSpider(scrapy.Spider):
    name = 'uestcjwc'
    allowed_domains = ["jwc.uestc.edu.cn"]
    start_urls = []
    for i in range(1, MAX_PAGE):
        url = "http://www.jwc.uestc.edu.cn/web/News!queryHard.action?currentPage={}".format(
            str(i))
        start_urls.append(url)

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        item = JwcinfocrawlerItem()

        url_ids = sel.xpath(
            '//div[@class="textAreo clearfix"]/a/@newsid').extract()
        item['title'] = [i.strip() for i in sel.xpath(
            '//div[@class="textAreo clearfix"]/a/text()').extract()]
        item['url'] = [
            "http://www.jwc.uestc.edu.cn/web/News!view.action?id=" + url for url in url_ids]
        item['date'] = sel.xpath(
            '//div[@class="textAreo clearfix"]/i/text()').extract()

        return item
