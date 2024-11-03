# EX 3: PAR - Way Partition

"""""
Given: A positive integer n≤10^5 and an array A[1..n] of integers from -10^5 to 10^5.

Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 1≤i≤q-1, B[q]=A[1], 
and B[i]>A[1] for all q+1≤i≤n.
"""""

# I'll use the partition procedure to solve this problem
# The partition procedure takes an array element, called a pivot (in this case, the first element A[0]), and rearranges the array so that:
# - Elements less than or equal to the pivot are to its left
# - The major elements of the pivot are located to its right

# The result will then be a new version of the array where all elements less than or equal to the pivot appear before the pivot itself, 
# followed by the major elements

def partition_array(A):
    
    # I define the pivot as the first element of the array
    pivot = A[0]
    
    # I create two empty lists to divide the elements according to the pivot:
    
    # it will contain elements <= pivot
    left = []  
    
    # it will contain elements > pivot
    right = [] 
    
    # Using the for loop, I run through all the elements of A starting from the second (A[1:]), since the first element is the pivot itself
    for x in A[1:]:

        # In each iteration, I compare element x with the pivot:
        # If x is less than or equal to the pivot, it is added to left
        if x <= pivot:
            left.append(x)
        else:
            # If x is greater than the pivot, it is added to right
            right.append(x)

    # I construct and return the array B, which follows the required partition:
    # - First come all elements less than or equal to the pivot (left)
    # - This is followed by the pivot itself, entered as a list [pivot]
    # - Finally, come all the major elements of the pivot (right)
    return left + [pivot] + right

# Statement for test code
if __name__ == "__main__":
    with open("./datasets-pt2/ex3/rosalind_par.txt", "r") as file:
        
        # I read the value n (number of elements in array A), although I do not use it directly in the code
        # file.readline() reads the first line of the file
        # .strip() removes any spaces or new-line characters
        n = int(file.readline().strip())

        # I create array A from the second line of the file
        # file.readline() reads the next line (the second one in the file), containing the numbers of the array A
        # .split() divides the string into a list of substrings, one for each number
        # map(int,..) converts each substring into an integer
        # list(..) converts the output of map into an actual list
        A = list(map(int, file.readline().strip().split()))

    # I call the function and get the partitioned array
    result = partition_array(A)
    
    # I print result as a string of numbers separated by spaces
    print(" ".join(map(str, result)))