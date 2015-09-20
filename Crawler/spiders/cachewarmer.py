# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor

import Crawler.settings_sheldon

from Crawler.items import PageCrawlerItem


class SheldonSpider(CrawlSpider):
    name = Crawler.settings_sheldon.CRAWLER_NAME
    allowed_domains = Crawler.settings_sheldon.CRAWLER_DOMAINS
    start_urls = Crawler.settings_sheldon.CRAWLER_START_URLS
    rules = (
        Rule(
            LinkExtractor(
                allow=(),
                deny=(),
                restrict_css=Crawler.settings_sheldon.CSS_SELECTORS,
                canonicalize=True,
                unique=True
            ),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        # self.logger.info('Parsed URL: %s with STATUS %s', response.url, response.status)
        item = PageCrawlerItem()
        item['status'] = response.status
        item['title'] = response.xpath('//title/text()')[0].extract()
        item['url'] = response.url
        item['headers'] = response.headers
        return item
