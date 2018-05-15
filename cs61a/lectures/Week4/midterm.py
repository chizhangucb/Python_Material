# What Would Python Print?
# The print function returns None. It also displays its arguments (seperated by space) when it is called.
# eg.  print(print(5))  => Evaluates to None; Interactive output: delayed; delayed; 6

def delay(arg):
    print("delayed")
    def g():
        return arg
    return g 

# delay(delay)()(6)()   => Interactive: delayed; delayed; 6
# print(delay(print)()(4))  => Interactive: delayed; 4; None

def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

# add(pirate(3)(square)(4), 1)   => matey; 17
# pirate(pirate(pirate))(5)(7)   => matey; matey; error

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)
horse(mask)
# 2
