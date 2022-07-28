import scrapy

from computers.items import ComputersItem


class ComputersSpider(scrapy.Spider):
    name = 'computers_spider'
    start_urls = ['https://www.komputronik.pl/search-filter/5801/komputery-do-gier']

    def parse(self, response, **kwargs):
        c_list = response.css("li.product-entry2")

        for product in c_list:
            href = product.css('div.pe2-head > a::attr(href)').extract_first()

            yield response.follow(href, self.parse_product_computer)

            # c_item = ComputersItem()
            #
            # computer_name = c_list.css("div.pe2-head > a::text").getall()
            # c_name = [name.strip() for name in computer_name if name != ""]
            # c_item["name"] = c_name
            #
            # computer_price = c_list.css("div.prices > span").getall()
            # c_price = computer_price.strip()
            # c_item["price"] = c_price
            #
            # processor_model = c_list.css("div.inline-features::text").getall()
            # c_processor = [name.split("|")[0].strip() for name in processor_model ]
            # c_item["processor_model"] = c_processor
            #
            # graphics_card = c_list.css("ul.key-features2 > li:nth-child(2) > a::text").getall()
            # c_item["graphics_card"] = graphics_card
            #
            # yield c_item

    def parse_product_computer(self, response):
        def extract_with_css(query):
            return response.css(query).extract()

        def extract_first_with_css(query):
            return response.css(query).extract_first().strip()

        item = ComputersItem()

        computer_name = response.xpath("descendant-or-self::section[@id = 'p-inner-name']/h1/text()").get().strip()
        item["name"] = computer_name

        c_price = response.xpath("descendant-or-self::section[@id = 'p-inner-prices']//span[@class = 'proper']/text()").get().strip()
        item["price"] = c_price

        item['processor_model'] = response.xpath("descendant-or-self::section[@id = 'p-content-specification']//th[. = 'Model procesora']/ancestor::tr/td/text()").get().strip()
        # // *[ @ id = "p-content-specification"] / div[2] / div / div[2] / table / tbody / tr[3] / td / text()
        item['graphics_card'] = response.xpath("descendant-or-self::section[@id = 'p-content-specification']//th[. = 'Karta graficzna']/ancestor::tr/td/text()").get().strip()
        item['chipset'] = response.xpath("descendant-or-self::section[@id = 'p-content-specification']//th[. = 'Chipset płyty głównej']/ancestor::tr/td/text()").get().strip()

        yield item
    # def parse(self, response, **kwargs):
    #
    #     c_item_loader = CountryItemLoader(CountriesItem(), response.css("div.country"))
    #     c_item_loader.add_css("name", "h3.country-name::text")
    #     c_item_loader.add_css("capital", "span.country-capital::text")
    #     c_item_loader.add_css("population", "span.country-population::text")
    #     c_item_loader.add_css("area", "span.country-area::text")
    #
    #     yield c_item_loader.load_item()
