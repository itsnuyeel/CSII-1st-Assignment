# EX 2: MER - Merge Two Sorted Arrays

"""""
Given: A positive integer n≤10^5 and a sorted array A[1..n] of integers from -10^5 to 10^5, a positive integer m≤10^5 and a sorted array B[1..m]
of integers from -10^5 to 10^5.

Return: A sorted array C[1..n+m] containing all the elements of A and B.
"""""

# Given an ordered array A with n elements and an ordered array B with m elements, we must combine A and B into a new array C 
# containing all elements in order

# The function accepts two ordered arrays A and B
def merge_arrays(A, B):

    # I create a C list to store the result
    C = []
    
    # I start two indices, one for A (let's call it i) and one for B (let's call it k)
    # These indices will allow us to compare the elements of A and B one at a time
    i, k = 0, 0
    n, m = len(A), len(B)
    
    # Using a while loop, I compare the current element of A (given by A[i]) with the current element of B (given by B[k])
    # And I add the lower of the two to C
    while i < n and k < m:

        # If A[i] is less than or equal to B[k], we add A[i] to C and increase i
        if A[i] <= B[k]:
            C.append(A[i])
            i += 1
        
        # Otherwise, I add B[k] to C and increase k
        else:
            C.append(B[k])
            k += 1
    
        # I repeat the process until I reach the end of one of the two arrays
            
    # If there are elements left in A (that is, i < n), I add them to C
    if i < n:
        C.extend(A[i:])
    
    # If there are elements left in B (that is, k < m), I add them to C
    if k < m:
        C.extend(B[k:])
    
    return C

# Statement for test code
if __name__ == "__main__":
    with open("./datasets-pt2/ex2/rosalind_mer.txt", "r") as file:
        
        # I read the value n and A, then m and B, from the input file

        n = int(file.readline().strip())
        A = list(map(int, file.readline().strip().split()))
        m = int(file.readline().strip())
        B = list(map(int, file.readline().strip().split()))

    # By calling the function, I obtain the sorted array C, and print it in a single line
    result = merge_arrays(A, B)
    print(" ".join(map(str, result)))