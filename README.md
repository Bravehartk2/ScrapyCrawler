# ScrapyCrawler
The ScrapyCrawler is a simple page crawler bases on the open source Python library Scrapy. Its build to initialize the Fullpage Cache 
of my webblog https://www.ask-sheldon.com.

# Features 
- Crawls all links of a given domain recursively so that all pages will be loaded ones 
- The links that should be called can be specified via simple  CSS selectors
- Everything can be configured in one single configuration file 
- Writes logs to a logfile per day (logs folder)
- Writes crawled urls together with pages titles, status and headers to a csv file per day (export folder)

# Installation
1. Install python package management system:
```
$> sudo apt-get install python-pip
```
2. Install required networking engine twisted:
``` 
$> sudo apt-get install python-twisted
```
3. Install scrapy via package manager:
```
$> pip install scrapy
```
 
# Settings
To get the page crawler running you have to set a symlink to a project specific settings file (in the **Crawler** folder).

```
$> ln -S myown_settings_file.py settings.py
``` 
As an example you find the settings_sheldon.py which crawls all pages of  my blog to initialize the Wordpress fullpage cache use for 
https://www.ask-sheldon.com.

# Run it
Now you can run the crawler from inside the project folder by using the following command:
```
$> scrapy crawl CRAWLER_NAME_FROM_SETTINGS_PY
```
If you use the example file the command looks like this:
```
$> scrapy crawl sheldon
```

# More information about Scrapy
For more information about the used Python library Scrapy you should have a look at the following resources:

- https://www.ask-sheldon.com/python-website-crawler/
- [Scrapy project page] (http://scrapy.org/)
- [Scrapy documentation] (http://doc.scrapy.org/en/latest/)
- [Scrapy github wiki] (https://github.com/scrapy/scrapy/wiki)