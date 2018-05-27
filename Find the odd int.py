# def find_it(seq):
#     for i in seq:
#         num = seq.count(i)
#         if num % 2:
#             break
#     return i
# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

import operator
import functools
def find_it(xs):
    return functools.reduce(operator.xor, xs)
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))