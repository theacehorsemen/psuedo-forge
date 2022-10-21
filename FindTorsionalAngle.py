#Given 4 points A,B,C,D find the angle between the planes formed by points A,B,C and points B,C,D
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        ax = self.x - no.x
        ay = self.y - no.y
        az = self.z - no.z
        return(Points(ax,ay,az))

    def dot(self, no):
        ax = self.x * no.x
        ay = self.y * no.y
        az = self.z * no.z
        return(ax+ay+az)

    def cross(self, no):
        ax = (self.y * no.z) - (self.z*no.y)
        ay = (self.z * no.x) - (self.x*no.z)
        az = (self.x * no.y) - (self.y*no.x)
        return(Points(ax,ay,az))
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
