### Web-Crawler-Software-in-Python
A free version of a web crawler written in Python 3 with Beautiful Soup which collects links, and email addresses. For non-technical people, the offer is a premium version with GUI, many more functionalities like filters, and whatsoever you will want.

### Change the configuration file:
 assets --> config.json
 1. Add website url which you want to crawl, where you want to collect links or addresses from.

### Dependencies: 
1. (pip if it's in a virtual environment or outside:) pip3 install requests json csv bs4
2. clone the crawler:  
### Formats
CSV files, it creates two files, one file with links and another one with email addresses.

### Speed
I didn't perform any proper benchmarks, but on my laptop, I have scrapped more than 1300 links in 5 minutes. It might be 1 million in two days.

