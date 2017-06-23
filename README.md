# ScrapyCrawler
The ScrapyCrawler is a simple page crawler bases on the open source Python library Scrapy. Its build to initialize the Fullpage Cache 
of my webblog https://www.ask-sheldon.com.

# Features 
- The spider crawls all links of a given domain recursively.  So all domain pages will be loaded ones and the page cache for these pages is warmed.
- All links that should be called can be specified via simple CSS selectors. Only matching links will be processed.
- Everything can be configured in a single configuration file.
- All application logs are written into a log-file in a separate folder (one per day, logs folder)
- The crawled URLs, page-titles, headers and statuses are exported to a CSV file (per day, export folder)

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
4. Clone the repository (or just download it via [github](https://github.com/Bravehartk2/ScrapyCrawler/archive/master.zip))
   ```
   $> git clone https://github.com/Bravehartk2/ScrapyCrawler.git
   ```
 
# Settings
To get the page crawler running you have to set a symlink to a project specific settings file (in the **Crawler** folder).

```
$> cd Crawler
$> ln -S my_own_settings_file.py settings.py
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
- Scrapy project page: http://scrapy.org/
- Scrapy documentation: http://doc.scrapy.org/en/latest/
- Scrapy github wiki: https://github.com/scrapy/scrapy/wiki
