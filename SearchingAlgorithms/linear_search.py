#Algorithms and Data structures
#linear search: go through the array/list one by one and check if the current value is the one we are looking for. Time: O(n) = n, Space: O(n) = 1
"""if the value is in the list, return the index, else return -1"""
def linearSearch(list, target):
    for index in range(0, len(list)):
        if(list[index] == target):
            return index
    return -1

testList = range(0,10)
print("LinearSearch: " + str(linearSearch(testList, 7)))