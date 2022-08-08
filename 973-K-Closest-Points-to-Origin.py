def kClosest(points, k):
    distances = []
    res = []
    checker = collections.defaultdict(list)

    for point in points:
        x, y = point
        distance = x * x + y * y
        checker[distance].append(point)
        distances.append(distance)

    heapq.heapify(distances)

    while len(res) < k:
        res.extend(checker[distances[0]])
        heapq.heappop(distances)

    return res
