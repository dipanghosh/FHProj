#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bonisonaDec(func):
    """ This is the decorator for adding your name to any function you wish! The benefit now is that you just add the decorator, and get an awesome badge!  Notice this function, takes any function
    as the argument, prints the thing, then spits the function back out, so that it can be executed. If you do not return the function, it will never get executed.
    """
    print "\n\n-------------------------------------Welcome! স্বনামধন্য বনিসোনা----------------------------------"
    print func.__name__ + " has been decorated with your name!"
    return func


@bonisonaDec  # I am decorating the justprint function... You get the idea...
def justprint(n):
    print(n)


justprint("WHatever!")


@bonisonaDec
def printSquare():
    for i in range(20):
        print i ** i


printSquare()


@bonisonaDec
def fib(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    else:
        return (fib(num - 1) + fib(num - 2))


print fib(4)

'''
Here is a more useful/advanced application

def echo(fn):
    from itertools import chain
    def wrapped(*v, **k):
        name = fn.__name__
        print "%s(%s)" % (name, ", ".join(map(repr, chain(v, k.values()))))
        return fn(*v, **k)
    return wrapped

Use this as a decorator to see functioncalls with their arguments. Apply this on the recursive function fib(), where the function is called many times.
'''
