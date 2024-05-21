##Print the type of object
x=type(19.5)
print(x)

##/ operator returns float
print(5/2)

##// returns int
print(5//2)

###help(function name) gives information about the funtion
help(round)
print(round(10.1234,ndigits=2)) ##10.12 output

###docstring begings and ends with """ . It is used for adding description of the function

def leastdiff(a,b,c):
    """return the least difference between 3 numbers
    >>>leastdiff(4,5,6)
    1
    """
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(c-a)

    return min (diff1,diff2,diff3) ###If return is not used then none will be printed

print(leastdiff(9,4,3))

#leastdiff(8,5,1)

def multibyfive(x): 
    return 5 * x

###calling function from another function

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)





