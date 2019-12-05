import math

class Wire:
    def __init__(self, wire):
        self.intervals = []
        self.lastPoint = (0, 0)
        for command in wire:
            direction = command[0]
            distance = int(command[1:])

            if direction == 'L':
                self.intervals.append(Xinterval(self.lastPoint[0], self.lastPoint[0] - distance, self.lastPoint[1]))
                self.lastPoint = (self.lastPoint[0] - distance, self.lastPoint[1])
            elif direction == 'R':
                self.intervals.append(Xinterval(self.lastPoint[0], self.lastPoint[0] + distance, self.lastPoint[1]))
                self.lastPoint = (self.lastPoint[0] + distance, self.lastPoint[1])
            elif direction == 'U':
                self.intervals.append(Yinterval(self.lastPoint[1], self.lastPoint[1] + distance, self.lastPoint[0]))
                self.lastPoint = (self.lastPoint[0], self.lastPoint[1] + distance)
            elif direction == 'D':
                self.intervals.append(Yinterval(self.lastPoint[1], self.lastPoint[1] - distance, self.lastPoint[0]))
                self.lastPoint = (self.lastPoint[0], self.lastPoint[1] - distance)
    
    def print(self):
        for i in self.intervals:
            i.print()

    def getWire(self):
        return self.intervals
    
    def intersections(self, wire):
        intersections = {}
        wire_a_dist = 0
        
        for wire_a in self.intervals:
            wire_b_dist = 0

            for wire_b in wire.getWire():
                if (wire_a.getType() == 'Y' and wire_b.getType() == 'X') or (wire_a.getType() == 'X' and wire_b.getType() == 'Y'):
                    if wire_a.intersects(wire_b):
                        point = ''
                        extraDistanceX = 0
                        extraDistanceY = 0

                        if wire_a.getType() == 'Y':
                            point = '%d,%d' %(wire_a.getX(), wire_b.getY())
                            extraDistanceY = int(math.fabs(wire_b.getY() - wire_a.getInterval()[0]))
                            extraDistanceX = int(math.fabs(wire_a.getX() - wire_b.getInterval()[0]))
                        else:
                            point = '%d,%d' %(wire_b.getX(), wire_a.getY())
                            extraDistanceY = int(math.fabs(wire_a.getY() - wire_b.getInterval()[0]))
                            extraDistanceX = int(math.fabs(wire_b.getX() - wire_a.getInterval()[0]))

                        total_distance = wire_a_dist + wire_b_dist + extraDistanceX + extraDistanceY

                        if total_distance != 0:    
                            intersections[point] = wire_a_dist + wire_b_dist + extraDistanceX + extraDistanceY

                wire_b_dist += wire_b.distance()

            wire_a_dist += wire_a.distance()
        
        return intersections

    def shortest_distance_intersection(self, wire):
        intersections = self.intersections(wire)

        minDistance = 99999999

        for intersection in intersections:
            minDistance = min(minDistance, intersections[intersection])

        return minDistance


def between(val, tup):
    return tup[0] <= val <= tup[1] or tup[1] <= val <= tup[0]


class Yinterval:
    def __init__(self, yStart, yEnd, x):
        self.x = x
        self.y = (yStart, yEnd)

    def getType(self):
        return 'Y'

    def distance(self):
        return int(math.fabs(self.y[1] - self.y[0]))

    def getX(self):
        return self.x

    def getInterval(self):
        return self.y
    
    def print(self):
        print('x: %d,\t\ty:[%d, %d]' %(self.x, self.y[0], self.y[1]))

    def intersects(self, xInterval):
        y = xInterval.getY()
        x = xInterval.getInterval()

        if between(self.x, x) and between(y, self.y):
            return True
        return False

    
class Xinterval:
    def __init__(self, xStart, xEnd, y):
        self.y = y
        self.x = (xStart, xEnd)

    def getType(self):
        return 'X'

    def distance(self):
        return int(math.fabs(self.x[1] - self.x[0]))

    def getY(self):
        return self.y

    def getInterval(self):
        return self.x

    def print(self):
        print('x:[%d, %d],\ty: %d' %(self.x[0], self.x[1], self.y))

    def intersects(self, yInterval):
        x = yInterval.getX()
        y = yInterval.getInterval()

        between(x, self.x) and between(self.y, y)
        if between(x, self.x) and between(self.y, y):
            return True
        return False

if __name__ == '__main__':
    
    file = open('input3.txt', 'r')
    wires = file.read().split('\n')
    wireInputA = wires[0].split(',')
    wireInputB = wires[1].split(',')
    file.close()

    # test case
    # wireInputA = 'R8,U5,L5,D3'.split(',')
    # wireInputB = 'U7,R6,D4,L4'.split(',')

    wireA = Wire(wireInputA)
    wireB = Wire(wireInputB)

    print(wireA.shortest_distance_intersection(wireB))