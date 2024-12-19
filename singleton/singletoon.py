from threading import Lock


class Singleton:

    _instance = None
    _lock = Lock()

    def __new__(cls):

        if cls._instance is None:

            with cls._lock:
                print("OBJ DOES NOT EXIST CREATING THE SAME")

                if not cls._instance:

                    cls._instance = super(Singleton, cls).__new__(cls)

                    cls._instance.client = "Raj"

        return cls._instance


Singleton1 = Singleton()
Singleton2 = Singleton()


print(Singleton1 is Singleton2)

"""

Q. Why Use cls in __new__?

The __new__ method is called before an instance is created, so it operates at the class level, not the instance level.
cls refers to the class that is being instantiated (or subclassed), so it allows the creation of the right type of object.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

This ensures only one instance of the class is created, even if subclasses are involved.



Q. How is cls Different from self?

Aspect	            self	                        cls
Refers To	        The instance of the class	    The class itself
Used In	            Instance methods	            Class methods, __new__
Example Usage	    Accessing instance attributes	Creating or interacting with class attributes or instances
When Available	    After the instance is created	Before the instance exists



Q. Explanation of super(Singleton, cls).__new__(cls)

cls._instance = super(Singleton, cls).__new__(cls)

-> super(Singleton, cls) refers to calling the parent class (Singleton)'s method.
-> super() allows access to methods in a parent class.
-> cls.__new__(cls) is used to create the new object of the class. This allows you to control the instantiation of the object.
-> By using super().__new__(cls), we ensure the class (or subclass) can correctly create an instance.


Q. Why Use super() Even When Not Inheriting?

In Python, all classes inherit from the base object class (even if we don't explicitly inherit from any class). 
So, when you use super(), you're calling the object.__new__(cls) method, which is part of the class hierarchy.


Q When and Why is cls Used in Singleton?

1. Creating Instances Dynamically:
    You use cls to create a new instance of the class dynamically via super().__new__(cls) or object.__new__(cls).

2. Supporting Inheritance:
    If a subclass inherits your class, the cls in __new__ will refer to the subclass, ensuring the correct instance type is created.

    
************************


Real-World Examples of Singleton Pattern
1. Database Connection Pools
Problem: Multiple database connections are expensive and inefficient.
Why Singleton: One instance manages a single pool of database connections.
2. Logging
Problem: Logging should be done via a single, centralized instance.
Why Singleton: Avoids multiple instances writing to different log files.




When NOT to Use a Singleton
If the class is supposed to be stateful and its state can change dynamically across different parts of your application, avoid using Singleton.

Avoid Singletons when working with multi-threaded applications where each thread may need a different instance.

"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            print(cls._instances)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):

    def __init__(self):
        self.connection_string = "localhost:27017"


class Logger(metaclass=SingletonMeta):

    def __init__(self):
        self.log_file = "/var/log/app.log"


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)


l1 = Logger()
l2 = Logger()

print(l1 is l2)
