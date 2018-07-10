"""
Given an array of time intervals (start, end) for meetings, which may be 
overlapping, find the minimum number of meeting rooms required.

For example:
Given [(30, 75), (0, 50), (60, 150)], 2 meeting rooms are required.
"""

# ---------------------------------------------------------
def meeting_rooms_1(meetings):
    meetings = sorted(meetings, key=lambda x: x)
    max_rooms = 0
    for i in range(len(meetings)):
        j = i+1
        curr_rooms = 1
        while j < len(meetings):
            meeting_i = meetings[i]
            meeting_j = meetings[j]
            if meeting_i[1] > meeting_j[0]:   # current meeting's end after next meeting's start
                curr_rooms += 1
            j += 1
        if curr_rooms > max_rooms:
            max_rooms = curr_rooms
    return max_rooms

def meeting_rooms_2(meetings):
    starts = sorted([i[0] for i in meetings])
    ends   = sorted([i[1] for i in meetings])
    start_i = end_i = 0
    curr_rooms = max_rooms = 0
    while start_i < len(meetings) and end_i < len(meetings):
        if starts[start_i] < ends[end_i]:
            curr_rooms += 1
            start_i += 1
        else:
            curr_rooms -= 1
            end_i += 1
        if curr_rooms > max_rooms:
            max_rooms = curr_rooms
    return max_rooms

# ---------------------------------------------------------
meetings = [(30, 75), (0, 75), (0, 50), (60, 150)]
result = meeting_rooms_1(meetings)
print(result)
result = meeting_rooms_2(meetings)
print(result)