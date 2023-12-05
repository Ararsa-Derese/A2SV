class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        elif start < destination:
            a = sum(distance[start:destination])
        else:
            a = sum(distance[destination:start])

        full = sum(distance)

        if full - a > a:
            return a
        return full - a

