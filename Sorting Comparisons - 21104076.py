#Saksham Beniwal
#EE
#21104076


#-----Start-----#



# In-place implementation of Bubble Sort
# Since Bubble Sort is an in-place algorithms, it can only be implemented using in-place

bubble_swap = 0
bubble_comparison = 0

def BubbleSort(array):
 
  # Looping through each positions of array  
  for i in range(len(array)):

    # Looping to compare array elements
    for j in range(0, len(array) - i - 1):

      global bubble_comparison
      bubble_comparison += 1

      # Compare two adjacent elements
      if array[j] > array[j + 1]:

        # Swap adjacent elements if left greater than right
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        global bubble_swap
        bubble_swap += 1

    # If no swap happens for a particular iteration, then array is sorted
    # No need to proceed further for comparison
    if bubble_swap == 0:

      break


data = [7, 2, -1, 9, 0, -3, 4, 6, -8, 8, 5, 3] # Placeholder array for demo

print(f"Original array for Bubble Sort: {data}")

BubbleSort(data)

print(f"Sorted array in ascending order after Bubble Sort: {data}")
print(f"Number of swaps in Bubble Sort: {bubble_swap}")
print(f"Number of comparisons in Bubble Sort: {bubble_comparison}")
# Time complexity of Bubble Sort is O(n ** 2) for worst and average case
# Worst case happens for reverse sorted
# So bubble_comparison = number of comparisons (according to code) for worst case = [n * (n - 1)] / 2 = O(n ** 2)
# The above line always comes out true when code is run
# Time complexity of Bubble Sort is O(n) for best case
# Best case happens for already sorted
# So bubble_comparison = number of comparisons (according to code) for best case = n - 1 = O(n)
# The above line always comes out true when code is run
# In best case, the loop will break after first iteration due to swap = 0
# n = size of array



print() # Print an empty line



# In-place implementation of Selection Sort
# Since Selection Sort is an in-place algorithms, it can only be implemented using in-place

selection_swap = 0
selection_comparison = 0

def SelectionSort(array):
   
    # Looping through each positions of array
    for step in range(len(array)):
        min_index = step

        # Looping through positions after current location to find its minimum element
        for i in range(step + 1, len(array)):

            global selection_comparison 
            selection_comparison += 1
         
            # Selecting minimum element
            if array[i] < array[min_index]:
                min_index = i

        # Place minimum element at its correct position 
        (array[step], array[min_index]) = (array[min_index], array[step])
        
        if step != min_index:
        
          # Swap only happens if minimum element not at its correct position
          global selection_swap
          selection_swap += 1


data = [7, 2, -1, 9, 0, -3, 4, 6, -8, 8, 5, 3] # Placeholder array for demo

print(f"Original array for Selection Sort: {data}")

SelectionSort(data)

print(f"Sorted array in ascending order after selection sort: {data}")
print(f"Number of swaps in selection sort: {selection_swap}")
print(f"Number of comparison in selection sort: {selection_comparison}")
# Time complexity of Selection Sort is O(n ** 2) for all cases
# So selection_comparison = number of comparisons (according to code) = [n * (n - 1)] / 2 = O(n ** 2)
# The above line always comes out true when code is run
# n = size of array



print() # Print an empty line



# Comparing number of swaps of both sorts
if bubble_swap < selection_swap:

    print("Bubble Sort require less number of Swaps")

if selection_swap < bubble_swap:

    print("Selection Sort require less number of Swaps")

if bubble_swap == selection_swap:

    print("Both Sort require same number of Swaps")




print() # Print an empty line



# Comparing number of comparisons of both sorts
if bubble_comparison < selection_comparison:

    print("Bubble Sort require less number of Comparisons")

if selection_comparison < bubble_comparison:

    print("Selection Sort require less number of Comparisons")

if bubble_comparison == selection_comparison:

    print("Both Sort require same number of Comparison")



print() # Print an empty line



#-----End-----#
