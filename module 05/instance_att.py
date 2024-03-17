class Shop:
    shopping_mall = 'buyer'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attributes

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('meh jabeeeen')
mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('ni sho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)