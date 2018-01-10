# Abstract Toy
class Toy:
    name = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)
        return self.name


# Abstract Cat extends toy
class Cat(Toy):
    name = "Cat"


# Abstract Bear extends toy
class Bear(Toy):
    name = "Bear"


# Concrete Cat
class WoodenCat(Cat):
    name = "Wooden Cat"


class TeddyCat(Cat):
    name = "Teddy Cat"


# Concrete Bear
class WoodenBear(Bear):
    name = "Wooden Bear"


class TeddyBear(Bear):
    name = "Teddy Bear"


# Abstract Factory Interface
# TODO : Question about 'abc' and MetaClass ?
class ToyFactory:
    def getCat(self):
        pass

    def getBear(self):
        pass


# Concrete Factory - Wooden
class WoodenFactory(ToyFactory):
    def getCat(self):
        return WoodenCat()

    def getBear(self):
        return WoodenBear()


# Concrete Factory - Teddy
class TeddyFactory(ToyFactory):
    def getCat(self):
        return TeddyCat()

    def getBear(self):
        return TeddyBear()


def main():
    w_factory = WoodenFactory()
    w_bear = w_factory.getBear().get_name()
    w_cat = w_factory.getCat().get_name()

    t_factory = TeddyFactory()
    t_bear = t_factory.getBear().get_name()
    t_cat = t_factory.getCat().get_name()

if __name__ == '__main__':
    main()
