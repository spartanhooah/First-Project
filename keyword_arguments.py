def area(a, b=6):
    return a * b

print(area(b=4, a=5))
print(area(a=5))

# varargs
def mean(*args):
    return sum(args) / len(args)

# indefinite  number of keyword args
def foo(**kwargs):
    return kwargs

print(foo(a=1, b=2, c=3))