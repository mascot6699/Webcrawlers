#!/usr/bin/env python

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class CatalogSpider(BaseSpider):
    name = "links"
    allowed_domains = ["dir.indiamart.com"]
    start_urls = [
        "http://dir.indiamart.com/indianexporters/h_miscel.html"
    ]

   
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//p[@class="cat-lst"]/a/@href').extract()
        for i in range(len(links)):
            print "http://dir.indiamart.com"+"".join(links[i])

