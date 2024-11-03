# EX 4: IPRB - 	Mendel's First Law

"""""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous 
dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""""

def dominant_probability(k, m, n):

    total = k + m + n

    # This formula calculates the total number of possible pairs in a population of total individuals:
    # 1. I subtract -1 in view of the fact that the second individual has one less chance compared to the first --> It serves to ensure 
    # that I am not considering a pair in which the same individual is selected twice.
    # 2. I divide by two to avoid counting the same pair twice.
     
    total_pairs = total * (total - 1) / 2
    
    # sum of all pairs with dominant offspring, with their specific probabilities
    dominant_pairs = (

        # AA-AA pairs (100% dominant) - k=AA 
        # it calculates the number of ways to choose two AA individuals from the population
        k * (k - 1) / 2     

        # AA-Aa pairs (100% dominant) - m=Aa 
        # k * m is the number of ways to make a pair between an individual AA and an individual Aa 
        + k * m

        # # AA-aa pairs (100% dominant) - n=aa 
        # k * n is the number of ways to make a pair between an individual AA and an individual aa             
        + k * n

        # # Aa-Aa pairs (75% dominant)
        # m * (m - 1) / 2 calculates the number of ways of forming pairs between two individuals Aa 
        # Since these pairs produce dominant offspring only 75% of the time, I multiply this value by 0.75              
        + m * (m - 1) / 2 * 0.75 

        # Aa-aa pairs (50% dominant)
        # m * n is the number of ways to form pairs between individuals Aa and aa
        # Since these pairs produce dominant offspring only 50% of the time, I multiply by 0.5
        + m * n * 0.5        
    )
    
    # Calculates the overall probability of having a dominant descendant
    # dominant_pairs represents the total number of pairs producing dominant offspring
    # total_pairs represents all possible pairs.
    return dominant_pairs / total_pairs


# Statement for test code
if __name__ == "__main__":

    with open("./datasets-pt1/ex4/rosalind_iprb.txt", "r") as file:
        rosalind = file.read().strip()  # strip() deletes unwanted characters before passing the string to the function

        # I need to convert the string read from the file into 3 integers (the ones required by our function - k,m,n):
        
        # rosalind.split() method splits the string according to spaces and returns a list of values (in this case, strings representing numbers)
        # map(int,..) converts each string in the resulting list into an integer
        # k, m, n = ... assigns the 3 values in the list to k, m, and n
        k, m, n = map(int, rosalind.split())
        
    print(dominant_probability(k, m, n))