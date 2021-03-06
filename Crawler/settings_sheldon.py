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


import datetime

dateTimeString = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")

# Scrapy settings for Crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Scrapy PageSpider'

SPIDER_MODULES = ['Crawler.spiders']
NEWSPIDER_MODULE = 'Crawler.spiders'


# Crawler settings:
##################################

# Crawler name:
CRAWLER_NAME = "sheldon"
CRAWLER_DOMAINS = ["ask-sheldon.com", "www.ask-sheldon.com"]
CRAWLER_START_URLS = (
    'https://www.ask-sheldon.com/',
)

# Regexes to allow or
# Allow all => domains are restricted by CRAWLER_DOMAINS above
CRAWLER_ALLOW_REGEX = None
CRAWLER_DENY_REGEX = None

# CSS selectors to get links:
CSS_SELECTORS = (
    '.menu-item a',
    '.widget_archive ul li a',
    '.widget_tag_cloud a',
    '.cat-item a',
    '.entry-title a',
    '.entry-footer a',
    '.nav-links a',
    '.entry-content a'
)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'ScrapyCrawler (+https://www.ask-sheldon.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY=3

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED=False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
# 'Crawler.middlewares.MyCustomSpiderMiddleware': 543,
# 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': None,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Crawler.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'Crawler.pipelines.SomePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 3600
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Logging and stats
DEPTH_STATS_VERBOSE = True
LOG_FILE = "logs/www.ask-sheldon.com_%s.log" % dateTimeString

# Feed export
FEED_FORMAT = 'csv'
FEED_EXPORT_FIELDS = ['parse_time', 'status', 'title', 'url', 'headers']
FEED_URI = "export/www.ask-sheldon.com_%s.csv" % dateTimeString
