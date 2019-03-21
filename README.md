### Web-Crawler-Software-in-Python
A free version of a web crawler written in Python 3 with Beautiful Soup which collects links, and email addresses. For non-technical people, the offer is a premium version with GUI, many more functionalities like filters, and whatsoever you will want.

### Change the configuration file:
 assets --> config.json --> websites
 1. Add website urls which you want to crawl, where you want to collect links or addresses from.
 Change the urls in this file: https://github.com/unisoftdev/Web-Crawler-Software-in-Python/blob/master/assets/config.json
 2. Blacklist: delete Reddit and any site which you wanna crawl. The bot will not go on the domains if the keywords from the blacklist will match the domain names. For example, there's banned GitHub, Reddit, YouTube, etc. 

### Dependencies: 
1. Python 3, the crawler has been tested on Python 3.7 but it will work alson on lower versions like 3.5, 3.6, and 3.x in general.
2. (pip if it's in a virtual environment or outside:) pip3 install requests json csv bs4
3. Clone the web crawler: git clone https://github.com/unisoftdev/Web-Crawler-Software-in-Python.git

### Formats
CSV files, it creates two files, one file with links and another one with email addresses.

### Speed
I didn't perform any proper benchmarks, but on one of my laptops with a very poor internet speed of ~7Mb/sec (should be 20 but it's not), I have scrapped more than 1300 links in 5 minutes. With the same speed, it might be 748.800 in two days and above 1 million in three days.

### For a premium version with GUI and many more functionalities (also on demand):
https://www.unisoftdev.tech

###### Disclaimer:
## 1. The software is provided as it is without any waranty or responsibility from the side of the author. If it will cause any damages or in some countries illegal scraping then it's only your problem.
## 2. The software was released under GNU/GPL licence so you can feel very free to do almost whatever you want but the author released it only for educational purposes, nothing else. This doesn't mean that you are not free to crawl, scrap, and extract data (if the law of your country does allow it) from websites, it only means that the author doesn't say you that you should/ought do it, the author of the software doesn't say anything.
