from math import sqrt
from functools import wraps


################################################################################
# Decorators
################################################################################
def Singleton(cls):
    """Singleton decorator"""
    instances = {}
    def getInstance(*args, **kwargs):
        if class_ not in instances:
            instances[cls] = class_(*args, **kwargs)
        return instances[cls]
    return getInstance


class PrintInfoClass(object):
    """Give full information about a function"""
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
    def __call__(self, *args, **kwargs):
        @wraps(self.func)
        def wrapper(*args, **kwargs):
            print 'Function   : {0}'.format(self.func.__name__)
            print '  - args   : {0}'.format(args)
            print '  - kwargs : {0}'.format(kwargs)
            output = self.func(*args, **kwargs)
            print '  - return : {0}'.format(output)
            return output
        return wrapper(*args, **kwargs)


def PrintInfo(func):
    """Give full information about a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'Function   : {0}'.format(func.__name__)
        print '  - args   : {0}'.format(args)
        print '  - kwargs : {0}'.format(kwargs)
        output = func(*args, **kwargs)
        print '  - return : {0}'.format(output)
        return output
    return wrapper


def Deprecated(fully_deprecated=True):
    def wrapper_for_function(func):
        def wrapper_for_arguments(*args, **kwargs):
            if fully_deprecated:
                print "Function deprecated : {0}".format(func.__name__)
                raise Exception("Deprecated")
            else:
                print "Function to be deprecated : {0}".format(func.__name__)
                return func(*args, **kwargs)
        return wrapper_for_arguments
    return wrapper_for_function
################################################################################


################################################################################
if __name__ == "__main__":
    """TEST"""










