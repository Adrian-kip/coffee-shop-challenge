class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        new_order =(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None
        
        for customer in set(order.customer for order in coffee.orders()):
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
                
        return top_customer