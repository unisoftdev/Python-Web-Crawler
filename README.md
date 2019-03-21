### Web-Crawler-Software-in-Python
A free version of a web crawler written in Python 3 with Beautiful Soup which collects links, and email addresses. For non-technical people, the offer is a premium version with GUI, many more functionalities like filters, and whatsoever you will want.

### Change the configuration file:
 assets --> config.json
 1. Add website urls which you want to crawl, where you want to collect links or addresses from.

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
