import numpy
import timeit

# -------------------------------------------------------------------
def present_value_1(cf_list, discount_rate):
    if discount_rate <= -1:
        return None
    pv = 0
    for i in range(len(cf_list)):
        cf_i = cf_list[i]
        n = i + 1
        pv += cf_i / ((1+discount_rate)**n)
    return pv

def present_value_2(cf_list, discount_rate):
    if discount_rate <= -1:
        return None
    def discount(c, r, n):
        return c / ((1+r)**n)
    discount = numpy.vectorize(discount)
    cf_list = discount(c=cf_list, r=discount_rate, n=range(1, len(cf_list)+1))
    pv = sum(cf_list)
    return pv

# -------------------------------------------------------------------
cf_list = numpy.random.choice(10, 100)
discount_rate = 0.05

result = present_value_1(cf_list, discount_rate)
print(result)
result = present_value_2(cf_list, discount_rate)
print(result)
print()

# Performance between for-loop and numpy.vectorize is roughly the same...
# TODO: test reduce(map())
t = timeit.Timer(lambda: present_value_1(cf_list, discount_rate))
print(t.timeit(number=1000))
t = timeit.Timer(lambda: present_value_2(cf_list, discount_rate))
print(t.timeit(number=1000))
print()