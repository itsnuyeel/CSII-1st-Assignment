# EX 8: HS - Heap Sort

"""""
Given: A positive integer n≤10^5 and an array A[1..n] of integers from -10^5 to 10^5.

Return: A sorted array A.
"""""

# Heap Sort is a sorting algorithm based on the construction of a max heap and its gradual reduction to an ordered array.
# The procedure uses the fact that the maximum value in a max heap is always at the root of the tree (first element of the array).

# 1. I transform the array into a max heap (a binary tree in which each parent node is greater than or equal to its children). 
# In a max heap, the maximum value is at the root.
# 2. I move the maximum value to the bottom of the array and reduce the effective heap size by 1
# 3. After the swap, I return the new element to its correct place on top (max heap structure)

def tree(A, n, i):
    
    # I assume that the current node is the largest
    largest = i  
    
    # Index of the left child
    left = 2 * i + 1  
    
    # Index of the right child
    right = 2 * i + 2  

    # If the left child exists and is greater than the parent:
    if left < n and A[left] > A[largest]:
        largest = left

    # If the right child exists and is greater than the current node (parent or left child):
    if right < n and A[right] > A[largest]:
        largest = right

    # If the largest node is not the current node (i), I swap
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        
        # I recursively call tree on the new subtree
        tree(A, n, largest)

# This function builds the max heap
def max_heap(A):
    n = len(A)
    
    # I start from the last nodes and apply the tree function all the way to the root
    for i in range(n // 2 - 1, -1, -1):
        tree(A, n, i)

# I sort the array A
def sort(A):
    n = len(A)

    # I build the max heap
    for i in range(n // 2 - 1, -1, -1):
        tree(A, n, i)

    # I extract the elements one at a time
    for i in range(n-1, 0, -1):

        # I exchange the root (maximum) for the last unsorted element
        A[0], A[i] = A[i], A[0]
        
        # I restore the max heap on the reduced part of the array
        tree(A, i, 0)

    return A

# Statement for test code
if __name__ == "__main__":
    with open("./datasets-pt2/ex8/rosalind_hs.txt", "r") as file:
        
        # I read the array to be sorted (ignoring the first line)
        file.readline()  
        A = list(map(int, file.readline().strip().split()))

    # I call the function on array A
    sorted_A = sort(A)

    # I print the sorted array separated by spaces
    print(" ".join(map(str, sorted_A)))











