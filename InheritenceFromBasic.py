from shop import Item

class Phone(Item):
    all = []
    def __init__(self, name: str, price: int, quantity: int, broken_phones: int = 0):

        super().__init__(name, price, quantity)
        # data validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"

        # assigning the values to the object's properties
        self.quantity = quantity
        self.broken_phones = broken_phones

        Phone.all.append(self)

        print(f"Phone created, name : {name}")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"


samsung = Phone(
    name="Samsung",
    price=5000,
    quantity=10,
    broken_phones=2
)
print(samsung.broken_phones)
print(samsung.calculate_total_price())
print(Phone.all)