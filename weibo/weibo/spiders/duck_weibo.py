import scrapy

class Duck(scrapy.Spider):
        name = "weibo"
        start_urls = [
                'https://weibo.com/?category=0'
        ]

def parse(self, response):

