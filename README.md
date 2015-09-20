# ScrapyCrawler
Just an experiment at the moment!!!
The ScrapyCrawler is a simple page crawler bases on the open source Python library Scrapy. Its build to initialize the Fullpage Cache 
of my webblog https://www.ask-sheldon.com.

# Features 
- Crawls all links of a given domain recursively so that all pages will be loaded ones 
- The links that should be called can be specified via simple  CSS selectors
- Everything can be configured in one single configuration file 
- Writes logs to a logfile per day (logs folder)
- Writes crawled urls together with pages titles, status and headers to a csv file per day (export folder)

# Installation
To get the page crawler running you have to set a symlink to a project specific settings file.

```
$> ln -S myown_settings_file.py settings.py
``` 
As an example you find the settings_sheldon.py which crawls all pages of  my blog to initialize the Wordpress fullpage cache use for 
https://www.ask-sheldon.com.

# More information
For more information about the used Python library Scrapy you should have a look at the following resources:

- https://www.ask-sheldon.com/python-website-crawler/
- [Scrapy project page] (http://scrapy.org/)
- [Scrapy documentation] (http://doc.scrapy.org/en/latest/)
- [Scrapy github wiki] (https://github.com/scrapy/scrapy/wiki)