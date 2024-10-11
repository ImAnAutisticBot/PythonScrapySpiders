import scrapy

class CSECourseSpider(scrapy.Spider):
    name = "csecoursesyllabi"
    allowed_domains = ["syllabi.engineering.osu.edu"]
    start_urls = ['https://syllabi.engineering.osu.edu/?field_fiscal_unit_academic_org_target_id=6']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Course_Number', 'Course_Title', 'Credit_Hours']
    }

    def parse(self, response):

        for course in response.xpath('//tr[@class="coe-view-grid-row"]'):
            yield {
                'Course_Number': course.xpath('.//td[@class="views-field views-field-field-display-number is-active"]/a/text()').get().strip() if course.xpath('.//td[@class="views-field views-field-field-display-number is-active"]/a/text()').get() else None,
                'Course_Title': course.xpath('.//td[@class="views-field views-field-title"]//text()').get().strip() if course.xpath('.//td[@class="views-field views-field-title"]//text()').get() else None,
                'Credit_Hours': course.xpath('.//td[@class="views-field views-field-nothing"]/text()').get().strip() if course.xpath('.//td[@class="views-field views-field-nothing"]/text()').get() else None,
            }

        next_page = response.xpath('//li[@class="pager__item pager__item--next"]/a/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback = self.parse)

