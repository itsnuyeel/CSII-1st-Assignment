# EX 1: DNA - 	Counting DNA Nucleotides

"""""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""""

def countNucleotides(input_dna):
    
    # I create a list within a variable that'll store the counter of the recurrence of each nucleotide
    result = [0, 0, 0, 0]
    
    # I use a for loop to count the recurrence of each nucleotide
    for nucleotide in input_dna:
        # if nucleotide is 'A' --> increase position 0 in the list "result" by 1
        if nucleotide =="A":
            result[0] = result[0]+1
        elif nucleotide =="C":
            result[1] = result[1]+1
        elif nucleotide =="G":
            result[2] = result[2]+1
        elif nucleotide =="T":
            result[3] = result[3]+1

    return result


# Statement for test code
if __name__ == "__main__":
    
    file = open("./datasets-pt1/ex1/rosalind_dna.txt", "r")
    rosalind = file.read()

    result2 = countNucleotides(rosalind)
    for count in result2:
        print(count, end=" ")