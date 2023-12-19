import csv


class Item:
    pay_rate = 0.8  # 20% discount on all items - this is a magic attribute / class attribute
    all_classes = []  # this is a magic attribute / class attribute

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)

        for item in items:
            print(item)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()