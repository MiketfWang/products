products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break # 有輸入商品才需問價格/q即可離開
	price = input('請輸入商品價格: ')
	# p = []
	# p.append(name) # 建立小清單(小火車)
	# p.append(price)
	# p = [name, price] (7-9行可以精簡成一行)
	# products.append(p) # 裝進大清單(大火車)
	products.append([name, price]) # 直接(10-11行)更精簡!!
print(products)

products[0][0] # 左0大為清單中的第一個/右0為小清單的第一個