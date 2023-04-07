a = [
    1,
    2,
    3
]
print(a)
"""implicit expres as 
         to exprece "list literals" we use'[]'
                    "tuple literals"we use'()'
                    "dictionary literals" we use'{}'
                    "set literals" we use'{}'
                    "function argument/parameters"
"""
# the below example is list
a = [1,  # item 1
     2,  # item 2
     3]
print(a)
# the below example is tuple
b = (0,
     9,
     8)
print(b)
# the below example is dictionary
c = {'key1': 1,  # value for key1
     'key2': 2  # value for key2
     }
print(c)


# the bolow example is function
def my_func(a,
            b,
            c):
    print(a, b, c)


my_func(10, 20, 30)


# another example of function
def my_func2():
    a = "this is me sami i am practicing the python code"
    return a  # this code is used to ask the compiler to answer the function decleard


print(my_func2())  # this code is used to call the function

"""you can break up statments by using backslash(\)
    the other thing is we cannot write a comment at the end of backslash"""
# let as see an examle
a = 10
b = 20
c = 30
if a < b \
        and b < c \
        and c < 40:
    print("it is true")

# conditionals
a = 50
if a > 60:
    print("a is greaterthan 60")
else:
    print("a is lessthan or equal 60")

# let us see example2
a = 40
if a > 50:
    print("a is greater than 50")
else:
    if a < 30:
        print("a is lessthan or equal 30 ")
    else:
        print("a is greater than 30")

    # example 3
a = 20
if a > 30:
    print("a is greater then 30")
elif a < 30:
    print("a is less than 30")
else:
    print("a is equal to 30")
    # conditional with function


def sami_func():
    print("it is sami's function")


def kidus_func():
    print("it is kidus's function")


s = 10
sami_func() if s < 30 else kidus_func()

# other example 3
d = 10
sam = 'yes it is correct' if d > 5 else 'no it is not correct'
print(sam)

"""in the below code we will see about function
   What is function?
   let as see
"""


# EXAMPLE1

def func_z(m, k):

    return m * k


func_z(2, 3)
