import scrapy
from ..items import ImagesScraperItem
import csv


class ImagesFamousBirthdaysSpider(scrapy.Spider):
    name = 'url'
    URLs_list = []
    final_urls = []
    start_urls = []
    with open("F:/CODE/Ezra's Script/URLs.csv", 'r')as f:
        data = csv.reader(f)
        for row in data:
            for link in row:
                start_urls.append(link)
        start_urls.pop(0)
    print(len(start_urls))

    def parse(self, response):
        items = ImagesScraperItem()
        urls = response.css('a.face::attr(href)').extract()

        for href in urls:
            ImagesFamousBirthdaysSpider.URLs_list.append(href)

        url_set = (ImagesFamousBirthdaysSpider.URLs_list)
        for link in url_set:
            if "https://www." in link:
                ImagesFamousBirthdaysSpider.final_urls.append(link)
            else:
                pass

        for url in ImagesFamousBirthdaysSpider.final_urls:
            items['Urls'] = url

        yield items
