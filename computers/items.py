import scrapy


class ComputersItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    processor_model = scrapy.Field()
    graphics_card = scrapy.Field()
    chipset = scrapy.Field()

