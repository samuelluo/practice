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
        curr_rooms = 0
        while j < len(meetings):
            meeting_i = meetings[i]
            meeting_j = meetings[j]
            if meeting_i[1] > meeting_j[0]:   # current meeting's end after next meeting's start
                print([meeting_i, meeting_j])
                curr_rooms += 1
            j += 1
        if curr_rooms > max_rooms:
            max_rooms = curr_rooms
    return max_rooms

# ---------------------------------------------------------
meetings = [(30, 75), (0, 75), (0, 50), (60, 150)]
result = meeting_rooms_1(meetings)
print(result)