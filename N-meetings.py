class Meeting:
    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position


def max_meetings(start, end):
    n = len(start)

    # Step 1: Create meeting objects
    meetings = [Meeting(start[i], end[i], i + 1) for i in range(n)]

    # Step 2: Sort by end time, then start time
    meetings.sort(key=lambda x: (x.end, x.start))

    # Step 3: Select meetings greedily
    result = [meetings[0].position]
    count = 1
    last_time = meetings[0].end

    for i in range(1, n):
        if meetings[i].start > last_time:
            result.append(meetings[i].position)
            count += 1
            last_time = meetings[i].end

    return count, result


# 🔹 Example Usage
start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

count, meetings_selected = max_meetings(start, end)

print("Maximum meetings:", count)
print("Meetings selected:", meetings_selected)