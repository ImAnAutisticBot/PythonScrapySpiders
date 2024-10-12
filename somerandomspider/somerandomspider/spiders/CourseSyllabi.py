import scrapy

def parse_courses(response):
    for course in response.xpath('//tr[@class="coe-view-grid-row"]'):
        yield {
            'Course_Number': course.xpath('.//td[@class="views-field views-field-field-display-number is-active"]/a/text()').get().strip() if course.xpath('.//td[@class="views-field views-field-field-display-number is-active"]/a/text()').get() else None,
            'Course_Title': course.xpath('.//td[@class="views-field views-field-title"]//text()').get().strip() if course.xpath('.//td[@class="views-field views-field-title"]//text()').get() else None,
            'Credit_Hours': course.xpath('.//td[@class="views-field views-field-nothing"]/text()').get().strip() if course.xpath('.//td[@class="views-field views-field-nothing"]/text()').get() else None,
        }
    next_page = response.xpath('//li[@class="pager__item pager__item--next"]/a/@href').get()
    if next_page:
        next_page_url = response.urljoin(next_page)
        yield scrapy.Request(next_page_url, callback = parse_courses)

##########################################allcoursesyllabi##############################################################

class AllCourseSpider(scrapy.Spider):
    name = "allcoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=All']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

#########################################aeroengcoursesyllabi###########################################################

class AEROENGCourseSpider(scrapy.Spider):
    name = "aeroengcoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=1']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

########################################aviatncoursesyllabi#############################################################

class AVIATNCourseSpider(scrapy.Spider):
    name = "aviatncoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=2']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

#########################################bmecoursesyllabi###############################################################

class BMECourseSpider(scrapy.Spider):
    name = "bmecoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=3']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

#########################################cbecoursesyllabi###############################################################

class CBECourseSpider(scrapy.Spider):
    name = "cbecoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=4']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

#######################################civilencoursesyllabi#############################################################

class CIVILENCourseSpider(scrapy.Spider):
    name = "civilencoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=5']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

##########################################csecoursesyllabi##############################################################

class CSECourseSpider(scrapy.Spider):
    name = "csecoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=6']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

##########################################ececoursesyllabi##############################################################

class ECECourseSpider(scrapy.Spider):
    name = "ececoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=7']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

##########################################engrcoursesyllabi#############################################################

class ENGRCourseSpider(scrapy.Spider):
    name = "engrcoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=8']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

###########################################isecoursesyllabi#############################################################

class ISECourseSpider(scrapy.Spider):
    name = "isecoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=9']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

#########################################matscencoursesyllabi###########################################################

class MATSCENCourseSpider(scrapy.Spider):
    name = "matscencoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=10']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)

#########################################mechengcoursesyllabi###########################################################

class MECHENGCourseSpider(scrapy.Spider):
    name = "mechengcoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=11']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):
        yield from parse_courses(response)