# EX 9: HAMM - 	Counting Point Mutations

"""""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding 
symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)
"""""

def hamming_distance(s, t):
    result = 0

    # I use the range function and the positions (i) in order to spot the different 
    # element (for each position) between the two strings

    for i in range(len(s)):

        # if the letter in position 'i' in "s" is different from the letter 
        # in position 'i' of "t"--> increase the distance (result) by 1
         
        if s[i] != t[i]:
            result += 1

    return result


# Statement for test code
if __name__ == "__main__":
    
    with open("./datasets-pt1/ex9/rosalind_hamm.txt", "r") as file:
        
        # Since the function requires two arguments (s and t), I must have them both read from the file.
        s = file.readline().strip()
        t = file.readline().strip()

    test_result = hamming_distance(s, t)
    print (test_result)