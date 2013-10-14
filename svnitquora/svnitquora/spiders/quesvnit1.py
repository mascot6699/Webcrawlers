from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class SvnitquoraSpider(BaseSpider):
    name = "quesvnit1"
    allowed_domains = ["http://www.quora.com"]
    start_urls = ["http://www.quora.com/Sardar-Vallabhbhai-National-Institute-of-Technology-Surat/questions"]
    def parse(self, response):
        hxs = HtmlXPathSelector(response) 
        questions = hxs.select('//div[@class="feed_item_question"]/h3/span/a/text()').extract()
        ansnum = hxs.select('//a[@class="number_answers"]/text()').extract()
        for i in range(len(questions)-1):        
            print questions[i] , ansnum[(2*i)+1],ansnum[2*i]
        

        
