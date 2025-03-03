# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage

import scrapy

class InstituteSpider(scrapy.Spider):
    name = 'institute'
    start_urls = ['https://kpgu.ac.in']

    def parse(self, response):
        # Define how to extract data here
        data = {
            'title': response.css('h1::text').get(),
            'description': response.css('p::text').get(),
        }
        yield data

        # Follow links to other pages if needed
        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, self.parse)
