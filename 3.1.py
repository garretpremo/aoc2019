import math

class Wire:
    def __init__(self, wire):
        self.wire = { '0,0' }
        self.lastPoint = (0, 0)

        for command in wire:
            direction = command[0]
            distance = int(command[1:])

            x = 0
            y = 0

            if direction == 'L':
                x = 1
            elif direction == 'R':
                x = -1
            elif direction == 'U':
                y = 1
            elif direction == 'D':
                y = -1

            for i in range(distance):
                self.lastPoint = (self.lastPoint[0] + x, self.lastPoint[1] + y)
                self.addLastPoint()
    
    def addLastPoint(self):
        point = '%d,%d' %(self.lastPoint[0], self.lastPoint[1])
        self.wire.add(point)

    def print(self):
        print(self.wire)

    def getWire(self):
        return self.wire
    
    def intersect(self, wire):
        return self.wire.intersection(wire.getWire())



if __name__ == '__main__':

    file = open('input3.txt', 'r')
    wires = file.read().split('\n')
    wireInputA = wires[0].split(',')
    wireInputB = wires[1].split(',')

    # test cases
    # wireInputA = 'R8,U5,L5,D3'.split(',')
    # wireInputA = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
    # wireInputA = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')

    # wireInputB = 'U7,R6,D4,L4'.split(',')
    # wireInputB = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
    # wireInputB = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')

    wireA = Wire(wireInputA)
    wireB = Wire(wireInputB)

    minDist = 99999999999
    intersections = wireA.intersect(wireB)
    intersections.remove('0,0')
    print(intersections)

    for point in intersections:
        coords = point.split(',')

        x = int(math.fabs(int(coords[0])))
        y = int(math.fabs(int(coords[1])))

        minDist = min(minDist, (x + y))


    print(minDist)

    file.close()


# rip grid :(
class Grid:

    def __init__(self):
        self.grid = [ ['O'] ]
        self.intersections = []
        self.width = 1
        self.height = 1
        self.base = ( 0, 0 )

    def print(self):
        for col in self.grid:
            row = ''
            for cell in col:
                row += cell
            print(row)

    def minDistFromBase(self):
        print(self.width, self.height, self.base)
        print(self.intersections)
        minDist = max(self.width, self.height)
        for point in self.intersections:
            minDist = min(minDist, self.distFromBase(point))

        return minDist
    
    def distFromBase(self, point):
        dist = int(math.fabs(point[0] - self.base[0]) + math.fabs(point[1] - self.base[1]))
        return dist

    def addColumns(self, columns, right):
        self.width += columns

        for row in self.grid:
            for i in range(columns):
                if right:
                    row.append('.')
                else:
                    row.insert(0, '.')

        if not right:
            self.adjustBase(columns, 0)                  

    def addRows(self, rows, bottom):
        self.height += rows

        for i in range(rows):
            baseRow = ['.'] * len(self.grid[0])
            
            if bottom:
                self.grid.append(baseRow)
            else:
                self.grid.insert(0, baseRow)

        if not bottom:
            self.adjustBase(0, rows)

    def adjustBase(self, x, y):
        self.base = (self.base[0] + x, self.base[1] + y)
        
        for intersection in self.intersections:
            intersection = (intersection[0] + x, intersection[1] + y)

    def recordWire(self, instructions, label):
        base = (self.base[0], self.base[1])
        for instruction in instructions:
            distance = int(instruction[1:])
            if instruction[0] == 'R':
                base = self.recordWireRight(base, distance, label)
            elif instruction[0] == 'L':
                base = self.recordWireLeft(base, distance, label)
            elif instruction[0] == 'D':
                base = self.recordWireDown(base, distance, label)
            elif instruction[0] == 'U':
                base = self.recordWireUp(base, distance, label)

    def recordWireRight(self, base, distance, label):
        overflow = (base[0] + distance + 1) - self.width 

        if overflow > 0:
            self.addColumns(overflow, True)

        for i in range(distance):
            if not self.checkIntersection(base[0] + i + 1, base[1], label):
                self.grid[ base[1] ][ base[0] + i + 1] = label
            
        return (base[0] + distance, base[1])

    def recordWireLeft(self, base, distance, label):
        overflow = base[0] - distance

        if overflow < 0:
            self.addColumns(int(math.fabs(overflow)), False)
            base = (base[0] - overflow, base[1])

        for i in range(distance):
            if not self.checkIntersection(base[0] - i - 1, base[1], label):
                self.grid[ base[1] ][ base[0] - i - 1] = label
            
        return (base[0] - distance, base[1])

    def recordWireDown(self, base, distance, label):
        overflow = (base[1] + distance + 1) - self.height

        if overflow > 0:
            self.addRows(overflow, True)

        for i in range(distance):
            if not self.checkIntersection(base[0], base[1] + i + 1, label):
                self.grid[ base[1] + i + 1 ][ base[0] ] = label

        return (base[0], base[1] + distance)

    def recordWireUp(self, base, distance, label):
        overflow = (base[1] - distance)

        if overflow < 0:
            self.addRows(int(math.fabs(overflow)), False)
            base = (base[0], base[1] - overflow)

        for i in range(distance):
            if not self.checkIntersection(base[0], base[1] - i - 1, label):
                self.grid[ base[1] - i - 1 ][ base[0] ] = label
            
        return (base[0], base[1] - distance)
                    
    def checkIntersection(self, x, y, label):
        cell = self.grid[y][x]
        
        if cell != '.' and cell != 'X' and cell != label:
            self.intersections.append( (x, y) )
            self.grid[y][x] = 'X'
            return True

        return False