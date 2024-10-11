class Item:

    pay_rate = 0.8 # 20% discount on all items - this is a magic attribute / class attribute
    all_classes = [] # this is a magic attribute / class attribute

    def __init__(self, name: str, price: int, quantity: int):

        # data validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # assigning the values to the object's properties
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_classes.append(self)

        print(f"Item created, name : {name}")

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# item1 = Item(
#     name="Phone",
#     price=1000,
#     quantity=10
# )
#
# item2 = Item(
#     name="Laptop",
#     price=2000,
#     quantity=5
# )

# print("this is without creating a instance variable", Item.pay_rate)
# print()
#
# print("this is with creating a instance variable", item1.pay_rate)
# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# print(item1.calculate_total_price())


# fetching all attributes of an object

# print(Item.__dict__) # this is for class level
# print(item1.__dict__) # this is for object/instance level
# item1.pay_rate = 0.9
# print(item1.apply_discount())
# print(item1.price)
#
# print(item2.price)
# print(Item.all_classes)
# # print("*********************")
# # for instance in Item.all_classes:
# #     print(instance.name)
# #     print(instance.price)
# #     print(instance.quantity)
# #     print(instance.calculate_total_price())
# #     print(instance.pay_rate)
# #     print(instance.apply_discount())
# #     print(instance.price)
# #     print("*********************")