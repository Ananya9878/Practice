# def my_generator():
#     n = 1
#     print('This is the first iteration:')
#     yield n
#
#     n += 1
#     print('Next 2 iteretions')
#     yield n
#
#
# a=my_generator()
# print(next(a))
# print(next(a))


# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length-1,-1,-1):
#         yield  my_str[i]
# for char in rev_str('Happy'):
#     print(char)

# a = rev_str('Happy')
# print(next(a))


# my_list = [1,3,6,10]
# list comprehension
# print([x**2 for x in my_list])
# generator expression
# a = (x**2 for x in my_list)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# ......................................................................................................
#.................................,,,,,,,,,,,DECORATORS,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# def make_pretty(func):
#     def inner():
#         print('I got decorated')
#         func()
#     return inner()
# def ordinary():
#     print('im ordinary')
# pretty = make_pretty(ordinary)
# pretty()
# '''''''''''''''''''''''''''''''''''''
# def smart_divide(func):
#     def inner(a,b):
#         print('Im going to divide by {} by {}'.format(a,b))
#         if b == 0:
#             print('It is not possible to divide')
#             return
#         return func(a,b)
#     return inner
# @smart_divide
# def divide(a,b):
#     print(a/b)
#
# divide(3,0)
# divide=smart_divide(divide)
# print(a)



def ten():
    n=1
    while n!=10:
        yield n
        n+=1
a = ten()
print(next(a))
print(next(a))
















