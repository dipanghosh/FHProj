'''
Created on 22 May 2017

@author: dghosh
'''
import inspect
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        
        print '%f sec' % \
              (te-ts)
#         print '%r (%r, %r) %f sec' % \
#               (method.__name__, args, kw, te-ts)
        return result

    return timed
def printDebugInfo(func):
    '''
    Prints debug info to the console, saying which function is being called, with what arguments
    '''
    def decorated(*args, **kwargs):
        print("{} has been called with the arguments{}".format(func.__name__,args))
        return func(*args, **kwargs)
    return decorated

@timeit
@printDebugInfo
def my_function(i):
    num_list = []
    for num in (range(0, (10**i))):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))
if __name__ == "__main__":
    for i in range(0,7):
        my_function(i)

