class Pair:
    """A pair has two instance attributes:
    first and second.

    For a pair to be a well-formed list,
    second is either a well-formed list or nil.
    Some methods only apply to well-formed lists.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    elif isinstance(exp, Pair):
        arguments - exp.second.map(calc_eval)
        return calc_apply(exp.first, arguments)
    else:
        raise TypeError

def calc_apply(operator, args):
    if not isinstance(operator, str):
        raise TypeError(str(operator)+ ' is not a symbol')
    if operator == "+":
        return reduce(add, args, 0)
    elif operator == "-":
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)
    elif operator == "*":
        return reduce(mul, args, 1)
    elif operator == "/":
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + ' is an unknown operator')
