

"""Split (unsorted) list into sublists in the middle
   Returns two sublists, the left half and the right half"""
def splitList(list):
    #find the midpoint of the lists using the floor(//) operator
    mid = len(list)//2
    #left half of the list
    left = list[:mid]
    #right half of the left
    right = list[mid:]
    return left, right

"""Merges two list and sorts them.
   Returns a new merged list."""
def merge(left, right):
   #resulting list
   resultList = []
   #counter for the left and right list
   i = 0
   j = 0
   #while there are elements in the left and right list
   while(i < len(left) and j < len(right)):
      #if the element in the left list is smaller than the one in the right 
      if(left[i] < right[j]):
         # add the left element to the result list
         resultList.append(left[i])
         i = i + 1
      else:
         # else add the element of the right list to the result element
         resultList.append(right[j])
         j = j + 1

   #if the original list is odd there is one list (either left or right) that has one more element than the other
   while(i < len(left)):
      resultList.append(left[i])
      i+=1
   
   while(j < len(right)):
      resultList.append(right[j])
      j+=1
   
   return resultList

"""Sorts a list in ascending order using the mergesort algorithm
   Returns a new sorted list
   Steps:
   Divide: Split the list into two sublists in the middle
   Conquer: Sort the sublists recursivly
   Finally, merge the created sublists to a list """

def merge_sort(list):
   #as this is a recursive algorithms we need a base case, i.e. when the list has one or no element.
   if len(list) <= 1:
      return list
   leftHalf, rightHalf = splitList(list)
   left = merge_sort(leftHalf)
   right = merge_sort(rightHalf)
   return merge(left, right)

unorderedOddList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8]
unorderedEvenList = [3, 5, 9, 8 , 6, 5, 3 , 1, 1,2, 8, 1]

print("Sorted odd list: " + str(merge_sort(unorderedOddList)))
print("Sorted even list: " +str(merge_sort(unorderedEvenList)))