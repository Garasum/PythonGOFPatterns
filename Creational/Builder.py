class Laptop:
    monitor_resolution = None
    processor = None
    memory = None
    hdd = None
    battery = None

    def to_string(self):
        return print(
            "Laptop : {0}, {1}, {2}, {3}, {4}".format(self.monitor_resolution, self.processor, self.memory, self.hdd,
                                                      self.battery))


# Abstract Builder
class LaptopBuilder:
    laptop = Laptop()

    # def create_new_laptop(self):
    #     return self.laptop

    def get_laptop(self):
        return self.laptop

    def set_monitor_resolution(self):
        pass

    def set_processor(self):
        pass

    def set_memory(self):
        pass

    def set_hdd(self):
        pass

    def set_battery(self):
        pass


# Concrete Builder
class TripLaptopBuilder(LaptopBuilder):
    def set_monitor_resolution(self):
        self.laptop.monitor_resolution = "1200x800"

    def set_processor(self):
        self.laptop.processor = "Celeron 2 GHz"

    def set_memory(self):
        self.laptop.memory = "2048 Mb"

    def set_hdd(self):
        self.laptop.hdd = "250 Gb"

    def set_battery(self):
        self.laptop.battery = "12 lbs"


# Concrete Builder
class GamingLaptopBuilder(LaptopBuilder):
    def set_monitor_resolution(self):
        self.laptop.monitor_resolution = "1900x1200"

    def set_processor(self):
        self.laptop.processor = "Core i7 4.2 GHz"

    def set_memory(self):
        self.laptop.memory = "16,384 Mb"

    def set_hdd(self):
        self.laptop.hdd = "1 T"

    def set_battery(self):
        self.laptop.battery = "6 lbs"


# Director
class BuyLaptop:
    laptop_builder = None

    def set_laptop_builder(self, builder):
        self.laptop_builder = builder

    def get_laptop(self):
        return self.laptop_builder.get_laptop()

    def construct_laptop(self):
        self.laptop_builder.set_monitor_resolution()
        self.laptop_builder.set_processor()
        self.laptop_builder.set_memory()
        self.laptop_builder.set_hdd()
        self.laptop_builder.set_battery()


if __name__ == '__main__':
    trip_laptop = TripLaptopBuilder()
    shop = BuyLaptop()
    shop.set_laptop_builder(trip_laptop)
    shop.construct_laptop()

    laptop = shop.get_laptop()
    laptop.to_string()
