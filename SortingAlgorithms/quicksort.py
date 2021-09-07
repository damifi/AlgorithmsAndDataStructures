"""
   Complexity:
   Time: Worst case O(n^2) (rare), Best case O(n log n)
   Space: Worst case O(n): """

TODO video
def quicksort(list):
    lo = 0
    hi = len(list)-1

    if(lo >= 0 and hi >= 0):
        if lo < hi:
            p = partition(list, lo, hi)
            quicksort(list[:(p-1)])
            quicksort(list[(p+1):])

def partition(list,lo, hi):
    pivot = list[hi]
    i = lo - 1
    for j in range(0, hi):
        if list[j] <= pivot:
            i = i + 1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    return i



unorderedOddList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8]
unorderedEvenList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8, 1]

print("Sorted odd list: " + str(quicksort(unorderedOddList)))
print("Sorted even list: " +str(quicksort(unorderedEvenList)))