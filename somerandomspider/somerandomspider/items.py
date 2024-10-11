# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CSECourseItem(scrapy.Item):
    Course_Number = scrapy.Field()
    Course_Title = scrapy.Field()
    Credit_Hours = scrapy.Field()
