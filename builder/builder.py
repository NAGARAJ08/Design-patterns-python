"""

The Builder Pattern is used to construct complex objects step by step.

It separates the construction logic from the representation of the object.
You use a Builder to specify how to construct an object, and a Director to orchestrate the building process.


Real-Life Analogy
Imagine you're ordering a customized pizza:

You can specify the size, crust type, toppings, and sauce.
You don’t care how the pizza is made internally. You just give the instructions, and the pizza builder follows them step by step.


lets take an exampel

Building a House

we want to build different types of houses:

A Wooden House with basic features.
A Glass House with advanced features.
Each house has:

Walls
Roof
Windows
Doors

"""


class House:

    def __init__(self, walls, roof, windows, doors):

        self.walls = walls
        self.roof = roof
        self.windows = windows
        self.doors = doors

    def display(self):
        print(
            f"House with {self.walls} walls, {self.roof} roof, {self.windows} windows, and {self.doors} doors.")


wooden_house = House(walls="wooden", roof="wooden", windows=4, doors=1)
glass_house = House(walls="glass", roof="glass", windows=10, doors=2)

wooden_house.display()
glass_house.display()


"""
Problems:

The constructor (__init__) gets cluttered with too many parameters.
Adding optional features (like a swimming pool) becomes messy.
It's not clear what each parameter means without additional documentation.

"""

# lets write it using the builder pattern

# the product


class House:

    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def display(self):
        print(
            f"House with {self.walls} walls, {self.roof} roof, {self.windows} windows, and {self.doors} doors.")


# builder interface

class HouseBuilder:

    def build_walls(self):
        pass

    def build_roof(self):
        pass

    def build_windows(self):
        pass

    def build_doors(self):
        pass

    def get_house(self):
        pass

# Concrete Builder for Wooden House


class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "wooden"

    def build_roof(self):
        self.house.roof = "wooden"

    def build_windows(self):
        self.house.windows = 4

    def build_doors(self):
        self.house.doors = 1

    def get_house(self):
        return self.house

# Concrete Builder for Glass House


class GlassHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "glass"

    def build_roof(self):
        self.house.roof = "glass"

    def build_windows(self):
        self.house.windows = 10

    def build_doors(self):
        self.house.doors = 2

    def get_house(self):
        return self.house


# the ultimate  director

class Director:

    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()
        return self.builder.get_house()


# Client Code
wooden_builder = WoodenHouseBuilder()
director = Director(wooden_builder)
wooden_house = director.construct_house()
wooden_house.display()


glass_builder = GlassHouseBuilder()
director = Director(glass_builder)
glass_house = director.construct_house()
glass_house.display()


"""
Director: Orchestrates the construction process.
Builder: Defines how each part of the product is built.
Product: The final object (e.g., House, Pizza).

"""
