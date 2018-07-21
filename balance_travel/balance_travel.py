"""
Suppose there are interviewing N job candidates for roles in New York and
San Francisco.
There are two costs associated with each candidate, one for sending him/her to
each city.
Split the candidates into two equal-sized groups while also minimizing travel
cost.
"""

# ---------------------------------------------------------
def balance_travel(costs):
    # Set up
    swap_costs = [(i[0]-i[1],) + i for i in costs]
    swap_costs = sorted(swap_costs, key=lambda x: x[0], reverse=True)
    ny = []
    sf = []
    i = 0

    # Assign the largest cost differences (opportunity cost) first
    while len(ny) < len(costs)//2 and len(sf) < len(costs)//2:
        cost = swap_costs[i]
        if cost[0] > 0:    # If NY > SF, send to SF
            sf.append(cost[1:])
        else:              # If NY < SF, send to NY
            ny.append(cost[1:])
        i += 1

    while len(ny) < len(costs)//2:
        cost = swap_costs[i]
        ny.append(cost[1:])
        i += 1

    while len(sf) < len(costs)//2:
        cost = swap_costs[i]
        sf.append(cost[1:])
        i += 1

    total_cost = sum([i[0] for i in ny]) + sum([i[1] for i in sf])
    print("ny: " + str(ny))
    print("sf: " + str(sf))
    print("total cost: " + str(total_cost))
    print()

# ---------------------------------------------------------
costs = [(400, 200), (200, 100), (300, 150), (100, 50)]
balance_travel(costs)

costs = [(1000, 1001), (1, 11)]
balance_travel(costs)
