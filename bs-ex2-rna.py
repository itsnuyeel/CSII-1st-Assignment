# EX 2: RNA - Transcribing DNA into RNA

"""""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t
with 'U' in u.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""""

def DNAtoRNA(input_dna):
    result = ''

    # I use the for loop to replace 'T' with 'U' in the DNA string

    for nucleotide in input_dna:
        # if nucleotide is 'T' --> add 'U' to the string result
        if nucleotide =="T":
            result +="U"
        # otherwise --> add the same nucleotide to the string result
        else:
            result += nucleotide

    return result


# Statement for test code
if __name__ == "__main__":

    file = open("./datasets-pt1/ex2/rosalind_rna.txt", "r")
    rosalind = file.read()

    print(DNAtoRNA(rosalind))
