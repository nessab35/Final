# person
class Person():
    '''Person'''
    def __init__(self, name, fav_drink, wallet = 0.0, tip_percent = 0.0):
        self.name = name
        self.fav_drink = fav_drink
        self.wallet = wallet
        self.tip_percent = tip_percent

    def my_order(self):
        # create instance of Order with person and fav_drink
        order = Order(self, self.fav_drink, self, self.tip_percent)
        return order



class Order():
    '''Order'''
    def __init__(self, person, drink_type, price = 0.0, tip_percent = 0.0):
        self.person = person
        self.drink_type = drink_type
        self.price = price
        self.tip_percent = tip_percent

    def to_string(self):
        return f"{self.person.name} orders: {self.drink_type}. Price: ${self.price:.2f} Tip: {self.tip_percent}"

    def calculate_price_with_tip(self):
        base_price = CoffeeBar.calcuate_price(self.drink_type)
        tip_amount = base_price * self.tip_percent / 100
        return base_price + tip_amount



class CoffeeBar():
    '''Coffee Shop'''
    def __init__(self, name, register= 0.0, tip_jar = 0.0, barista = None):
        self.name = name
        self.barista = barista
        self.register = register
        self.tip_jar = tip_jar
        self.orders_list = []
        self.receipts = []

    def set_barista(self, barista):
        self.barista = barista

    @staticmethod
    def calcuate_price(drink_type):
        if drink_type == "Coffee":
            return 5.00
        elif drink_type == "Milk":
            return 2.50
        elif drink_type == "Tea":
            return 3.50
        elif drink_type == "Mathcha" or "Chai":
            return 4.50
        else:
            return 0.0

    def place_order(self, order):
        order.price = order.calculate_price_with_tip()
        self.orders_list.append(order)

    def process_order(self):
        if self.barista:
            barista_greeting = self.barista.greeting
        else:
            barista_greeting = "Welcome to Nessa's Coffee Shop!"

        if not self.orders_list:
            print("No orders at this time! :)")
        else:
            for order in self.orders_list:
                self.charge_customer(order)
                print(f"{barista_greeting} {order.to_string()}")

                self.receipts.append(order)

        self.orders_list.clear()

    def charge_customer(self, order):
        total_cost = order.price
        tip_amount = (total_cost * order.tip_percent) / 100
        order.person.wallet -= total_cost
        self.register += total_cost
        self.tip_jar += tip_amount

    def cash_out(self):
        print(f"Total in register: ${self.register:.2f}")
        print(f"Tip Jar: ${self.tip_jar:.2f}")

        self.barista.wallet += self.tip_jar
        self.tip_jar = 0.0



class Barista(Person):
    '''Barista'''
    def __init__(self, name, greeting):
        super().__init__(name, "Coffee")
        self.greeting = greeting






# TEST CODE
if __name__ == "__main__":
    # creating instance
    amy = Person("Amy", "Coffee", 50.0, 20.0)
    bob = Person("Bob", "Tea", 25.60, 18.0)
    cat = Person("Cat", "Milk", 78.99, 15.0)
    meghan = Person("Meghan", "Matcha", 5000.00, 0)


    # adding orders
    amy_order = amy.my_order()
    bob_order = bob.my_order()
    cat_order = cat.my_order()
    meghan_order = meghan.my_order()


    # print(amy_order.to_string())
    # print(bob_order.to_string())
    # print(cat_order.to_string())


    # creating my shop instace
    my_shop = CoffeeBar("Nessa's Coffee Shop")
    # placing peoples orders at my shop
    my_shop.place_order(amy_order)
    my_shop.place_order(bob_order)
    my_shop.place_order(cat_order)
    my_shop.place_order(meghan_order)
    print("------------------------------")


    #  making instance with barista
    kevin = Barista("Kevin", "Hey dude!")
    my_shop.set_barista(kevin)
    print("Wallet before: ")
    print(f"{amy.name} wallet: ${amy.wallet:.2f}")
    print(f"{bob.name} wallet: ${bob.wallet:.2f}")
    print(f"{cat.name} wallet: ${cat.wallet:.2f}")
    print(f"{meghan.name} wallet: ${meghan.wallet:.2f}")
    print(f"{kevin.name} wallet: ${kevin.wallet:.2f}")

    my_shop.process_order()
    # cashing out
    my_shop.cash_out()
    print("------------------------------")


    print("Receipts:")
    for receipt in my_shop.receipts:
        print(receipt.to_string())
    print("------------------------------")


    print("order list after:")
    for order in my_shop.orders_list:
        print(order.to_string())
    print("------------------------------")


    # checking each persons wallet after being charged + added money too
    print("wallet after: ")
    print(f"{amy.name} wallet: ${amy.wallet:.2f}")
    print(f"{bob.name} wallet: ${bob.wallet:.2f}")
    print(f"{cat.name} wallet: ${cat.wallet:.2f}")
    print(f"{meghan.name} wallet: ${meghan.wallet:.2f}")
    print(f"{kevin.name} wallet: ${kevin.wallet:.2f}")
    # wihtout barista
    #my_shop.process_order()
