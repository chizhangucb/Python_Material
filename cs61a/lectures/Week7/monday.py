# The effect of Nonlocal Statements (Python 3 language)
# Effect: future assignment to that name changes its pre-existing binding in the first non-local
# (enclosing scope) frame of the current environment in which that name is bound.
# Names listed in a nonlocal statement must refer to pre-existing bindings in an enclosing scope.
# Names listed in a nonlocal statement must collide with pre-existing bindings in the local scope (current).

# Python Particulars
# Python pre-computes which frame contains each name before executing the body of a function.
# Within the body of a function, all instances of a name must refer to the same frame.

# Mutable Values & Persistent Local State
# Mutable values can be changed without a nonlocal statement.
# E.g., using lists

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance  # Change the frame of balance to make_withdraw instead of withdraw
        # Declare the name "balance" nonlocal at the top of the body of the function in which it is re-assigned
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        # Re-bind balance in the first non-local frame in which it was bound previously.
        return balance
    return withdraw

def make_withdraw_wrong(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        # nonlocal balance
        # If we don't add it, balance is local now
        if amount > balance: # Non-local look up to balance
            return 'Insufficient funds'
        balance = balance - amount
        # Local change on balance
        # However, a variable canont be local and nonlocal at the same time
        return balance
    return withdraw

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

# Expressions are referentially transparent if substituting an expression with its value
# does not change the meaning of a program.
# Mutation operation violate the condition of referential transparency because they do more
# than just return a value; they change the environment. 

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total1 = b(3) + b(4)
# Referential transparency is lost
c = f(1)(2)
total2 = 10 + c(4)
