import scrapy

class Duck(scrapy.Spider):
start_urlsz = [
            'https://weibo.com/?category=0'
        ]
name = "weibo"
start_urls = [
            'https://weibo.com/?category=0'
        ]

def parse(self, response):

