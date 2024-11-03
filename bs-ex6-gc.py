# EX 6: GC - Computing GC Content

"""""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.
"""""

def GCcontent(dna):
    result = 0

    # I create 2 variables to count C and G
    count_C = 0
    count_G = 0

    # every time there will be C or G in the dna string --> add 1 to the counter
    for nucleotide in dna:
        if nucleotide =="C":
            count_C += 1
        if nucleotide =="G":
            count_G += 1

    # I create a new variable that contains the sum of the count of C and G
    countCG = count_C + count_G

    # I calculate the percentage: count of C and G, divided by the lenght of the dna and multiplied by 100
    result = (countCG / len(dna) *100)

    return result

# This function takes as input a list of strings (fasta_data), which contains data in FASTA format, and returns the ID of the sequence 
# with the highest GC content, together with the value of that content in percentage.
# The fasta_data parameter will be a list of text lines, each representing a line in the FASTA file.
def find_highest_GCcontent(fasta_data):

    # This variable will store the ID of the sequence with the highest GC content (initially it's an empty string)
    highest_gc_id = ""

    # This variable will store the value of the highest GC content found (initially set to 0.0)
    highest_gc_content = 0.0

    # This variable stores the ID of the current sequence
    current_id = ""

    # This variable stores the DNA sequence associated with the current ID
    # Each time we find a new ID, we reset this variable to build the new sequence
    current_sequence = ""

    # I start a for loop to scroll through each row of fasta_data
    for line in fasta_data:

        # Removes blank spaces or newline characters (\n) at the beginning and end of the line
        line = line.strip()

        # It checks whether the line starts with the character >, which indicates that it is an ID in FASTA format  
        if line.startswith(">"):  

            # This section checks whether we have already constructed a current_sequence (so we are not on the first line of the file)
            if current_sequence:

                # I call the CGcontent function to calculate the GC content of the current_sequence
                gc_content = GCcontent(current_sequence)

                # If the GC content of the current sequence is greater than highest_gc_content:
                if gc_content > highest_gc_content:

                    # I update highest_gc_content with the new GC value
                    highest_gc_content = gc_content

                    # I update highest_gc_id  with the ID associated with this sequence
                    highest_gc_id = current_id

            # This part of the code updates the current sequence ID with the new current_id (without the >) 
            # and resets current_sequence to prepare for collecting the new DNA sequence
            current_id = line[1:]
            current_sequence = ""
        
        # If the line is not an ID (does not start with >), then it is a part of the DNA sequence
        # The += concatenation adds this line to the current_sequence
        else:
            current_sequence += line  # Aggiunge la sequenza al corrente ID

    # This section handles the last sequence found in the file, as it may not have a new > after it to trigger the calculation
    if current_sequence:

        # I calculate the GC content of current_sequence
        gc_content = GCcontent(current_sequence)

        # I compare and, if it is greater than highest_gc_content, I update highest_gc_content and highest_gc_id as explained before
        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_gc_id = current_id

    # The function returns the ID of the sequence with the highest GC content and the value of that content.
    return highest_gc_id, highest_gc_content

# Statement for test code
if __name__ == "__main__":
    with open("./datasets-pt1/ex6/rosalind_gc.txt", "r") as file:
        fasta_data = file.readlines()
    
    highest_gc_id, highest_gc_content = find_highest_GCcontent(fasta_data)
    print(highest_gc_id)

    # It ensures that the value of highest_gc_content is printed with six decimal digits
    print(f"{highest_gc_content:.6f}")