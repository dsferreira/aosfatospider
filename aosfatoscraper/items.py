# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AosfatoscraperItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    fonte = scrapy.Field()
    referencias = scrapy.Field()
    check = scrapy.Field()
    #imagem1 = scrapy.Field()
    #imagem2 = scrapy.Field()
    
