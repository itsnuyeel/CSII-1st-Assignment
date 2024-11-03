# EX 9: PS - Partial Sort

"""""
Given: A positive integer n≤10^5 and an array A[1..n] of integers from -10^5 to 10^5, a positive integer k≤1000.

Return: The k smallest elements of a sorted array A.
"""""

# I need to find the k smallest elements of an array and return them in ascending order, so:
# I build a data structure that always keeps the minimum element at the top: I start from the entire array and extract the k smallest elements
# I sort the k extracted elements to present them in ascending order 

# This function helps maintain the property of the minimum heap in a sub-tree with root in node i
# Each knot is smaller than its children:
# "smallest" is initially set as the current index i, while "left" and "right" represent the indices of the left and right children of the current 
# node respectively
def tree(array, n, i):
    smallest = i
    left = 2 * i + 1  # It calculates the index of the left child
    right = 2 * i + 2  # It calculates the index of the right child
    
    # This function finds the smallest child and swaps it with the current node if necessary, then continues the process recursively

    # I check whether the left child (left) is smaller than the current element (array[smallest])
    if left < n and array[left] < array[smallest]:
        
        # If yes, I update smallest with index left
        smallest = left
    
    # I check whether the right child is smaller than the current node
    if right < n and array[right] < array[smallest]:
        smallest = right
    
    # Now smallest contains the index of the smallest value between the current node and its children.

    # If smallest has been updated, I exchange the current node for the smallest element identified
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        
        # I call the tree function recursively on the sub-tree to check the heap structure
        tree(array, n, smallest)

# This function constructs a minimum heap from the array "array"
# It starts with the last nodes with children and apply the tree function to each one
def build_heap(array):
    n = len(array)
    
    # I start from the last node that has children (n // 2 - 1) and work upwards by calling "tree" on each node
    for i in range(n // 2 - 1, -1, -1):
        tree(array, n, i)

# This function extracts the k minimum elements one by one, adding the root (the current minimum) to min_elements
# After each extraction, it replaces the root with the last element of the heap and reduces the size of the heap, reorganizing with the tree function.
# I make sure that the minimum value is at the top
def smallest_elements(array, k):
    
    build_heap(array)
    
    # list in which I will save the k smaller elements extracted from the heap
    min_elements = []
    
    n = len(array)
    
    # For k iterations, I add the smallest element (the heap root) to min_elements
    for _ in range(k):
        # I add the root, which is the minimum
        min_elements.append(array[0])
        
        # I replace the root with the last element of the heap, reducing the effective size of the heap by 1
        array[0] = array[n - 1]
        n -= 1
        
        # I call the tree function on the root to reorganize the heap
        tree(array, n, 0)
    
    # To provide the result in ascending order:
    return sorted(min_elements)


# Statement for test code
if __name__ == "__main__":
    
    # I open the file and skip the first line, then read the array A and the number k from the second and third lines
    with open("./datasets-pt2/ex9/rosalind_ps.txt", "r") as file:
        file.readline()  # Ignora la prima riga
        A = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
    
    # I call the smallest_elements function to obtain the k smallest elements
    result = smallest_elements(A, k)
    
    # I print result as a string of numbers separated by spaces
    print(" ".join(map(str, result)))