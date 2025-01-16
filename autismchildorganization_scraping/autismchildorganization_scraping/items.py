# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutismchildorganizationScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link=scrapy.Field()
    title=scrapy.Field()
    name=scrapy.Field()
    email_address=scrapy.Field()
    contact_number=scrapy.Field()
