"""
 Stores and Houses
 You are given 2 arrays representing integer locations of 
 stores and houses (each location in this problem is one-
 -dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote 
the location of the store closest to the i-th house. If many 
stores are equidistant from a particular house, choose the 
store with the smallest numerical location. Note that there 
may be multiple stores and houses at the same location.
Example:
Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation: 
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
"""
class Solution:
    def find_closest_store(self,houses,stores):
        result = []
        stores.sort()
        for house in houses:
            # result.append(self.binary_search(house,stores))
            min_distance = closest_store = None
            for store in stores:
                if min_distance == None:
                    min_distance = abs(store-house)
                elif min_distance > abs(store-house):
                    min_distance = abs(store-house)
                    closest_store = store
            result.append(closest_store)
        return result
  
   
test = Solution()
houses = [5, 10, 17]
stores = [1, 5, 20, 11, 16]
print(test.find_closest_store(houses,stores))