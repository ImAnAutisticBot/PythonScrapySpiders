import scrapy

class FacultySpider(scrapy.Spider):
    name = "csefaculty"
    allowed_domains = ["cse.osu.edu"]
    start_urls = ['https://cse.osu.edu/directory/faculty']

    custom_settings = {
        'FEED_EXPORT_FIELDS': ['Name', 'Appointment', 'Category', 'Phone', 'Email', 'Address']
    }

    def parse(self, response):
        for person in response.xpath('//div[@class="directory-wrapper directory-items"]/article'):
            yield {
                'Name': person.xpath('.//h2[@class="directory-grid-name"]/text()').get().strip() if person.xpath('.//h2[@class="directory-grid-name"]/text()').get() else None,
                'Appointment': person.xpath('.//div[@class="appointment-name"]/text()').get().strip() if person.xpath('.//div[@class="appointment-name"]/text()').get() else None,
                'Category': person.xpath('.//div[@class="directory-category"]/text()').get().strip() if person.xpath('.//div[@class="directory-category"]/text()').get() else None,
                'Phone': person.xpath('.//div[@class="directory-grid-phone"]/text()').get().strip() if person.xpath('.//div[@class="directory-grid-phone"]/text()').get() else None,
                'Email': person.xpath('.//div[@class="directory-grid-email"]//text()').get().strip() if person.xpath('.//div[@class="directory-grid-email"]//text()').get() else None,
                'Address': person.xpath('.//div[@class="directory-grid-address"]/text()').get().strip() if person.xpath('.//div[@class="directory-grid-address"]/text()').get() else None,
            }
        next_page = response.xpath('//li[@class="pager__item pager__item--next"]/a/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback = self.parse)
