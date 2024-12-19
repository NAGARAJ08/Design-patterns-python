"""

Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

The Factory Design Pattern is a way to create objects without specifying the exact class of the object. 
Instead of directly creating the object with new or __init__, you delegate that job to a factory (a function or class).

Simplest Example
Imagine you're at a pizza shop. You don’t make the pizza yourself; you just tell the shopkeeper what type of pizza you want, and they make it for you.

In programming terms:

The factory is the pizza shop.
The products are different types of pizzas.
You, the customer, don't care how the pizza is made; you just want the right type of pizza.


"""


class Pizza:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing a delicious {self.name} pizza!")


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__('cheese')


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__('Veggie')


def pizza_shop(pizza_type):

    if pizza_type == 'cheese':
        return CheesePizza()
    elif pizza_type == "veggie":
        return VeggiePizza()
    else:
        raise ValueError("Unknown pizza type!")


my_pizza = pizza_shop('cheese')
my_pizza.prepare()


#############################################################################################

# Other examples:
"""
lets take an example of e-commerce platform where customers can place orders for different types of shipping:

Standard Shipping
Takes 5-7 business days.

Express Shipping
Takes 1-2 business days.

International Shipping
Requires additional customs processing.

"""

# With Factory pattern:


class Shipping:

    def calculate_cost(self):
        raise NotImplementedError("Subclasses must implement this method")


class StandardShipping(Shipping):

    def calculate_cost(self):
        return 10.0


class ExpressShipping(Shipping):
    def calculate_cost(self):
        return 20.0


class InternationalShipping(Shipping):
    def calculate_cost(self):
        return 40.0

# added later


class SameDayShipping(Shipping):
    def calculate_cost(self):
        return 12.50


def shipping_factory(shipping_type):

    if shipping_type == 'standard':
        return StandardShipping()
    elif shipping_type == 'express':
        return ExpressShipping()

    elif shipping_type == 'international':
        return InternationalShipping()
    elif shipping_type == 'sameday':
        return SameDayShipping()
    else:
        raise ValueError(f"Unknown shipping type: {shipping_type}")


# client code:

def process_order(order_type):
    shipping = shipping_factory(order_type)
    print(f"Shipping cost: ${shipping.calculate_cost()}")


process_order("standard")
process_order("express")
process_order("international")

# added later
process_order('sameday')


#  now if you want to add new type of shipping you can just add the same in the factory method and write the class for it
# and ask client to pass that value to get the cost for that shipping type


# without factory

def process_order(order_type):

    if order_type == 'standard':
        shipping = StandardShipping()
    elif order_type == 'express':
        shipping = ExpressShipping()
    elif order_type == 'internatitonal':
        shipping = InternationalShipping()
    elif order_type == 'sameday':
        shipping = SameDayShipping()
    else:
        raise ValueError(f"Unknown shipping type: {order_type}")

# As we can see here, the client needs to know which specific class or function to call for a given shipping type.
# This leads to repetitive if-else conditions every time this logic is needed, making the code harder to maintain and extend.
