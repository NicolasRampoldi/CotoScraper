import scrapy
import re


class NamePriceSpider(scrapy.Spider):
    name = 'namePrice'
    start_urls = [
        'https://www.cotodigital3.com.ar/sitios/cdigi/browse/'
    ]
    #//span[@class="price_discount"]/text()
    def parse(self, response):
        all_category_products = response.xpath('//*[@id="products"]')
        for product in all_category_products:
            name = product.xpath('//div[@class="descrip_full"]/text()').extract()
            price = product.xpath('//span[@class="atg_store_productPrice" and not(@style)]/span[@class '
                                  '="atg_store_newPrice"]/text()').re(
                r'\$\d{'
                r'1,'
                r'3}(?:['
                r'.,'
                r']\d{'
                r'3})*('
                r'?:[., '
                r']\d{2})')

            yield {'name': name,
                   'price': price}
