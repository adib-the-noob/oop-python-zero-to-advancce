from shop import Item

class Phone(Item):
    all = []
    def __init__(self, name: str, price: int, quantity: int, broken_phones: int = 0):
        # data validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"

        # assigning the values to the object's properties
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

        print(f"Item created, name : {name}")