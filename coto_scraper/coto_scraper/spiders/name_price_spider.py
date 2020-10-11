import scrapy
import re


class NamePriceSpider(scrapy.Spider):
    name = 'namePrice'
    start_urls = [
        'https://www.cotodigital3.com.ar/sitios/cdigi/browse/'
    ]

    def parse(self, response):
        all_category_products = response.xpath('//*[@id="products"]')
        for product in all_category_products:
            name = product.xpath('//div[@class="descrip_full"]/text()').extract()
            price = product.xpath('//span[@class="atg_store_productPrice" and not(@style)]/span[@class '
                                  '="atg_store_newPrice"]/text() | //span[@class="price_discount"]/text()').re(
                r'\$\d{'
                r'1,'
                r'5}(?:['
                r'.,'
                r']\d{'
                r'3})*('
                r'?:[., '
                r']\d{2})*')

            yield {'name': name,
                   'price': price}

            next_page = response.xpath('//a[@title = "Siguiente"]/@href').extract_first()
            next_page = response.urljoin(next_page)

            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)

