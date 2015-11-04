# -*- coding: utf-8 -*-

'''
*   This program is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
*   @author Marcel Lange <info@ask-sheldon.com>
*   @package ScrapyCrawler 
 '''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import Crawler.settings
from Crawler.items import PageCrawlerItem


class ScrapyCrawlerSpider(CrawlSpider):
    name = Crawler.settings.CRAWLER_NAME
    allowed_domains = Crawler.settings.CRAWLER_DOMAINS
    start_urls = Crawler.settings.CRAWLER_START_URLS
    rules = (
        Rule(
            LinkExtractor(
                allow_domains=Crawler.settings.CRAWLER_DOMAINS,
                allow=Crawler.settings.CRAWLER_ALLOW_REGEX,
                deny=Crawler.settings.CRAWLER_DENY_REGEX,
                restrict_css=Crawler.settings.CSS_SELECTORS,
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback='parse_item',
            process_links='filter_links'
        ),
    )

    # Filter links with the nofollow attribute
    def filter_links(self, links):
        return_links = list()
        if links:
            for link in links:
                if not link.nofollow:
                    return_links.append(link)
                else:
                    self.logger.debug('Dropped link %s because nofollow attribute was set.' % link.url)
        return return_links

    def parse_item(self, response):
        # self.logger.info('Parsed URL: %s with STATUS %s', response.url, response.status)
        item = PageCrawlerItem()
        item['status'] = response.status
        item['title'] = response.xpath('//title/text()')[0].extract()
        item['url'] = response.url
        item['headers'] = response.headers
        return item
