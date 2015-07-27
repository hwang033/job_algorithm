#!/usr/bin/python

#Definition for a point
class Point:
    def __init__(self, a=0, b=0): 
        self.x = a
        self.y = b

#class Solution:
#    #@param points, a list of points
#    #@return an integer
#    def maxPoints(self, points):
#        points_len = len(points)
#        lr = {}  
#       
#        # find all the linear functions
#        for point1 in points: 
#           for point2 in points:
#              # y = kx + b 
#              try:
#                  k = (point1.x - point2.x)*1.0/(point1.y - point2.y)
#              except ZeroDivisionError:
#                  k = 0
#              b = point1.y - k*point1.x
#              lr["%f, %f" %(k, b)] = 0
#
#        max = 0
#
#        #count how many points in the line 
#        for point in points:
#           for key in lr.keys():
#               k_b = key.split(",")
#               k = float(k_b[0]) 
#               b = float(k_b[1])
#               if point.y == point.x * k + b :
#                   num = lr[key] 
#                   num += 1
#                   lr[key] = num
#                   if num > max:
#                       max = num
#        return max

class Solution:
    #@param points, a list of points
    #@return an integer
    def maxPoints(self, points):
    # find max points 
        if len(points) == 0 or len(points) == 1:
            return len(points)
        
        max = 0
        for i in range(0, len(points)):
            num_point = {}
            duplicate = 1 #duplicate point number
            for j in range(i+1, len(points)):
               try:
                   k = (points[i].y - points[j].y)*1.0/(points[i].x - points[j].x)
               except ZeroDivisionError:
                   # if i and j are the same point 
                   # every key in mun_point should +1
                   # and compare to max
                   if points[i].y - points[j].y == 0:
                       duplicate += 1
                       if duplicate > max:
                           max = duplicate
                       for key in num_point.keys():
                           num_point[key] = num_point.get(key) + 1 
                           if num_point[key] > max:
                                max = num_point[key]
                       continue 
                   else: 
                       k = 'infinity'
               #print k
               num_point.setdefault(k, duplicate)
               num_point[k] = num_point.get(k) + 1 
               if num_point[k] > max:
                max = num_point[k]
        return max    
               


if __name__ == "__main__":
    #x_y_l = [1,2,3,4,5,6,7,8,9, 10]
    #x_y_l = [1,1,1,1,2,3]
    x_y_l = [0,0,0,0]
    points = []
    for i in xrange(0, len(x_y_l), 2): 
        points.append(Point(x_y_l[i], x_y_l[i+1]))
    s = Solution()    
    print s.maxPoints(points)



