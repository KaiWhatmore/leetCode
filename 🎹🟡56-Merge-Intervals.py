def merge(intervals):

    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]

    endTime = 0
    for start, end in intervals[1:]:
        previousEnd = output[-1][1]
        if start <= output[-1][1]:
            output[-1][1] = max(end, previousEnd)
        else:
            output.append([start, end])

    return output
