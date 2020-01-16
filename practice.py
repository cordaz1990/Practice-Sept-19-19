#Keywords Args
def printall(*args):
    print(args)
    
>>> print(1,2.0, '3')
(1, 2.0, '3')

>>>print(1, 2.0, '3')
(1, 2.0, '3')

>>>print(1, 2.0, third = '3')
#TypeError: printall() got an unexpected keyword argument third
