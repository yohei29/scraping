import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parser_titles(self, response):
        for post_title in response.css('div.entries>ul>lia::text').extract():
            yield {'title':post_title}