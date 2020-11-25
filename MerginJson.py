import json
from firebase import firebase
import re
import hashlib
from time import sleep
database = firebase.FirebaseApplication('https://listy-itba-app.firebaseio.com/')
if __name__ == '__main__':
    database.delete('/','products')
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
            true_name = re.sub(' +', ' ', names[i].replace('\n','').replace('\r','').replace('\t', '').replace('/', ' ').rstrip())
            true_name = re.sub('( \.)+', '', true_name)
            product = {'name': true_name,  'price': prices[i].replace('\n', '').replace('\r', '').replace('\t', '').replace('$','')}
            products.append(product)
            hash_product = hashlib.sha256(true_name.encode('utf-8')).hexdigest()
            try:
                database.put('/products/', true_name, product)
            except:
                print('funco la excepcion')
                database = firebase.FirebaseApplication('https://listy-itba-app.firebaseio.com/')
                i -= 1

            print(product)
        if make_change:
            product = {'name': names[cant_names - 1], 'price': -1}
    with open('products.json', 'w', encoding='utf-8') as json_file:
        json.dump(products, json_file, ensure_ascii=False)
