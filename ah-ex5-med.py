# EX 5: MED - Median

"""""
Given: A positive integer n≤10^5 and an array A[1..n] of integers from -10^5 to 10^5, a positive number k≤n.

Return: The k-th smallest element of A.
"""""

# I need to find the k-th smallest element in an array, and to do this I use the QuickSelect algorithm, so that I do not have to sort the entire array
# 1. I choose a pivot 2. I partition the array around the pivot; 3. If the pivot index is k, we have found our element;
# 4. If k is less than the index of the pivot, I look in the left side; 5. If k is greater than the pivot index, I look in the right side
# Quick_select only recurs on the necessary half of the array

def partition(array, start_index, end_index):
    
    # The parameters include: 1. "array" contains the numbers to be reorganised; 2. "start_index" is the start index of the portion of the array we are working on
    # (in the first call is typically 0 (the beginning of the array)); ex: if start_index = 2, we are starting with the third element
    # 3. "end_index" is the end index of the portion of the array we are working on (In the first call it is len(arr)-1 (the last index of the array))
    
    # This function partitions the array using the last element as a pivot and it returns the final index of the pivot.
   
    pivot = array[end_index]
    
    # smallest element index
    i = start_index - 1  
    
    # It scrolls the array from the first to the penultimate element (not including the pivot)
    for j in range(start_index, end_index):
        
        # If the current element is less than or equal to the pivot:
        if array[j] <= pivot:
            
            # --> It increases the index of the smallest element
            i += 1  
            array[i], array[j] = array[j], array[i]
    
    # It puts the pivot in its final position, exchanging it with the first major element of the pivot
    array[i + 1], array[end_index] = array[end_index], array[i + 1]
    return i + 1

def quick_select(array, start_index, end_index, k):

    # This function finds the k-th smallest element in the array "array[start_index...end_index]".
    # k is the position of the element we are looking for (1-based) --> If k=1, we search for the smallest element; If k=n, we search for the largest element
    # ex: if k = 3, we are looking for the third smallest element
    
    # I convert k to 0-based for array indexing
    k = k - 1

    while start_index <= end_index:
        # I partition the array and get the pivot index
        pivot_index = partition(array, start_index, end_index)
            
        # If the pivot is the element we are looking for:
        if pivot_index == k:
            return array[pivot_index]
        
        # If k is smaller, look in the left side
        elif pivot_index > k:
            end_index = pivot_index - 1
        
        # If k is larger, look in the right side
        else:
            start_index = pivot_index + 1
                


# Statement for test code
if __name__ == "__main__":
    # I read the input from the file
    with open("./datasets-pt2/ex5/rosalind_med.txt", "r") as file:
        
        # I read n from the first line
        n = int(file.readline().strip())
        
        # I read the array from the second line
        arr = list(map(int, file.readline().strip().split()))
        
        # I read k from the third line
        k = int(file.readline().strip())

        result = quick_select(arr, 0, len(arr)-1, k)
        
        print(result)