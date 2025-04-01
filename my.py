class Product:
    def __init__(self, name = "None", price = 0):
        self.name = name
        self.price = price
    def info(self):
        print(f"name - {self.name}\ price - {self.price} грн")

class Customer:
    def __init__(self, name = "Ігор", cart = []):
        self.name = name
        self.cart = cart
    def add_to_cart(self, obj: Product):
        self.cart.append(obj)
    def show_cart(self):
        total_price = 0
        print(f"покупець - {self.name}")
        for i in self.cart:
            print("додано до кошика:", i.name, i.price)
            total_price += i.price
        print("загальна вартість", total_price)
d = Product("fsfqev", 200)
d1 = Product("fewvew", 230)
d2 = Product("fembjw", 180)
d3 = Product("kvjiis", 150)
d.info()
d1.info()
d2.info()
d3.info()
r = Customer()
r.add_to_cart(d)
r.add_to_cart(d1)
r.add_to_cart(d2)
r.add_to_cart(d3)
r.show_cart()



