import scrapy

class LeetcodeSpider(scrapy.Spider):
    name = "leetcodespider"
    allowed_domains = ["leetcode.com"]
    start_urls = ['https://leetcode.com/problemset/']

    # def start_requests(self):
    #     cookies = {
    #         'name_of_cookie': 'value_of_cookie',  # 替换为实际的 Cookie
    #     }
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, cookies=cookies, callback=self.parse)

    def parse_problems(self, response):
        for problem in response.xpath('//div[@row="rowgroup"]'):
            yield {
                'Title': problem.xpath('.//div[@class="truncate"]/a/text()').get().strip() if problem.xpath('.//div[@class="truncate"]/a/text()').get() else None,
                'Acceptance': problem.xpath('.//div[@style="box-sizing: border-box; flex: 100 0 auto; min-width: 0px; width: 100px;"]/span/text()').get().strip() if problem.xpath('.//div[@style="box-sizing: border-box; flex: 100 0 auto; min-width: 0px; width: 100px;"]/span/text()').get() else None,
                'Solution': problem.xpath('.//div[@style="box-sizing: border-box; flex: 84 0 auto; min-width: 0px; width: 84px;"]/span/text()').get().strip() if problem.xpath('.//div[@style="box-sizing: border-box; flex: 84 0 auto; min-width: 0px; width: 84px;"]/span/text()').get() else None,
            }
        next_page = response.xpath('//button[@aria-label="next"]/following-sibling::a/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback = self.parse_problems)
