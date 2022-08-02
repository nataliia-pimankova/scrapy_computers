import scrapy

from computers.items import ComputersItem
from computers.item_loaders import ComputerItemLoader, ItemLoader


class ComputersSpider(scrapy.Spider):
    name = 'computers_spider'
    start_urls = ['https://www.komputronik.pl/search-filter/5801/komputery-do-gier']
    custom_settings = {
        "ITEM_PIPELINES": {
            "computers.pipelines.ComputersPipeline": 300
        }
    }

    def parse(self, response, **kwargs):
        c_list = response.css("li.product-entry2")

        for product in c_list:
            href = product.css('div.pe2-head > a::attr(href)').extract_first()
            print('href', href)
            if href:
                yield response.follow(href, self.parse_product_computer)

        # follow pagination links
        next_page_url = response.xpath('//div[contains(@class,  "pagination")]//li//i[contains(@class,  "icon-caret2-right")]/ancestor::a/@href').get()
        print('next_page_url', next_page_url)
        yield response.follow(next_page_url, callback=self.parse)

    def parse_product_computer(self, response):
        def extract_with_css(query):
            return response.css(query).extract()

        def extract_first_with_css(query):
            return response.css(query).extract_first().strip()

        c_item_loader = ComputerItemLoader(ComputersItem(), response.css("ktr-product"))
        # c_item_loader.default_selector_class
        c_item_loader.add_xpath("name", "descendant-or-self::section[@id = 'p-inner-name']/h1/text()")
        c_item_loader.add_xpath("price", "descendant-or-self::section[@id = 'p-inner-prices']//span[@class = 'proper']/text()")

        c_item_loader.add_xpath('processor_model', "descendant-or-self::section[@id = 'p-content-specification']//th[. = 'Model procesora']/ancestor::tr/td/text()")
        c_item_loader.add_xpath('graphics_card', "descendant-or-self::section[@id = 'p-content-specification']//th[. = 'Karta graficzna']/ancestor::tr/td/text()")
        c_item_loader.add_xpath('chipset', "descendant-or-self::section[@id = 'p-content-specification']//th[. = 'Chipset płyty głównej']/ancestor::tr/td/text()")

        yield c_item_loader.load_item()

