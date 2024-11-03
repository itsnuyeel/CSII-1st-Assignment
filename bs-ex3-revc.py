# EX 3: REVC - 	Complementing a Strand of DNA

"""""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, then taking the complement of 
each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement s^c of s
"""""

def ReverseComplement(dna):
    
    # A dictionary to associate each symbol to its complement
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # An empty string to contain the reverse complement
    reverse_complement = ""
    
    # I use range (range(start, stop, step)) to include the indices of the dna string in reverse order (from last to first). 
    # The index of the last character is given by the length of dna - 1 (our "start"). 
    # The arrival limit is -1 (value not included), in order to stop just before index 0 (our "stop").
    # Our "step" is also -1, so that with each iteration the range decreases by one, allowing us to scroll the string backwards.

    for i in range(len(dna) - 1, -1, -1):  

        # I access each character of the dna string using its index i
        base = dna[i]    

        # I add the complement of each character to the final string   
        reverse_complement += complement[base]  
    
    return reverse_complement


# Statement for test code
if __name__ == "__main__":

    with open("./datasets-pt1/ex3/rosalind_revc.txt", "r") as file:
        rosalind = file.read().strip()  # strip() deletes unwanted characters before passing the string to the function

    print(ReverseComplement(rosalind))
