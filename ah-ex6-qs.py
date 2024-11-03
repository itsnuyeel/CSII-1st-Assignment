# EX 6: QS - Quick Sort

"""""
Given: A positive integer n≤10^5 and an array A[1..n] of integers from -10^5 to 10^5.

Return: A sorted array A[1..n].
"""""

# I solve the problem using the QuickSort algorithm: 1. I choose an element as pivot; 
# 2. I partition the array so that the minor elements of the pivot are on the left and the major elements on the right
# 3. I recursively order the two parts

def partition(array, start_index, end_index):
    
    # This function: - Selects the last element as pivot; - Reorganise the array by placing the minor elements of the pivot to the left;
    # Returns the final position of the pivot
    
    pivot = array[end_index]
    
    # smallest element index
    i = start_index - 1  
    
    for j in range(start_index, end_index):
        
        # If the current element is less than or equal to the pivot
        if array[j] <= pivot:
            
            # I increase the index of the smallest element
            i += 1  
            array[i], array[j] = array[j], array[i]
    
    # I place the pivot in its final position
    array[i + 1], array[end_index] = array[end_index], array[i + 1]
    return i + 1

def quicksort(array, start_index, end_index):

    # This function: - Implements the recursive algorithm QuickSort; -  It stops when low ≥ high (base case)
    # - It calls partition and then orders the two halves recursively
    
    # Basic condition: if start_index < end_index, it means that there is more than one element to be sorted
    if start_index < end_index:
        # I find the partition index
        pi = partition(arr, start_index, end_index)
        
        # I order the left and right parts recursively
        quicksort(array, start_index, pi - 1)
        quicksort(array, pi + 1, end_index)


# Statement for test code
if __name__ == "__main__":
    # I read input from the file
    with open("./datasets-pt2/ex6/rosalind_qs.txt", "r") as file:
        # I read n from the first line
        n = int(file.readline().strip())
        
        # I read the array from the second line
        arr = list(map(int, file.readline().strip().split()))
        
        # I sort the array
        quicksort(arr, 0, len(arr)-1)
        
        # I print the result
        print(" ".join(map(str, arr)))