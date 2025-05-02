class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def generate_report(self):
        for y, x in self.customers.items():
            a = 0
            for z in x:
                if z['price'] > self.tax_threshold:
                    a += z['price'] * (1 + self.tax_rate)
                else:
                    a += z['price']
            print(y)
            if a > self.discount_threshold:
                print("Eligible for discount")
            elif a > 300:
                print("Potential future discount customer")
            else:
                print("No discount")
            if a > 1000:
                print("VIP Customer!")
            elif a > 800:
                print("Priority Customer")


def calculate_shipping_fee(purchases, type):
    for purchase in purchases:
        if type == "fragile":
            if purchase.get('fragile', False):
                return 60
            else:
                return 25

        if type == "heavy":
            if purchase.get('weight', 0) > 20:
                return 50
            else:
                return 20
    return 20
