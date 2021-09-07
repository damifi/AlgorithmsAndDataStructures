"""Selection sort: pick an element from the list and search the correct position for it and insert it
   Complexity:
   Time: Worst case: O(n^2), Best case: O(n^2)
   Space: Worst case: O(n), Best case: O(1)"""
def selection_sort(list):
    #go through the list
    for i in range(0, len(list)):
        #assume the min element in the list is at index i
        jMin = i
        #iterate through the rest of the list
        for j in range(i+1, len(list)):
            #if another element in the list is smaller than the current min element
            if(list[j] < list[jMin]):
                #the new min element is at index j
                jMin = j
        #if the min element is not at index i, swap i with the min element
        if jMin != i:
            temp = list[i]
            list[i] = list[jMin]
            list[jMin] = temp
    return list



unorderedOddList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8]
unorderedEvenList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8, 1]

print("Sorted odd list: " + str(selection_sort(unorderedOddList)))
print("Sorted even list: " +str(selection_sort(unorderedEvenList)))