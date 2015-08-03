import sys
from lxml import html
import requests

try:
    subject = raw_input('Enter wikipedia page: ') #TODO what happens if page does not exist?
    page = requests.get('https://en.wikipedia.org/wiki/' + subject)
    tree = html.fromstring(page.text)
    links = tree.xpath('//*[@id="mw-content-text"]/p[1]/a[1]/@href')
    if (len(links) == 0):
        page = reqeuests.get('https://en.wikipedia.org/w/index.php?search=' + subject)
        tree = html.fromstring(page.text)
        links = tree.xpath('//*[@class="mw-search-result-heading'[1])
    title_xpath = tree.xpath('//*[@id="firstHeading"]/text()')
    count = 0
except:
    print "sorry page not found"

while (title_xpath[0] != 'Philosophy'):  
    try:
        page = requests.get('https://en.wikipedia.org' + links[0])
        tree = html.fromstring(page.text)
        links = tree.xpath('//*[@id="mw-content-text"]/p[1]/a[1]/@href')
        title_xpath = tree.xpath('//*[@id="firstHeading"]/text()')
        count += 1
        print count, title_xpath[0]
    except:
        links = tree.xpath('//*[@id="mw-content-text"]/ul[1]/li[1]/a/@href')  
