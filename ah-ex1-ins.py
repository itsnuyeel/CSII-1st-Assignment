# EX 1: INS - Computing the number of swaps in insertion sort

"""""
Given: A positive integer n≤10^3 and an array A[1..n] of integers.
Return: The number of swaps performed by insertion sort algorithm on A[1..n].
"""""

def swaps_number(array):

    # Variable to keep track of the total number of swaps
    swap_count = 0  

    # I start iterating from index 1 to the end of the array
    # I start from the second element (index 1), because the first one is already "sorted"
    for i in range(1, len(array)):

        # It represents the current element to be inserted in the correct position
        current_element = array[i]

        # h is the index of the previous element
        h = i - 1  

        # Using a while loop, I compare current_element with previous elements
        # If an element is greater than current_element, I move it forward and increase the swap counter
        while h >= 0 and array[h] > current_element:
            
            # I move the element forward
            array[h + 1] = array[h]  
            
            # I continue to compare the previous element
            h -= 1  
            
            # I increase the swap counter
            swap_count += 1  

        # I insert the element in the correct position
        array[h + 1] = current_element  

    # I return the total number of swaps
    return swap_count  


# Statement for test code
if __name__ == "__main__":
    
    with open("./datasets-pt2/ex1/rosalind_ins.txt", "r") as file:
        
        # I read all the lines and divide them into separate lines
        lines = file.readlines()
    
    # the input will consist of 2 lines: the first line with the number of elements and the second line with the values of the array.
    
    # With this I read the length of the array
    n = int(lines[0].strip())

    # With this I read the array (with its elements) as a list of integers
    array = list(map(int, lines[1].strip().split()))  

    # The function is called and the result is printed
    result = swaps_number(array)
    
    # Output: The code will print out the number of exchanges performed by the sorting algorithm
    print(result)  
    