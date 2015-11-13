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


# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import json


class PageCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    status = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    headers = scrapy.Field()

    # print scrapy.Item.fields.headers
    # cachehit = json.load(scrapy.Item.fields.headers)['X-Cache']
    #
    # print headers
    pass
