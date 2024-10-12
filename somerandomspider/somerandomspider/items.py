# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    Course_Number = scrapy.Field()
    Course_Title = scrapy.Field()
    Credit_Hours = scrapy.Field()

class FacultyItem(scrapy.Item):
    Name = scrapy.Field()
    Appointment = scrapy.Field()
    Category = scrapy.Field()
    Phone = scrapy.Field()
    Email = scrapy.Field()
    Address = scrapy.Field()

class LeedcodeItem(scrapy.Item):
    Title = scrapy.Field()
    Acceptance = scrapy.Field(
    Difficulty = scrapy.Field()