import numpy
import random

# -------------------------------------------------------------------
def present_value(cf_list, discount_rate):
    """
    cf_list (integer list): list of cashflows
    discount_rate (float): (-1, inf]
    """
    # TODO: vectorize pv calculation; compare speed
    if discount_rate <= -1:
        return None
    pv = 0
    for i in range(len(cf_list)):
        cf_i = cf_list[i]
        n = i + 1
        pv += cf_i / ((1+discount_rate)**n)
    return pv

def find_discount_rate(cf_list, target_pv):
    """
    x[n+1] = x[n] - f(x)/f'(x)
    discount_rate = discount_rate - cost/cost_prime
    cost = curr_pv - target_pv
    curr_pv = present_value(cf_list, discount_rate)
    cost_prime = d(cost)/d(discount_rate) = curr_pv_prime
    curr_pv_prime = present_value(cf_list, discount_rate+epsilon)
    """
    # Set up
    discount_rate = random.random()
    epsilon = 0.001
    threshold = 0.01

    # Iterate
    curr_pv = present_value(cf_list, discount_rate)
    while curr_pv < target_pv-threshold or curr_pv > target_pv+threshold:
        curr_pv = present_value(cf_list, discount_rate)
        curr_pv_1 = present_value(cf_list, discount_rate+epsilon)
        curr_pv_prime = (curr_pv_1 - curr_pv)/epsilon
        cost = curr_pv - target_pv
        cost_prime = curr_pv_prime
        discount_rate = discount_rate - cost/cost_prime
        print([curr_pv, target_pv])

    # Return
    return discount_rate

# -------------------------------------------------------------------
cf_list = [5, 5, 105]
discount_rate = 0.05
result = present_value(cf_list, discount_rate)
print(result)

cf_list = [5, 5, 5]
discount_rate = 1
result = present_value(cf_list, discount_rate)
print(result)

cf_list = [5, 5, 105]
target_pv = 100
result = find_discount_rate(cf_list, target_pv)
print(result)

