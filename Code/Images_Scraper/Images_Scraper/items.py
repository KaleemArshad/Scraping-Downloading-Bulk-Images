# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagesScraperItem(scrapy.Item):
    # define the fields for your item here like:
    Urls = scrapy.Field()
    src = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    links = scrapy.Field()
