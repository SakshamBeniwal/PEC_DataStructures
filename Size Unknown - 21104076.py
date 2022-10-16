#Saksham Beniwal
#21104076
#EE


#-----Start-----#

#Normal Binary Search iterative method
def BinarySearch(array , left, right, element):
 
    if right >= left:
        mid = left + (right - left) // 2
 
        if array[mid] == element:
            return mid
 
        if array[mid] > element:
            return BinarySearch(array, left, mid - 1, element)
 
        return BinarySearch(array, mid + 1, right, element)
 
    return -1

#To find 'high' of Binary Search and the use Binary Search function to find element
def FindPos(a, key):
 
    low = 0
    high = 1
    val = array[0]
 
    while val < key:
        low = high            
        high = high * 2          
        val = array[high]       
 
    return BinarySearch(a, low, high, key)
 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #random sorted array for demonstration
element = 4

answer = FindPos(array, element)

if answer == -1:
    print ("Element not found")

else:
    print("Element found at index", answer)

#-----End-----#