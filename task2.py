class Road:
    weight1mroad = 25
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight (self, depth):
        return depth * self.weight1mroad * self._width * self._length

road_to_work = Road(50, 20)
print(road_to_work.weight(5))
