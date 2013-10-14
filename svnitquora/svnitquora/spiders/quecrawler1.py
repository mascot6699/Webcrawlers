from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class SvnitquoraSpider(BaseSpider):
    name = "que1"
    allowed_domains = ["http://www.quora.com"]
    start_urls = [
        "http://www.quora.com/Sardar-Vallabhbhai-National-Institute-of-Technology-Surat/questions"
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        fo = open("infogathered.txt", "wb")
        sites = hxs.select('//div/div') 
        for site in sites:
            questions = site.select('h3/span/a/text()').extract()
            ansnum = site.select('div/span/a/text()').extract()
            if not questions:
                pass
            else:
                q1 = ' '.join(' '.join(questions).split())
                fo.write("Question: \t" +q1 +"\n")
            if not ansnum:
                pass
            else:
                fol1 = ' '.join(' '.join(ansnum).split())
                fo.write(":\t" +fol1+"\n\n")