# Do you want a free web crawler (bot) or do you want a premium (with a graphic user interface and more functionalities)?
# For a GUI, better performance, more functions, and easiness to use... Check out: www.unisoftdev.tech

'''
* @ The Free Version Of a Web Crawler
* Created By: Juraj Vysvader
* Author's profile: https://www.linkedin.com/in/jurajvysvader
                    https://www.linkedin.com/company/unisoftdev 
* Creation date: 13.8.2018
* Business website: https://www.unisoftdev.tech
* @license http://www.gnu.org/copyleft/lgpl.html GNU/GPL
* @Copyright (C) 2019 Juraj Vysvader. All rights reserved.
'''


# import Python 3.x libraries (tested on Python 3.6 and 3.7):
import requests, re, json, csv
from bs4 import BeautifulSoup
# You need a Python 3.x virtual environment or:
# Go to your Linux terminal (command prompt) and type:
# sudo apt install pip3
# sudo apt update
# pip3 install requests re json csv bs4



# to create a CVS file if doesn't exist and open if does. 
f = csv.writer(open('emails.csv', 'w'))
# to write found email addresses
f.writerow(['email', 'leading url'])

# to create a CVS file if doesn't exist and open if does.
k = csv.writer(open('links.csv', 'w'))
# to write found email addresses.
k.writerow(['scrapped domain names'])

with open('assets/config.json', 'r') as config_file:
    config_data = json.load(config_file)

# lists
robotstxt = [] # scrapped robots.txt
collected_pages = [] # variables of pages filtrated according to robots.txt.
collected_domains = [] # final result of found domains
robotstxt_allowed = [] # robots.txt rules allowing access for web crawlers.
robotstxt_disallowed = [] # robots.txt rules disallowing access for web crawlers.
garbage = [] # binned variables those is needed to know, a rabbish which shouldn't be used second time

# to check whether the crawler should visit particular web pages (either subpages or a landing page).
# It checks robot text but basically, only disallowed pages and not properly. It'd need an extra work.
def robots_txt():
    try: 
        address_of_robots_text = 'http://' + domain_name + '/robots.txt'
        req_ = requests.head(address_of_robots_text)
        # you can change the response code if you really need something else
        # the code just check availability
        if req_.status_code < 400:
                # Python Requests library: https://pypi.org/project/requests/
                # You could set up: the user agent (your real creditionals), not Unisoftdev.
                # Helpful tips if you'll need authentification to log in or something else: http://docs.python-requests.org/en/master/ 
                scrapped_txt = requests.get(address_of_robots_text, stream=True, timeout=0.5)
                # For performance, the code above is vulnerable. If you wanna fix it then add: "allow_redirects=False".
                # Ten it will be: scrapped_txt = requests.get(address_of_robots_text, stream=True, timeout=0.5, allow_redirects=False).
                rob_txt = []
                all_lines = scrapped_txt.iter_lines() # It's not JSON or Python dictionary/list, it need a remake.
                # loop
                for iline in all_lines:
                    rob_txt.append(iline)
                # loop
                for line in rob_txt:
                    if b'Disallow:' in line: # bytecode or string?
                        line = str(line) #changing the format, unicode isn't really uni   
                        robotstxt_disallowed.append(line.split(': ')[1].split(' ')[0]) 
                    elif b'Allow:' in line:
                        line = str(line) #changing the format, unicode isn't really uni   
                        robotstxt_allowed.append(line.split(': ')[1].split(' ')[0]) 
                        # I filled it out full of variables but didn't use this variables from the list (robotstxt_allowed), it's a junk code left that you can get bored.
        else:
            print('no retried robots.txt, status code > 400') # If the web crawler isn't fed up. 
    except requests.exceptions.RequestException as e:
        print(e) # An error message (variable, it prints any message that is delivered).

# To retrieve data from JSON file from assets folder:
website_addresses = config_data["websites"]
# It's checking that you wrote any URL, if it's not empty.
if len(website_addresses) > 0:
    for nm in website_addresses:
        domain_name = nm.split('//')[-1].split('/')[0] # getting the domain names.
        # Here's the function above
        robots_txt() # this function will take care of response code, checks availability of websites.
        allowed_rob = int(len(robotstxt_allowed)) # To count it just once and save as a variable, it saves some proccessing power.
        disallowed_rob = int(len(robotstxt_disallowed)) # To count it just once and save as a variable, it saves some proccessing power.
        if disallowed_rob < 1: # To check that the bot got any data from the robots.txt.
            collected_pages.append(nm) # To say the web crawler where to go next.
        else:
            # If it's not disallowed by robots.txt then it's to crawl... 
            for eachline in robotstxt_disallowed:
                if not eachline in nm and not nm in collected_pages:
                    collected_pages.append(nm)
        # This numbers are gonna be important:
        for i in range(1, 50): # <=== Change it if you need to crawl in a different range!
            if not '//' in str(i):
                url = nm + str(i) 
                collected_pages.append(url)
            

# a list, another Python list.
# It just checks for a rabbish.
all_email_addresses = []

for sub_page in collected_pages:
  # To check that it's a garbage.  
  if not sub_page in garbage:
    # To collect the garbage which can be usable once again.
    garbage.append(sub_page)
    try:
        print(sub_page)
        # Requests: https://pypi.org/project/requests/
        page = requests.get(sub_page, timeout=0.5, stream=False)
        # Beautiful Soup (a Python library): https://pypi.org/project/beautifulsoup4/
        soup = BeautifulSoup(page.text, 'html.parser') # To parse with HTML parser but you can change it.
        email_soup = soup.select('a[href^="mailto"]') # To find all email addresses in HTML of a crawled website.
        # loop
        for email_address in email_soup:
            email_address = email_address.text
            print(str(email_address)) # If you use a command line then you can watch it at a real time.
            if not email_address in all_email_addresses:
                # To write on a SSD/HDD/SHDD or wherever else can be a solid disk.
                f.writerow([email_address, sub_page]) # a csv file which you find in assets
                all_email_addresses.append(email_address) 
        # Some basic filters those are dependent of the particular HTML makeup of a website:
        if 'b5szba-0 dQcRmW' in soup:
            scrapped_links = soup.find_all('a', attrs={'class':'class="b5szba-0 dQcRmW"'}) # To match link with this class
        elif 'title' in soup:
            scrapped_links = soup.find_all('a', attrs={'class':'title'}) # To match link with this class
        elif 'url' in soup:
            scrapped_links = soup.find_all('a', attrs={'class':'url'}) # To match link with this class
        else:
            scrapped_links = soup.find_all('a') # To match else.
        for a in scrapped_links:      
            if domain_name not in a['href'] and 'http' in a['href']: # No ftp, etc.
                r_domain = a['href'].split('//')[-1].split('/')[0] # Getting the domain names.
                for b_keywords in config_data["blacklist"]: 
                    if not b_keywords in r_domain and not r_domain in collected_domains:
                            print(r_domain) # If you watch at command line then it prints for you.
                            collected_domains.append(r_domain) 
                            k.writerow([r_domain])  # a csv file which you find in assets
    except:
        print('exceptation')    


    # This open source code serves as an example of a python web crawler made from a scratch with BeautifulSoup and Requests libraries. 
    # Enjoy your new python web scraping experience.
