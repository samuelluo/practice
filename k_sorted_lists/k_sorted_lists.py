"""
Return a new sorted merged list from K sorted lists, each with size N.
"""

import heapq

def sort_lists(lists):
    merged = []
    heap = []
    #heap = [[l[0], list_index, 0] for list_index, l in enumerate(lists) if len(l) != 0]
    for list_index in range(len(lists)):
        list_i = lists[list_index]
        if len(list_i) != 0:
            # value, list_index, element_index
            heap.append([list_i[0], list_index, 0])
    heapq.heapify(heap)
    
    while len(heap) != 0:
        value, list_index, element_index = heapq.heappop(heap)
        merged.append(value)
        if element_index + 1 < len(lists[list_index]):
            # Finding next minimum using heap/PQ is O(log n)
            # Finding next minimum through traverse & select is O(n)
            heapq.heappush(heap, [lists[list_index][element_index + 1],
                                  list_index,
                                  element_index + 1])
    return merged
        
def heapify(heap):
    pass

def heappop(heap):
    pass
    
lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
result = sort_lists(lists)
print(result)

lists = [[], [], [1,2,3]]
result = sort_lists(lists)
print(result)