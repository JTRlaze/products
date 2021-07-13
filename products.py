import os

product = []
if os.path.isfile('product.csv'):
    print('yeah')
    with open('products.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            product.append([name, price])
    print(product)
else:
    print('no no no ')

while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入價格')
    price = int(price)
    product.append([name, price])

with open('products.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in product:
        f.write(p[0] + ',' + str(p[1]) + '\n')
