import math

"""Binary search algorithm. Requires the list to be sorted. Time complexity: O(log n), Space complexity: O(1)
   Idea: start at the middle of the sorted list/array and check if the target value is smaller or greater than the current value.
   Repeat with the correct half of the list/array until the value is found or until the last value in the list/array is found.
   Because the data is cut in half in every step it has a worst case time complexity of O(log n)."""

def binarySearch(list, target):
    #left index of the list
    L = 0
    #right index of the list
    R = len(list)-1

    while(L <= R):
        #compute the middle index
        M = math.floor((L+R)/2)
        #check in what half of the list the value must be
        if(list[M] < target):
            # the new left index of the list is the middle index + 1
            L = M + 1
        elif(list[M] > target):
            # the new right index of the list is the middle index - 1
            R = M - 1
        else:
            # return the middle index
            return M
    # value is not in the list
    return -1


testList = range(0,10)
print("binarySearch: " + str(binarySearch(testList, 11)))
print("binarySearch: " + str(binarySearch(testList, 5)))