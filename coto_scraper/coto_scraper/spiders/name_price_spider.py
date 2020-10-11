import scrapy
import re


class namePriceSpider(scrapy.Spider):
    name = 'namePrice'
    start_urls = [
        'https://www.cotodigital3.com.ar/sitios/cdigi/browse/'
    ]

    def parse(self, response):
        all_category_products = response.xpath('//*[@id="products"]')
        for product in all_category_products:
            name = product.xpath('//div[@class="descrip_full"]/text()').extract()
            pre_price = product.xpath('//span[@class ="atg_store_newPrice"]/br/text()').extract()
            # regex = re.compile(r"\$[1-9]+[0-9]*(\.[0-9]+)?")
            # price = regex.findall(pre_price)
            # real_price = price[0]
            yield {'name': name,
                   'price': pre_price}
        next_url = response.xpath('//*[@class = " " and @title = "Siguiente"]/@href').extract()
        if next_url:
            yield scrapy.Request(next_url, self.parse)
