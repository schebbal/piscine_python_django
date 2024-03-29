class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        s = "name : " + self.name + "\nprice : " + \
            str(self.price) + "\ndescrition : " + self.description() + "\n"
        return s


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"
    price = 0.30

    def description(self):
        return "Just some hot water in a cup."


class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self):
        return "Un po' di Italia nella sua tazza!"


if __name__ == '__main__':
    a = HotBeverage()
    print(a)

    c = Coffee()
    print(c)

    t = Tea()
    print(t)

    l = Chocolate()
    print(l)

    p = Cappuccino()
    print(p)
