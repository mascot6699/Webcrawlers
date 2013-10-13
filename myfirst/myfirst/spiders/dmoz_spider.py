#!/usr/bin/env python

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        fo = open("infogathered.txt", "wb")
        for site in sites:
            title = site.select('a/text()').extract()
            link = site.select('a/@href').extract()
            desc = site.select('text()').extract()
            title1 = ' '.join(title)
            desc1 = ' '.join(' '.join(desc).split())
            link1 = ' '.join(' '.join(link).split())
            fo.write("book name: \t" +title1 + "\n"+"description :\t"+desc1+"\n"+"link:\t"+ link1+"\n\n\n")
        # Close opend file
        fo.close()

