'''
Created on 22 May 2017

@author: dghosh
'''
def containerFunc(param1):
    print "This is a bit of debug info"
    def insider(x):
        while x<10:
            x += 1
            yield x
        print "I also have"+param1
    return insider
if __name__ == "__main__":
    print(containerFunc(" test").__name__)