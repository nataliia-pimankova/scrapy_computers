import csv

from itemadapter import ItemAdapter


class ComputersPipeline:
    def open_spider(self, spider):
        print('open_spider', spider)
        self.file = open('items.csv', 'w')
        self.writer = csv.DictWriter(self.file, ['name', 'price', 'processor_model', 'chipset', 'graphics_card'])
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print('process_item', item, spider)
        self.writer.writerow(ItemAdapter(item).asdict())
        return item
