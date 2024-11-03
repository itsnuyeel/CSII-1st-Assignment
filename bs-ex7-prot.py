# EX 7: PROT - Translating RNA into Protein

"""""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""""

# The codon table is a map showing how RNA nucleotide sequences (consisting of adenine ‘A’, cytosine ‘C’, guanine ‘G’ and uracil ‘U’) 
# are translated into amino acids, which are the building blocks of proteins

# Each amino acid is encoded by a sequence of 3 nucleotides, called a codon. There are 64 possible combinations of codons 
# (since 4^3=64), but only 20 common amino acids, so some codons correspond to the same amino acid.
# ex: UAA → Stop codon (does not correspond to an amino acid)

# Function that takes a string of RNA as input
def RNAtoProtein(rna):

    # The codon_table variable is a dictionary that maps codons (keys) to amino acids (values)
    codon_table = {
        'UUU': 'F',    'CUU': 'L',    'AUU': 'I',    'GUU': 'V',
        'UUC': 'F',    'CUC': 'L',    'AUC': 'I',    'GUC': 'V',
        'UUA': 'L',    'CUA': 'L',    'AUA': 'I',    'GUA': 'V',
        'UUG': 'L',    'CUG': 'L',    'AUG': 'M',    'GUG': 'V',
        'UCU': 'S',    'CCU': 'P',    'ACU': 'T',    'GCU': 'A',
        'UCC': 'S',    'CCC': 'P',    'ACC': 'T',    'GCC': 'A',
        'UCA': 'S',    'CCA': 'P',    'ACA': 'T',    'GCA': 'A',
        'UCG': 'S',    'CCG': 'P',    'ACG': 'T',    'GCG': 'A',
        'UAU': 'Y',    'CAU': 'H',    'AAU': 'N',    'GAU': 'D',
        'UAC': 'Y',    'CAC': 'H',    'AAC': 'N',    'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q',    'AAA': 'K',    'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q',    'AAG': 'K',    'GAG': 'E',
        'UGU': 'C',    'CGU': 'R',    'AGU': 'S',    'GGU': 'G',
        'UGC': 'C',    'CGC': 'R',    'AGC': 'S',    'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R',    'AGA': 'R',    'GGA': 'G',
        'UGG': 'W',    'CGG': 'R',    'AGG': 'R',    'GGG': 'G'
    }

    # String to store the translated amino acids.
    protein = ""

    # The loop starts at 0 and continues up to the length of the RNA string, incrementing by 3 at each iteration
    # This is used to take each 3-nucleotide sequence (one codon) from the RNA string
    for i in range(0, len(rna), 3):
       
        # This extracts the substring from position i to i + 3
        # The notation i:i + 3 indicates that we are taking characters from i up to (but not including) i + 3, 
        # so we are obtaining a codon consisting of 3 nucleotides
        codon = rna[i:i + 3]

        # This checks if we have a complete codon of 3 nucleotides
        # This is important because at the end of the RNA sequence we may have incomplete nucleotides
        if len(codon) == 3:

            # Use the codon as a key to search in the codon_table dictionary
            # For example, if codon = ‘AUG’, we get amino_acid = ‘M ’ (Methionine)
            amino_acid = codon_table[codon]
            
            # This checks whether we have encountered a stop codon (UAA, UAG, or UGA)
            # break immediately exits the for loop, terminating the translation
            if amino_acid == 'Stop':
                break
                
            # If it is not a stop codon, it adds the amino acid to the protein string
            protein += amino_acid

    return protein


# Statement for test code
if __name__ == "__main__":

    with open("./datasets-pt1/ex7/rosalind_prot.txt", "r") as file:
        rosalind = file.read() 

    print(RNAtoProtein(rosalind))