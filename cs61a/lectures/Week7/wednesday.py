# A class statement creates a new class and binds that class to <name> in the first frame of the current environment.
# class <name>:
#     <suite>
# Assignment & def statements in <suite> create attributes of the class (not names in frame)

class Clown:
    """An illustration of a class statement. This class is not useful.

    >>> Clown.nose
    'big and red'
    >>> Clown.dance()
    'No thanks'
    """
    nose = 'big and red'
    def dance():
        return 'No thanks'


class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """

    interest = 0.02  # A class attribute

    # These def statements create function objects as always, but their names are bound as attributes of the class.
    # All invoked methods have access to the object via the self parameter, ans so they can all access and manipulate the object's state.
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

tom_account = Account("Tom") # self
tom_account.deposit(100) # self.balance

# Accessing Attributes
# getattr and dot expression look up a name in the same way
john = Account("john")
john.deposit(2000)
getattr(john, "balance")
getattr(john, "deposit")
hasattr(john, "balance")

# Methods and Functions
# Bound methods, which couple together a function and the object on which that method will be invoked.
# Object + Function = Bound Method
type(Account.deposit)       # <class 'function'>
type(tom_account.deposit)   # <class 'method'>
Account.deposit(tom_account, 1001)
tom_account.deposit(1000)

# Each call to Account creates a new Account instance. There is only one Account class.
a = Account("Jim"); a.balance; b = Account("Jack"); b.holder
# Identity operator 'is'  and 'is not' test if two expressions evaluates to the same object.
a is a; a is not b
# Binding an object to a new name using assignment does not create a new object
c = a; c is a 

# Dot Expressions
# Objects receive message via dot notation.
# Dot notation accesses attributes of the instance or its class.
# <expression>.<name>

# Class Attributes
# Class attributes are "shared" across all instances of a class because they are atrributes of the class, not the instance

# Assignment to Attributes
# Assignment statements with a dot expression on their left-hand side affect attributes for the object of that dot expression.
# If the object is an instance, then assignment sets an instance attribute.
# If the object is an class, then assignment sets a class attribute.

jim_account = Account("Jim")
tom_account.interest   # 0.02
jim_account.interest   # 0.02
Account.interest = 0.04
tom_account.interest   # 0.04
jim_account.interest   # 0.04
jim_account.interest = 0.08
jim_account.interest   # 0.08
tom_account.interest   # 0.04
Account.interest = 0.05
tom_account.interest   # 0.05
jim_account.interest   # 0.08

