"""Insertion sort: Takes a single element and places it in the correct location.
   Complexity:
   Time: Worst case: O(n^2), Best case: O(n)
   Space: Worst case: O(n^2), O(1)"""

def insertion_sort(list):
    i = 1
    while i < len(list):
        j = i
        while j > 0 and list[j-1] >list[j]:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j = j - 1
        i = i + 1
    return list


unorderedOddList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8]
unorderedEvenList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8, 1]

print("Sorted odd list: " + str(insertion_sort(unorderedOddList)))
print("Sorted even list: " + str(insertion_sort(unorderedEvenList)))