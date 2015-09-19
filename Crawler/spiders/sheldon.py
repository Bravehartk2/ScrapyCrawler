# -*- coding: utf-8 -*-
import scrapy
from items import SheldonCrawlerItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SheldonSpider(CrawlSpider):
    name = "sheldon"
    allowed_domains = ["ask-sheldon.com", "www.ask-sheldon.com"]
    start_urls = (
        'https://www.ask-sheldon.com/',
    )
    rules = (
        Rule(
            LinkExtractor(
                allow=(),
                deny=(),
                restrict_css=('.menu-item a', '.cat-item a', '.entry-title a', '.nav-previous a'),
                canonicalize=True,
                unique=True
            ),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        self.logger.info('Parsed URL: %s with STATUS %s', response.url, response.status)
        status = response.status
        if (status != 200):
            self.logger.error('Found satutus unlike 200: %s STATUS: %s', response.url, response.status)
        item = SheldonCrawlerItem()
        item['title'] = response.xpath('//title/text()')
        return item
