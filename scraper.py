import sys
from lxml import html
import re
import requests

should_continue = True

while (should_continue):
    chosen_link = None
    try:
        subject = raw_input('Enter wikipedia page: ') #TODO what happens if page does not exist?
        page = requests.get('https://en.wikipedia.org/wiki/' + subject)
        tree = html.fromstring(page.text)
        links = tree.xpath('//*[@id="mw-content-text"]/p/a/@href|//*[@id="mw-content-text"]/p/i/a/@href')
        if (len(links) == 0):
            page = requests.get('https://en.wikipedia.org/w/index.php?search=' + subject)
            tree = html.fromstring(page.text)
            links = tree.xpath('//*[@class="mw-search-result-heading'[1])
        title_xpath = tree.xpath('//*[@id="firstHeading"]/child::*/text()|//*[@id="firstHeading"]/text()')
        count = 0
    except:
        print "sorry page not found"
    
    while (''.join(title_xpath) != 'Philosophy'):  
        try:
            for link in links:
                if link.split('/')[1] == 'wiki':
                    chosen_link = link
                    break
            page = requests.get('https://en.wikipedia.org' + chosen_link)
            tree = html.fromstring(page.text)
	    links = tree.xpath('//*[@id="mw-content-text"]/p/a/@href|//*[@id="mw-content-text"]/p/i/a/@href')
            title_xpath = tree.xpath('//*[@id="firstHeading"]/child::*/text()|//*[@id="firstHeading"]/text()')
            count += 1
            print count, ''.join(title_xpath)
        except:
            links = tree.xpath('//*[@id="mw-content-text"]/p/b/a/@href | //*[@id="mw-content-text"]/ul[1]/li[1]/a/@href')
    should_continue = True if raw_input("Perform another search? (y/n): ") is 'y' else False
