# EX 7: HEA - Building a Heap

"""""
Given: A positive integer n≤10^5 and array A[1..n] of integers from -10^5 to 10^5.

Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].
"""""

# A binary max heap is a data structure in which each parent node has a value greater than or equal to those of its children
# Every level of the tree is completely filled, except perhaps the last, which is filled from left to right

# Given an array of numbers, I must rearrange it so that it satisfies the binary max heap property, that is, 
# I must position the elements so that each node (that has its specific element) is greater than its children
# To do this, I start from the last parent node and work my way upwards along the array

# I take a node, compare its value with that of the children and exchange the node with the greatest child (if necessary)

# The function takes 3 arguments: the array A, the array size n, and the index i of the current node
def tree(A, n, i):
    
    # I find the father node, left son and right son
    
    # I assume that i is the largest node
    largest = i             
    
    # I calculate the index of the left child
    left = 2 * i + 1        
    
    # I calculate the index of the right child
    right = 2 * i + 2       

    # If the left child exists and its value is greater than A[largest]: 
    if left < n and A[left] > A[largest]:
        
        # I update largest with the index of the left child
        largest = left     

    # If the right child exists and its value is greater than A[largest]:
    if right < n and A[right] > A[largest]:

        # I update largest with the index of the right child
        largest = right     

    # If the current node is not the largest:
    if largest != i:
        
        # I exchange A[i] for A[largest]
        A[i], A[largest] = A[largest], A[i]  
        
        # I call the function recursively to restore the binary max heap property in the resulting subtree
        tree(A, n, largest)  

# This function constructs the binary max heap from the array A
def max_heap(A):
    
    # I calculate the length of the array
    n = len(A)
    
    # I start from the first node with children: n // 2 - 1
    for i in range(n // 2 - 1, -1, -1):
        
        # And I apply the tree function on each node up to the root (i = 0)
        tree(A, n, i)

# Statement for test code
if __name__ == "__main__":
    
    # I open the input file 
    with open("./datasets-pt2/ex7/rosalind_hea.txt", "r") as file:
        
        # I discard the first line of the file, as it is not needed n
        file.readline()

        # I read the array A and I convert the second line into a list of integers 
        A = list(map(int, file.readline().strip().split()))

    # I call the function
    max_heap(A)

    # I print the result
    print(" ".join(map(str, A)))