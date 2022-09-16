class Manager:
    def __init__(self):
        self.orders = {}

    def add_order(self, new_order, ilosc):

        # temp_order = new_order.return_order()
        # print(f' ____________________ {self.new_order} _________________')
        if not self.orders:
            self.orders[new_order] = 1
            return
        for order in list(self.orders):
            if order.id == new_order.id:
                self.orders[order] += ilosc
                return
            else:
                self.orders[new_order] = 1

    def __str__(self):
        for key in self.orders.keys():
            print(f'{key.__str__()} {self.orders[key]}')

    def sell(self, id_to_sell):
        self.id_sell = id_to_sell.return_order()
        for order in self.orders.keys():
            if order == self.id_sell:
                if self.orders[self.id_sell] != 0:
                    self.orders[self.id_sell] -= 1

    def print_orders(self):
        print(self.orders)

class Order:

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nazwa = kwargs['nazwa']
        self.cena = kwargs['cena']

    def add(self):
        return (id, self.nazwa, self.cena)

    def __str__(self):
        return f' ({self.id} {self.nazwa} {self.cena})'

    def return_order(self) -> list:
        return (self.id, self.nazwa, self.cena)


man1 = Manager()
order1 = Order(id=1, nazwa='kasza', cena=25)
man1.add_order(order1, 1)
order2 = Order(id=2, nazwa='olej', cena = 5)
man1.add_order(order2, 5)
order3 = Order(id=1, nazwa='kasza', cena=25)
man1.add_order(order3, 1)
order4 = Order(id=1, nazwa='kasza', cena=25)
man1.add_order(order4, 1)
order5 = Order(id=1, nazwa='kasza', cena=25)
man1.add_order(order5, 1)
order6 = Order(id=1, nazwa='kasza', cena=25)
man1.add_order(order6, 1)
man1.__str__()
order7 = Order(id=1, nazwa='kasza', cena=25)
# man1.sell(order7)
# man1.__str__()
#
# order8 = Order(id=1, nazwa='kasza', cena=25)
# man1.sell(order8)
# man1.__str__()
# order8 = Order(id=1, nazwa='kasza', cena=25)
# man1.sell(order8)
# man1.__str__()
# order8 = Order(id=1, nazwa='kasza', cena=25)
# man1.sell(order8)
# man1.__str__()
# order8 = Order(id=1, nazwa='kasza', cena=25)
# man1.sell(order8)
# man1.__str__()
# order8 = Order(id=1, nazwa='kasza', cena=25)
# man1.sell(order8)
# man1.__str__()

print(man1.orders)