import sys

"""
   Complexity:
   Time: Worst case O(n^2) (rare), Best case O(n log n)
   Space: Worst case O(n): """

#Recursive function
def quicksort(list):
    """implements the quicksort algorithm for lists"""
    #base case: the length of the values is <= 1
    if len(list) <= 1:
        return list

    #chose a pivot element and break the list into two parts: the left list contains all elements smaller 
    #than the pivot element and the right list contains all elements greater than the pivot element#

    #TODO:
    #1 choose pivot
    #2 break the list into 2 lists
    #3 recursively call the functions
    
    #list for elements smaller than the pivot
    smallerThanPivot = []
    #list for elements greater than the pivot
    greaterThanPivot = []

    #choose a pivot element, for this case take the first element
    pivot = list[0]

    #loop through the list of numbers and fill the lists with smaller or greater values than the pivot
    for item in list[1:]:
        if item <= pivot:
            smallerThanPivot.append(item)
        else:
            greaterThanPivot.append(item)
    return quicksort(smallerThanPivot) + [pivot] + quicksort(greaterThanPivot)


unorderedOddList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8]
unorderedEvenList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8, 1]
wrongTypeList = ["oi", "mate", "where"]
#print("Sorted odd list: " + str(quicksort(wrongTypeList)))

print("Sorted odd list: " + str(quicksort(unorderedOddList)))
print("Sorted even list: " +str(quicksort(unorderedEvenList)))