"""
Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit &
loss you could have made from buying and selling that stock once.
You must buy before you can sell it.
"""

prices = [9, 11, 8, 5, 7, 10]

curr_high = [0, prices[0]]    # [index, price]
curr_low  = [0, prices[0]]    # [index, price]
max_loss = [0, 0, 0]          # [max_loss, start_index, end_index]
max_gain = [0, 0, 0]          # [max_gain, start_index, end_index]
for i in range(len(prices)):
    price = prices[i]
    if price > curr_high[1]:
        curr_high = [i, price]
    if price < curr_low[1]:
        curr_low = [i, price]
    if price - curr_high[1] < max_loss[0]:
        max_loss = [price - curr_high[1], curr_high[0], i]
    if price - curr_low[1] > max_gain[0]:
        max_gain = [price - curr_low[1], curr_low[0], i]
print(max_loss)
print(max_gain)