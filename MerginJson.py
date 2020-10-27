import json
from firebase import firebase
import re
from time import sleep
firebase = firebase.FirebaseApplication('https://listy-itba-app.firebaseio.com/')
if __name__ == '__main__':

    with open('./coto_scraper/data.json') as file:
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
            true_name = re.sub(' +', ' ', names[i].replace('\n','').replace('\r','').replace('\t', '').rstrip())
            true_name = re.sub('( \.)+', '', true_name)
            product = {'name': true_name, 'price': prices[i].replace('\n', '').replace('\r', '').replace('\t', '')}
            products.append(product)
            firebase.post('products', product)
            sleep(30)
            print(product)
        if make_change:
            product = {'name': names[cant_names - 1], 'price': -1}
    with open('products.json', 'w', encoding='utf-8') as json_file:
        json.dump(products, json_file, ensure_ascii=False)
