# EX 5: FIB - Rabbits and Recurrence Relations

"""""
Given: Positive integers n≤40 and k≤5
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""""

def rabbit_pairs(n, k):

    # I open a list where the two values represent the number of pairs in the first 2 months (1 pair for each month)
    rabbits = [1, 1]
    
    # A for loop to calculate the number of pairs for each successive month
    # I start from month 3 (index 2) and calculate the number of rabbit pairs for each month up to month n
    for month in range(2, n):  

        # This formula uses the last value in the list (rabbits[-1], representing f(n-1)) 
        # and the penultimate value (rabbits[-2], representing f(n-2))
        # Every month we add the calculated value to the rabbits list with rabbits.append()
        rabbits.append(rabbits[-1] + k * rabbits[-2])
    
    # rabbits[-1] will contain the total number of pairs in the month n
    return rabbits[-1]


# Statement for test code
if __name__ == "__main__":

    file = open("./datasets-pt1/ex5/rosalind_fib.txt", "r")
    rosalind = file.read().strip()

    n, k = map(int, rosalind.split())

    print(rabbit_pairs(n, k))