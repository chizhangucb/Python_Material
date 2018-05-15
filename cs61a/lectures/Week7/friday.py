# All objects have attributes, which are name-value pairs
# Classes are objects too, so they have attributes.
# Instance attribute: attribute of an instance
# Class attribute: attribute of the class of an instance.

# Functions are objects.
# Bound methods are also objects: a function that has its first parameter 'self' already bound to an instance.
# Dot expression evaluate to bound methods for class attributes that are functions.

# Inheritance
# Inheritance is a method for relating classes together.
# A common use: two similar classes differ in their degree of speclalization.
# The specialzied class may have the same attributes as the general class, along with some special-case behavior.
# class <name>(<base class>):
#     <suite>
# The new subclass "shares" attributes with its base class.
# The subclass may override certain inherite attributes.

class Account:
    """An account has a balance and a holder.

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
    """

    interest = 0.02  # A class attribute

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

class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

# Base class attributes aren't copied into subclasses.
# To look up a name in a clss.
# 1. If it names an attribute in the class, return the attribute value.
# 2. Otherwise, look up the name in the base class, if there is one.

ch = CheckingAccount("Tom")
ch.interest    # 0.01 instead of 0.02
ch.deposit(20)
ch.balance     # 20

# Designing for Inheritace
# Don't repeat yourself; use existing implementation.
# Attributes that have been overridden are still accessible via class objects.
# Look up attributes on instances whenever possible.

# Inheritance and Composition
# 1. Inheritance is best for representing is-a relationships.
# eg. a checking account is a specific type of account. So, CheckingAccount inherits from Account.
# 2. Composition is best for representing has-a relationships.
# eg. a bank has a collection of bank accounts it managse.
# So, a bank has a list of accounts as an attribute.

class Bank:
    """A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> jack.interest
    0.01
    >>> john.interest = 0.06
    >>> bank.pay_interest()
    >>> john.balance
    10.6
    >>> jack.balance
    5.05
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, account_type=Account):
        """Open an account_type for holder and deposit amount."""
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        """Pay interest to all accounts."""
        for account in self.accounts:
            account.deposit(account.balance * account.interest)

class SavingsAccount(Account):
    """A bank account that charges for deposits."""

    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

# A class may inherit from multiple base classes in Python.

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """A bank account that charges for everything."""

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar!

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]
# As long as we have single inheritance, __mro__ is just the tuple of: the class, its base, its base's base, 
# and so on up to object(only works for new-style classes of course).
# eg. AsSeenOnTVAccount.mro()[0].__name__   # 'AsSeenOnTVAccount'
