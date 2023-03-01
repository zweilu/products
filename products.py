products = []
with open('products.csv', 'r',encoding='utf-8') as f:
	for line in f:
			if '商品，價格' in line:
				continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格:')
	
	products.append([name, price])	
print(products)

for p in products:
	print(p[0], '的價格' , p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+ ',' +p[1]+ '\n')