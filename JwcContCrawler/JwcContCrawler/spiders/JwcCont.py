import scrapy
from JwcContCrawler.items import JwccontcrawlerItem

URL_BASE = "http://www.jwc.uestc.edu.cn/"
MAX_PAGE = 3


class JwcContSpider(scrapy.Spider):
    name = 'uestcjwc'
    allowed_domains = ["jwc.uestc.edu.cn"]
    start_urls = []
    for i in range(1, MAX_PAGE):
        url = "http://www.jwc.uestc.edu.cn/web/News!queryHard.action?currentPage={}".format(
            str(i))
        start_urls.append(url)

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        item = JwccontcrawlerItem()

        url_ids = sel.xpath(
            '//div[@class="textAreo clearfix"]/a/@newsid').extract()
        entryUrls = [
            "http://www.jwc.uestc.edu.cn/web/News!view.action?id=" + url for url in url_ids]
        for entryUrl in entryUrls:
            yield scrapy.Request(entryUrl, callback=self.parseContent, meta={'item': item})

    def parseContent(self, response):
        item = response.meta['item']

        item['header'] = [i.strip() for i in response.xpath(
            '//div[@class="detail_header"]/h2/text()').extract()]
        item['content'] = [i.strip() for i in response.xpath(
            '//div[@class="NewText"]/p/text()').extract()]

        return item
