# EX 4: PAR3 - 3-Way Partition

"""""
Given: A positive integer n≤10^5 and an array A[1..n] of integers from -10^5 to 10^5.

Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for all 1≤i≤q-1, B[i]=A[1]
for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
"""""

# The ‘3-way’ partition divides the array into 3 sections:
# a part of minor values, a part of equal values and a part of major values in relation to a reference element (in this case 
# the first element A[1] (or A[0] in Python - the pivot))

# I will use 3 temporary lists: one for pivot minor elements, one for pivot equals and one for pivot major elements.
# I will scroll through all the elements of array A and place them in one of 3 lists, depending on the pivot comparison.
# In the end, I will combine these 3 lists into one, which will represent the result B.

def three_way_partition(A):
    
    # I set the first element of the array as pivot
    pivot = A[0]
    
    # Empty lists to collect the minor, equal and major values of the pivot respectively
    minor = []   # values < pivot
    equal = []    # values = pivot
    greater = [] # values > pivot
    
    # Iteration on the elements of A to distribute the values in the 3 lists
    for element in A:

        # If the element is less than the pivot, it is added to "minor"
        if element < pivot:
            minor.append(element)
        
        # If the element is equal to the pivot, it is added to "equal"
        elif element == pivot:
            equal.append(element)
        
        # If the element is greater than the pivot, it is added to "greater"
        else:
            greater.append(element)

    # I combine the 3 lists into a new list containing all elements of array A sorted according to the partition criteria
    return minor + equal + greater


# Statement for test code
if __name__ == "__main__":
    with open("./datasets-pt2/ex4/rosalind_par3.txt", "r") as file:
        
        # I read and discard the first line
        file.readline()
        
        # I read array A from the second line onwards
        A = list(map(int, file.readline().strip().split()))
    
    # I call the function and print the resulting array
    result = three_way_partition(A)
    
    # I print the result as a space-separated string
    print(" ".join(map(str, result)))