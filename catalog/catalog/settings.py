# Scrapy settings for catalog project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'catalog'

SPIDER_MODULES = ['catalog.spiders']
NEWSPIDER_MODULE = 'catalog.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'catalog (+http://www.yourdomain.com)'
