'''K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] 
represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is 
the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is 
guaranteed to be unique (except for the order that it is in).
Example:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the 
answer is just [[-2,2]].'''

class Solution:
    def kClosest(self, points, k: int):
        distance_dict = {}
        for point in points:
            distance_dict[point[0],point[1]] = point[0]**2 + point[1]**2
        result = sorted(distance_dict, key=distance_dict.get)[:k]
        return [list(i) for i in result]


test = Solution()
points = [[1,3],[-2,2]]
k = 1
print(test.kClosest(points , k))