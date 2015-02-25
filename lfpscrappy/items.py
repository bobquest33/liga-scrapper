# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeamClassification(scrapy.Item):
    season = scrapy.Field()
    round = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    points = scrapy.Field()

