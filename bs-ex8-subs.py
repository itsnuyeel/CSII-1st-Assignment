# EX 8: SUBS - Finding a Motif in DNA

"""""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""""

# I need to find all positions where a shorter string (t) appears within a longer string (s).
def find_locations(s, t):

    # List for storing the positions found (initially empty).
    positions = []

    # I calculate the length of the two strings.
    len_s = len(s)
    len_t = len(t)

    # I scroll the string s from left to right, one position at a time.
    # The range goes from 0 to len_s - len_t, because the last valid substring of length len_t starts at index len_s - len_t.
    for i in range(len_s - len_t + 1):

        # In each iteration of the loop, I extract a substring of s of length len_t.
        # This substring starts at position i and ends at position i + len_t - 1.
        current_substring = s[i:i + len_t]
        
        # I compare the extracted current_substring with the substring t.
        if current_substring == t:

            # If we have found a match, we add the position (1-based) to the positions list
            # I add 1 because the indexing required by the problem is 1-based, whereas Python uses 0-based indexing.
            positions.append(i + 1)
    
    # At the end of the function, I return the list containing all the positions found.
    return positions


# Statement for test code
if __name__ == "__main__":
    
    with open("./datasets-pt1/ex8/rosalind_subs.txt", "r") as file:
        
        # Since the function requires two arguments (s and t), I must have them both read from the file
        s = file.readline().strip()
        t = file.readline().strip()

    result = find_locations(s, t)
    for positions in result:
        print(positions, end=" ")