from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    value = value.strip().replace(u'\xa0', u'')
    if value.isdigit():
        return float(value)


class ComputerItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

    name_in = MapCompose(str.strip)
    price_in = MapCompose(filter_price)
    processor_model_in = MapCompose(str.strip)
    graphics_card_in = MapCompose(remove_tags, str.strip)
    chipset_in = MapCompose(str.strip)

