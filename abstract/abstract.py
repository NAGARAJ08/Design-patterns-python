"""
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

The Abstract Factory Pattern is like a factory of factories. Instead of creating individual objects, it creates families of related or dependent objects without specifying their exact classes.

Real-Life Analogy

 The furniture depends on the theme of the room:

Modern Theme: You get a modern chair, modern table, and modern sofa.
Victorian Theme: You get a Victorian chair, Victorian table, and Victorian sofa.
Instead of picking each piece individually, you go to a theme store (the abstract factory), which provides all furniture for the chosen theme.

"""
# Example

# E-commerce Payment and Notifications
"""
Let’s say an e-commerce platform supports:

Payment Systems: Credit Card, PayPal.
Notification Systems: Email, SMS.
Each payment system has a corresponding notification type. For instance:

Credit Card → Email Notification
PayPal → SMS Notification

"""


# lets first see with out abstract factory pattern


class CreditCardPayment:

    def process_payment(self):
        return "Payment processed using Credit Card."


class PayPalPayment:
    def process_payment(self):
        return "Payment processed using PayPal."


class EmailNotification:
    def send_notification(self):
        return "Notification sent via Email."


class SMSNotification:
    def send_notification(self):
        return "Notification sent via SMS."


# client code:

def processs_order(payment_type):
    if payment_type == 'credit':
        payment = CreditCardPayment()
        notification = EmailNotification()
    elif payment_type == "paypal":
        payment = PayPalPayment()
        notification = SMSNotification()
    else:
        raise ValueError(f"Unknown payment type: {payment_type}")

    print(payment.process_payment())
    print(notification.send_notification())


processs_order('credit')

"""
if-else logic is repetitive and hard to maintain.
Adding a new payment system means updating multiple places.

"""
# with abstract factory:


class Payment:
    def process_payment(self):
        pass


class Notification:
    def send_notification(self):
        pass


# concrete produccts

class CreditCardPayment(Payment):

    def process_payment(self):
        return "Payment processed using Credit Card."


class PayPalPayment(Payment):

    def process_payment(self):
        return "Payment processed using Paypal."


class EmailNotification(Notification):
    def send_notification(self):
        return "Notification sent via Email."


class SMSNotification(Notification):
    def send_notification(self):
        return "Notification sent via SMS."


# abstract factory:

class PaymentFactory:
    def create_payment(self):
        pass

    def create_notification(self):
        pass


class CreditCardFactory(PaymentFactory):
    def create_payment(self):
        return CreditCardPayment()

    def create_notification(self):
        return EmailNotification()


class PayPalFactory(PaymentFactory):
    def create_payment(self):
        return PayPalPayment()

    def create_notification(self):
        return SMSNotification()


def process_order(factory):

    payment = factory.create_payment()
    notification = factory.create_notification()
    print(payment.process_payment())
    print(notification.send_notification())


process_order(PayPalFactory())


"""
Client Side:
The client says, "I want to process an order using a credit card."
The client calls the CreditCardFactory and doesn't care how things are managed internally.

Factory Side (Abstracting the Details):

The CreditCardFactory handles everything related to credit card payments.
It creates the CreditCardPayment object to process the payment.
It also creates the EmailNotification object to notify the user.
The client doesn’t know or care about these details—it just gets the job done!


"""
