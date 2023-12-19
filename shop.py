class Item:
    def __init__(self, name, price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Item created, name : {name}")



item1 = Item(
    name="Phone",
    price=1000,
    quantity=2
)
print(item1.name)
print(item1.price)
print(item1.quantity)

