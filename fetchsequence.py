from Bio import SeqIO

def fetch_sequence(file_path):
    """
    Returns the DNA sequence when input is entered as a FASTA file with coordinates.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Initialize an empty string for the sequence
    sequence = ""
    
    for line in lines:
        # Skip header lines (which start with '>')
        if not line.startswith('>'):
            # Strip newline characters and add to the sequence
            sequence += line.rstrip("\n")

    with open(file_path, 'w') as file:
        file.write(sequence)
    
    return sequence

def mismatch(off_target,sub_sequence):
    mismatches = 0
    for (i) in range(len(off_target)):
        if (off_target[i] != sub_sequence[i]):
            mismatches+=1
    return mismatches

def find_gRNAs(sequence, gRNA_length=20):
    """
    Identifies potential gRNA sequences within a given DNA sequence.

    :param pam: PAM sequence for Cas9 (default is 'NGG').
    :param gRNA_length: Length of the gRNA sequence (default is 20 nucleotides).
    :return: List of gRNA sequences as strings.
    """
    gRNAs = []
    optimised_gRNAs = []
    
    # Iterate through the sequence to find PAM sites
    for i in range(len(sequence)-1):
        # Searching for PAM
        if (sequence[i]+sequence[i+1] == "GG"):
            if (i>20):
                sub_sequence = sequence[i-gRNA_length-1:i+2]
                # Appends only unique sequences
                if (sub_sequence not in gRNAs):
                    gRNAs.append(sub_sequence)
                    
                # Optimising the sub-sequence
                if ((sub_sequence[18] == 'G' or sub_sequence[18] == 'A') and (sub_sequence[19] == 'G' or sub_sequence[19] == 'A') and (sub_sequence[17] == 'C') and sub_sequence[15]== 'C'):
                    if (sub_sequence not in optimised_gRNAs):
                        optimised_gRNAs.append(sub_sequence)


    return gRNAs, optimised_gRNAs
