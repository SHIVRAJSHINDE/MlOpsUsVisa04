import sys
from us_visa.exception import USvisaException
try:
    x = 10
    print(x.append(5))  # AttributeError: 'int' object has no attribute 'append'


except Exception as e:
    raise USvisaException(e,sys)
