#!/usr/bin/env python

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class CatalogSpider(BaseSpider):
    name = "names"
    allowed_domains = ["dir.indiamart.com"]
    '''start_urls = [
        "http://dir.indiamart.com/impcat/fresh-vegetables.html",
        "http://dir.indiamart.com/impcat/decorative-items.html"
    ]'''
    start_urls = [line.strip() for line in open("fewlinks.txt", 'r')]
   
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        catname =   hxs.select('//li[@style="border:none; color:#444;"]/text()').extract()
        pname =     hxs.select('//a[@class="product-name"]/text()').extract()
        cname =     hxs.select('//span[@class="company-name"]/span[@itemprop="name"]/text()').extract()
        lname =     hxs.select('//span[@class="company-name"]/span[@class="location"]/text()').extract()
        print catname[0],
        print " has " + str(len(pname)) + " products\n"
        if(len(lname) == len(pname)):
            for i in range(len(pname)):
                print i+1 , pname[i] , cname[i] , lname[i]
                
        print "\n"