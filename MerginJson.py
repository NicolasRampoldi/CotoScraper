import json

if __name__ == '__main__':

    with open('/Users/roberto-j-catalan/CotoScraper/coto_scraper/data.json') as file:
        data = json.load(file)
        products = []
    for page in data:
        names = page["name"]
        prices = page["price"]
        cant_names = len(names)
        cant_prices = len(prices)
        print('cant name: ' + str(cant_names))
        print('cant price: ' + str(cant_prices))
        cant_products = cant_names
        make_change = False
        if cant_prices < cant_names:
            cant_products = cant_prices
            make_change = True
        for i in range(cant_products):
            product = {'name': names[i], 'price': prices[i]}
            products.append(product)
            print(product)
        if make_change:
            product = {'name': names[cant_names - 1], 'price': -1}
    with open('products.json', 'w') as json_file:
        json.dump(products, json_file)
